import os

HF_TOKEN = os.environ.get('HF_TOKEN', "hf_default_token")
HFHuB_TOKEN = os.environ.get('HFHUB_TOKEN', "hf_default_hub_token")
HF_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH = "vector_store/db_faiss"
DATA_PATH = "data/"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

openai_api_key = os.environ.get('OPENAI_API_KEY', "sk_default_openai_key")