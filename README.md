## Text Summarizer: Using BERT-large-CNN for Text Summarization

This project implements a text summarizer using Facebook's powerful BERT-large-CNN model in a PyTorch framework. The project focuses on providing an efficient and effective solution for summarizing textual content.

### Features

- **BERT-large-CNN model:** Utilizes the advanced BERT-large-CNN model for accurate summarization.
- **PyTorch framework:** Leverages the flexibility and efficiency of the PyTorch library.
- **Modular structure:** Organized into distinct pipelines for data ingestion, validation, transformation, training, and evaluation.
- **Web application:** Provides a user-friendly web interface for text summarization.
- **Parameter configuration:** Allows customizing the summarization process through adjustable parameters.

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/kzebibi/text_summarizer.git
cd text_summarizer
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install required packages:**

```bash
pip install -r requirements.txt
pip install --upgrade accelerate
pip uninstall -y transformers accelerate
pip install transformers accelerate
pip uninstall fsspec
pip install fsspec==2023.6.0
```

**Ensure you have `datasets==2.10.1` installed.**

### Usage

1. **Run the summarization pipeline:**

```bash
python main.py
```

This command will execute the following steps:

- Data ingestion
- Data validation
- Data transformation
- Model training
- Model evaluation

2. **Start the web application:**

```bash
python app.py
```

This will launch a web server, allowing you to input text and generate summaries.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Acknowledgments

This project leverages Facebook's BERT-large-CNN model and the PyTorch framework. The code structure and implementation draw inspiration from the provided code snippet.
