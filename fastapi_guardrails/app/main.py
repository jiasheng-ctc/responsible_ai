from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.validation.guardrails_validation import query_tinyllama, validate_sensitive_profanity_and_pii, validate_sql, is_sql_statement

app = FastAPI()
class InputText(BaseModel):
    text: str
@app.post("/validate")
def validate_input(data: InputText):
    text = data.text
    
    if is_sql_statement(text):
        sql_validation_result = validate_sql(text)
        if "failed" in sql_validation_result:
            raise HTTPException(status_code=400, detail=sql_validation_result)
    
    validation_result = validate_sensitive_profanity_and_pii(text)
    if "failed" in validation_result:
        raise HTTPException(status_code=400, detail=validation_result)
    tinyllama_response = query_tinyllama(text)
    
    return {"message": "Validation successful.", "validated_text": tinyllama_response}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True)