from langchain.llms import openai
from app.config.config import HF_TOKEN, HF_REPO_ID, HFHuB_TOKEN, openai_api_key

from app.common.logger import get_logger
from app.common.custom import CustomException   

import os
# print(os.environ.get('OPENAI_API_KEY', "sk_default_openai_key"))
print(openai_api_key)
logger = get_logger(__name__)

def load_llm():
    try:
        logger.info("Loading LLM from HuggingFace...")
        
        llm = openai.OpenAI(openai_api_key=openai_api_key,
                            model_name="gpt-4o",
                            temperature=0.7)
        logger.info("LLM loaded successfully.")
        return llm
    except Exception as e:
        logger.error(f"Error loading LLM: {e}")
        raise CustomException("Failed to load LLM.", e)
        return None
    
    
if __name__ == "__main__":
    try:
        llm = load_llm()
        if llm:
            logger.info("LLM is ready to use.")
        else:
            logger.error("Failed to load LLM.")
    except CustomException as ce:
        logger.error(f"Custom exception occurred: {ce}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")