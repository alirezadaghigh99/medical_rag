import os
import pypdf
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom import CustomException

from app.config.config import CHUNK_SIZE, CHUNK_OVERLAP, DATA_PATH

logger = get_logger(__name__)


def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException(f"Data path '{DATA_PATH}' does not exist.")
        
        logger.info(f"Loading PDF files from directory: {DATA_PATH}")
        
        loader = DirectoryLoader(path=DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
        
        documents = loader.load()
        if not documents:
            raise CustomException("No PDF documents found in the specified directory.")
        logger.info(f"Loaded {len(documents)} PDF documents.")
        
        return documents
    except Exception as e:
        logger.error(f"Error loading PDF files: {e}")
        raise CustomException("Failed to load PDF files.", e)
        return []

def chunk_documents(documents):
    try:
        logger.info("Chunking documents...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            length_function=len
        )
        
        text_chunks = text_splitter.split_documents(documents)
        logger.info(f"Created {len(text_chunks)} text chunks from documents.")
        return text_chunks
    except Exception as e:
        logger.error(f"Error chunking documents: {e}")
        raise CustomException("Failed to chunk documents.", e)
        return []
        