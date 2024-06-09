from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import BartForConditionalGeneration, BartTokenizer
from datasets import load_from_disk
from src.entity import ModelTrainerConfig
import torch


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = BartTokenizer.from_pretrained(self.config.model_ckpt)
        model_bert = BartForConditionalGeneration.from_pretrained(
            self.config.model_ckpt
        ).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_bert)

        # loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            overwrite_output_dir=self.config.overwrite_output_dir,
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
            adam_epsilon=self.config.adam_epsilon,
            weight_decay=self.config.weight_decay,
        )

        model_trainer = Trainer(
            model=model_bert,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_samsum_pt["train"],
            eval_dataset=dataset_samsum_pt["test"],
        )

        model_trainer.train()

        # Save model and tokenizer
        model_dir = os.path.join(self.config.root_dir, "bart-large-cnn-model")
        tokenizer_dir = os.path.join(self.config.root_dir, "bart-large-cnn-tokenizer")

        # Ensure the directories exist
        os.makedirs(model_dir, exist_ok=True)
        os.makedirs(tokenizer_dir, exist_ok=True)

        model_bert.save_pretrained(model_dir)
        tokenizer.save_pretrained(tokenizer_dir)
