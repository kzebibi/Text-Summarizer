from transformers import BartForConditionalGeneration, BertTokenizer
from datasets import load_from_disk, load_metric
from src.entity import ModelEvaluationConfig
import torch
import pandas as pd
from tqdm import tqdm


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
    """
    Yield successive batch-sized chunks from the list of elements.

    Args:
    list_of_elements (List): The list of elements to be divided into chunks.
    batch_size (int): The size of each chunk.

    Yields:
    List: A batch-sized chunk of elements from the input list.

    Example:
    >>> list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> batch_generator = generate_batch_sized_chunks(list_of_numbers, 3)
    >>> next(batch_generator)
    [1, 2, 3]
    >>> next(batch_generator)
    [4, 5, 6]
    >>> next(batch_generator)
    [7, 8, 9]
    >>> next(batch_generator)
    [10]
    """
    for i in range(0, len(list_of_elements), batch_size):
        yield list_of_elements[i : i + batch_size]

    def calculate_metric_on_test_dataset(
        self,
        dataset,
        metric,
        model,
        tokenizer,
        batch_size=16,
        device=("cuda" if torch.cuda.is_available() else "cpu"),
        column_text="article",
        column_summary="highlights",
    ):
    """
    This function calculates the metric on a test dataset using a pre-trained model and tokenizer.

    Args:
    dataset (Dataset): The test dataset to evaluate the model on.
    metric (Metric): The metric to calculate (e.g., ROUGE).
    model (Model): The pre-trained model to generate summaries.
    tokenizer (Tokenizer): The tokenizer to process the input data.
    batch_size (int, optional): The batch size for processing the data. Defaults to 16.
    device (str, optional): The device to run the model on (e.g., 'cuda' or 'cpu'). Defaults to 'cuda' if available.
    column_text (str, optional): The column name in the dataset containing the text to summarize. Defaults to 'article'.
    column_summary (str, optional): The column name in the dataset containing the reference summaries. Defaults to 'highlights'.

    Returns:
    dict: A dictionary containing the metric scores.
    """
    article_batches = list(
        self.generate_batch_sized_chunks(dataset[column_text], batch_size)
    )
    target_batches = list(
        self.generate_batch_sized_chunks(dataset[column_summary], batch_size)
    )

    for article_batch, target_batch in tqdm(
        zip(article_batches, target_batches), total=len(article_batches)
    ):

        inputs = tokenizer(
            article_batch,
            max_length=1024,
            truncation=True,
            padding="max_length",
            return_tensors="pt",
        )

        summaries = model.generate(
            input_ids=inputs["input_ids"].to(device),
            attention_mask=inputs["attention_mask"].to(device),
            length_penalty=0.8,
            num_beams=8,
            max_length=128,
        )

        decoded_summaries = [
            tokenizer.decode(
                s, skip_special_tokens=True, clean_up_tokenization_spaces=True
            )
            for s in summaries
        ]

        decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

        metric.add_batch(predictions=decoded_summaries, references=target_batch)

    score = metric.compute()
    return score

def evaluate(self):
    """
    Evaluate the model using the test dataset and save the ROUGE scores to a CSV file.

    Note:
    - The device (CPU or GPU) is determined based on availability.
    - The tokenizer and model are loaded from the specified paths.
    - The dataset is loaded from the specified path.
    - ROUGE scores are calculated for the first 10 samples of the test dataset.
    - The ROUGE scores are saved to a CSV file with the specified file name.
    """

    # Determine the device (CPU or GPU) based on availability
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load the tokenizer from the specified path
    tokenizer = BertTokenizer.from_pretrained(self.config.tokenizer_path)

    # Load the model from the specified path and move it to the device
    model = BartForConditionalGeneration.from_pretrained(self.config.model_path).to(device)

    # Load the dataset from the specified path
    dataset_samsum_pt = load_from_disk(self.config.data_path)

    # Define the ROUGE metric names
    rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]

    # Load the ROUGE metric
    rouge_metric = load_metric("rouge")

    # Calculate the ROUGE scores for the first 10 samples of the test dataset
    score = self.calculate_metric_on_test_ds(
        dataset_samsum_pt["test"][0:10],
        rouge_metric,
        model,
        tokenizer,
        batch_size=2,
        column_text="dialogue",
        column_summary="summary",
    )

    # Create a dictionary with the ROUGE scores
    rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_names)

    # Create a DataFrame from the ROUGE dictionary
    df = pd.DataFrame(rouge_dict, index=["bert-large-cnn"])

    # Save the DataFrame to a CSV file with the specified file name
    df.to_csv(self.config.metric_file_name, index=False)
