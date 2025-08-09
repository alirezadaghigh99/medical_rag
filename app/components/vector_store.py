from langchain_community.vectorstores import FAISS
import os

from app.components.embeddings import get_embeddings

from app.common.logger import get_logger
from app.common.custom import CustomException

from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)

def load_vector_store():
    try:
        logger.info("Loading vector store from FAISS database...")
        embeddings = get_embeddings()
        if not embeddings:
            raise CustomException("Failed to get embeddings for vector store.")
        
        if os.path.exists(DB_FAISS_PATH):
            vector_store = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
            logger.info("Vector store loaded successfully.")
            return vector_store
        
        else:
            logger.warning(f"FAISS database path '{DB_FAISS_PATH}' does not exist. Returning None.")
            return None
    except Exception as e:
        logger.error(f"Error loading vector store: {e}")
        raise CustomException("Failed to load vector store.", e)
        return None
    
def save_vector_store(text_chunks):
    try:
        logger.info("Saving text chunks to FAISS vector store...")
        embeddings = get_embeddings()
        if not embeddings:
            raise CustomException("Failed to get embeddings for saving vector store.")
        
        vector_store = FAISS.from_documents(text_chunks, embeddings)
        vector_store.save_local(DB_FAISS_PATH)
        logger.info(f"Vector store saved successfully at {DB_FAISS_PATH}.")
    except Exception as e:
        logger.error(f"Error saving vector store: {e}")
        raise CustomException("Failed to save vector store.", e)