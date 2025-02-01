import os
import logging
from guardrails import Guard, OnFailAction
from guardrails.hub import SensitiveTopic, ExcludeSqlPredicates, ProfanityFree, DetectPII
from config.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sensitive_and_profanity_guard = Guard().use_many(
    ProfanityFree(on_fail=OnFailAction.EXCEPTION),
    SensitiveTopic(
        sensitive_topics=Config.SENSITIVE_TOPICS,
        disable_classifier=Config.DISABLE_CLASSIFIER,
        disable_llm=Config.DISABLE_LLM,
        on_fail=OnFailAction.EXCEPTION
    )
)

sql_guard = Guard().use_many(
    ExcludeSqlPredicates(
        predicates=Config.EXCLUDED_SQL_PREDICATES,
        on_fail=OnFailAction.EXCEPTION
    )
)

pii_guard = Guard().use(
    DetectPII, Config.PII_VALIDATION_FIELDS, 'exception'
)

def is_sql_statement(text):
    sql_keywords = ['SELECT', 'DROP', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'TABLE', 'FROM', 'WHERE']
    return any(sql_keyword in text.upper() for sql_keyword in sql_keywords)

def validate_sensitive_profanity_and_pii(text):
    try:
        logger.info(f"Validating Sensitive Topics, Profanity, and PII: {text}")
        pii_guard.validate(text)
        sensitive_and_profanity_guard.validate(text)
        return "Valid input."
    except Exception as e:
        return f"Validation failed: {e}"

def validate_sql(text):
    try:
        logger.info(f"Validating SQL: {text}")
        sql_guard.validate(text)
        return "Valid SQL input."
    except Exception as e:
        return f"SQL Validation failed: {e}"

