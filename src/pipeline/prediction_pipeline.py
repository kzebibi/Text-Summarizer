from src.configuration import ConfigurationManager
from transformers import BertTokenizer
from transformers import pipeline

class PredictionPipeline:
    """
    A class to handle text summarization using a pre-trained model.

   ...

    Attributes
    ----------
    config : ConfigurationManager
        an instance of ConfigurationManager to get model evaluation configuration

    Methods
    -------
    predict(text: str) -> str
        Summarizes the input text using the pre-trained model and returns the summary.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the PredictionPipeline class.

        config : ConfigurationManager
            an instance of ConfigurationManager to get model evaluation configuration
        """
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text: str) -> str:
        """
        Summarizes the input text using the pre-trained model and returns the summary.

        Parameters
        ----------
        text : str
            The text to be summarized.

        Returns
        -------
        str
            The summarized text.
        """
        tokenizer = BertTokenizer.from_pretrained(self.config.model_name)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 0, "max_length":128}

        summarizer = pipeline('summarization', model=self.config.model_name, tokenizer=tokenizer)

        print("Dialogue:")
        print("================================")
        print(text)

        output = summarizer(text)[0]['summary_text']

        print("================================")
        print("Summary:")
        print(output)

        return output