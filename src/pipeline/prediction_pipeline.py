from src.configuration import ConfigurationManager
from transformers import BertTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        
        
    def predict(self, text):
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