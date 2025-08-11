# Medical RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with Flask and LangChain for answering medical queries using the GALE Encyclopedia of Medicine as the knowledge base.

## Features

- **Medical Knowledge Base**: Uses the GALE Encyclopedia of Medicine (Second Edition) as the primary data source
- **RAG Architecture**: Combines retrieval and generation for accurate, context-aware responses  
- **Vector Database**: FAISS-powered vector store for efficient similarity search
- **Web Interface**: Clean Flask-based web UI for chat interactions
- **Session Management**: Maintains conversation history during user sessions
- **Logging**: Comprehensive logging system for debugging and monitoring
- **Hugging Face Integration**: Powered by Mistral-7B-Instruct-v0.3 model

## Architecture

```
├── app/
│   ├── application.py          # Flask web application
│   ├── components/
│   │   ├── data_loader.py      # PDF document loading
│   │   ├── embeddings.py       # Text embeddings generation
│   │   ├── llm.py             # Language model integration
│   │   ├── pdf_loader.py      # PDF processing utilities
│   │   ├── retriever.py       # QA chain and retrieval logic
│   │   └── vector_store.py    # FAISS vector database
│   ├── config/
│   │   └── config.py          # Configuration settings
│   ├── common/
│   │   ├── custom.py          # Custom exceptions
│   │   └── logger.py          # Logging utilities
│   └── template/
│       └── index.html         # Web interface
├── data/                      # Medical documents
├── vector_store/              # FAISS database files
└── logs/                      # Application logs
```

## Prerequisites

- Python 3.8+
- Hugging Face account and API token
- Sufficient disk space for vector database storage

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd medical_rag
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   ```bash
   export HF_TOKEN="your_huggingface_token"
   export HFHUB_TOKEN="your_huggingface_hub_token"
   ```

4. **Install the package:**
   ```bash
   pip install -e .
   ```

## Usage

1. **Start the Flask application:**
   ```bash
   python app/application.py
   ```

2. **Access the web interface:**
   Open your browser and navigate to `http://localhost:5000`

3. **Ask medical questions:**
   - Type your medical query in the chat interface
   - The system will search the medical encyclopedia and provide relevant answers
   - Use the "Clear" button to reset the conversation

## Configuration

Key settings in `app/config/config.py`:

- `HF_REPO_ID`: Hugging Face model identifier (default: Mistral-7B-Instruct-v0.3)
- `CHUNK_SIZE`: Text chunk size for document processing (default: 500)
- `CHUNK_OVERLAP`: Overlap between text chunks (default: 50)
- `DB_FAISS_PATH`: Vector database storage path

## API Endpoints

- `GET/POST /`: Main chat interface
- `GET /clear`: Clear conversation history

## Data Source

The chatbot uses "The GALE ENCYCLOPEDIA of MEDICINE SECOND" as its primary knowledge source, providing comprehensive medical information across various topics.

## Logging

Application logs are stored in the `logs/` directory with daily rotation. Log levels and formats can be configured in `app/common/logger.py`.

## Limitations

- Responses are limited to information contained in the medical encyclopedia
- Not a substitute for professional medical advice
- Retrieval accuracy depends on query formulation and document chunking

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests (if available)
5. Submit a pull request

## License

This project is developed by Sudhanshu. Please check with the author for licensing terms.

## Disclaimer

**This chatbot is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.**