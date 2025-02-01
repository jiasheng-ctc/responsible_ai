from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    DISABLE_CLASSIFIER = os.getenv('DISABLE_CLASSIFIER', 'False').lower() == 'true'
    DISABLE_LLM = os.getenv('DISABLE_LLM', 'False').lower() == 'true'
    SENSITIVE_TOPICS = os.getenv('SENSITIVE_TOPICS', '').split(',')
    EXCLUDED_SQL_PREDICATES = os.getenv('EXCLUDED_SQL_PREDICATES', '').split(',')
    PII_VALIDATION_FIELDS = os.getenv('PII_VALIDATION_FIELDS', '').split(',')

