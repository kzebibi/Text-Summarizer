import os
from src.logger import logging
from transformers import BartTokenizer
from datasets import load_dataset, load_from_disk
from src.entity import DataTransfomationConfig

class DataTransformation:
    def __init__(self, config: DataTransfomationConfig):
        self.config = config
        self.tokenizer = BartTokenizer.from_pretrained(str(config.tokenizer_name))
        
    def convert_examples_to_features(self, example_batch):
        input_encoding = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)
        
        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)
            
        return {
            'input_ids': input_encoding['input_ids'],
            'attention_mask': input_encoding['attention_mask'],
            'decoder_input_ids': target_encoding['input_ids'],
            'decoder_attention_mask': target_encoding['attention_mask'],
        }
    
    def convert(self):
        # Ensure the paths are converted to strings
        dataset_samsum = load_from_disk("artifacts/data_ingestion/samsum_dataset")
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(str(self.config.root_dir), "samsum_dataset"))
