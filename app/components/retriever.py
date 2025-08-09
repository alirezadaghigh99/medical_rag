from langchain.chains import RetrievalQA 
from langchain_core.prompts import PromptTemplate

from app.components.llm import load_llm
from app.components.vector_store import load_vector_store
from app.common.logger import get_logger
from app.common.custom import CustomException

from app.config.config import HF_REPO_ID, HF_TOKEN, HFHuB_TOKEN

logger = get_logger(__name__)

CUSOTOM_PROMPT_TEMPLATE = """
Answer the question based on the context provided below. If the answer is not in the context, say "I don't know".
Context: {context}
Question: {question}

Answer:
"""

def set_custom_prompt():
    try:
        logger.info("Setting up custom prompt template...")
        prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=CUSOTOM_PROMPT_TEMPLATE
        )
        logger.info("Custom prompt template set successfully.")
        return prompt
    except Exception as e:
        logger.error(f"Error setting custom prompt: {e}")
        raise CustomException("Failed to set custom prompt.", e)
    
    
def create_qa_chain():
    try:
        logger.info("Creating QA chain...")
        llm = load_llm()
        if not llm:
            raise CustomException("LLM is not loaded, cannot create QA chain.")
        
        vector_store = load_vector_store()
        if not vector_store:
            raise CustomException("Vector store is not loaded, cannot create QA chain.")
        
        prompt = set_custom_prompt()
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=vector_store.as_retriever(search_kwargs={"k": 1}),
            return_source_documents=False,
            prompt=prompt,
            chian_type_kwargs={"prompt": prompt}
        )
        
        logger.info("QA chain created successfully.")
        return qa_chain
    except Exception as e:
        logger.error(f"Error creating QA chain: {e}")
        raise CustomException("Failed to create QA chain.", e)