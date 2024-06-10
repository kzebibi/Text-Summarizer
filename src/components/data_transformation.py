import os
from src.logger import logging
from transformers import BartTokenizer
from datasets import load_dataset, load_from_disk
from src.entity import DataTransfomationConfig


class DataTransformation:
    def __init__(self, config: DataTransfomationConfig):
    """
    Initialize the DataTransformation class.

    Args:
    config (DataTransfomationConfig): An instance of DataTransfomationConfig class containing configuration parameters.

    Returns:
    None
    """
    self.config = config
    self.tokenizer = BartTokenizer.from_pretrained(str(config.tokenizer_name))

    def convert_examples_to_features(self, example_batch):
    """
    Converts a batch of examples into model-ready features.

    Args:
    example_batch (dict): A batch of examples, where each example is a dictionary containing 'dialogue' and 'ummary' keys.

    Returns:
    dict: A dictionary containing the model-ready features, including 'input_ids', 'attention_mask', 'decoder_input_ids', and 'decoder_attention_mask'.
    """
    input_encoding = self.tokenizer(
        example_batch["dialogue"], max_length=1024, truncation=True
    )

    # Use the tokenizer as the target tokenizer for the target encoding
    with self.tokenizer.as_target_tokenizer():
        target_encoding = self.tokenizer(
            example_batch["summary"], max_length=128, truncation=True
        )

    return {
        "input_ids": input_encoding["input_ids"],
        "attention_mask": input_encoding["attention_mask"],
        "decoder_input_ids": target_encoding["input_ids"],
        "decoder_attention_mask": target_encoding["attention_mask"],
    }

    def convert(self):
        """
        Converts the dataset into model-ready features and saves it to disk.

        This method loads the dataset from a specified path, applies the `convert_examples_to_features` method to each example in the dataset,
        and saves the resulting dataset to a new path.

        Raises:
        FileNotFoundError: If the dataset file is not found at the specified path.
        """
        # Ensure the paths are converted to strings
        dataset_samsum = load_from_disk("artifacts/data_ingestion/samsum_dataset")

        # Apply the `convert_examples_to_features` method to each example in the dataset
        dataset_samsum_pt = dataset_samsum.map(
            self.convert_examples_to_features, batched=True
        )

        # Save the resulting dataset to a new path
        dataset_samsum_pt.save_to_disk(
            os.path.join(str(self.config.root_dir), "samsum_dataset")
        )