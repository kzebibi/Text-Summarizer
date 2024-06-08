from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import BartForConditionalGeneration, BertTokenizer
from datasets import load_dataset, load_from_disk
from src.entity import ModelTrainerConfig
import torch





class ModelTrainer:
    def __init__(self, config):
        self.config = config
        
        
    def train(self):
        device = "cuda" if torch.is_available() else "cpu"
        tokenizer = BertTokenizer.from_pretrained(self.config.model_ckpt)
        model_bert = BartForConditionalGeneration.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_bert)
        

            
        # loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            overwrite_output_dir=True,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            save_steps=self.config.save_steps,
            save_total_limit=self.config.save_total_limit,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            metric_for_best_model=self.config.metric_for_best_model,
            load_best_model_at_end=self.config.load_best_model_at_end,
            warmup_steps=self.config.warmup_steps,
            learning_rate=self.config.learning_rate,
        )
        
        
        model_trainer = Trainer(model=model_bert, args=trainer_args,
                          tokenizer=tokenizer, datacollator=seq2seq_data_collator,
                          train_dataset=dataset_samsum_pt["train"],
                          eval_dataset=dataset_samsum_pt["test"],
                          )
        
        model_trainer.train()
        
        #save model
        model_bert.save_pretrained(os.path.join(self.config.root_dir, "bart-large-cnn-model"))
        
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "bart-large-cnn-tokenizer"))
                                   
        