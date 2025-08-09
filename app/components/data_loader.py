import os

from app.components.pdf_loader import load_pdf_files, chunk_documents
from app.components.vector_store import save_vector_store, load_vector_store
from app.config.config import DATA_PATH, DB_FAISS_PATH
from app.common.logger import get_logger
from app.common.custom import CustomException

logger = get_logger(__name__)

def data_loader():
    try:
        logger.info("starting data loading process...")
        data = load_pdf_files()
        if not data:
            raise CustomException("No data loaded from PDF files.")
        
        data_chunks = chunk_documents(data)
        save_vector_store(data_chunks)
        logger.info("Data loading process completed successfully.")
        return data_chunks
    except Exception as e:
        logger.error(f"An error occurred during data loading: {e}")
        raise CustomException("An error occurred while loading data.", e)
        return None
    
if __name__ == "__main__":
    try:
        data_loader()
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")