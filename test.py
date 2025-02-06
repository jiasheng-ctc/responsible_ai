import requests
import json

def main():
    url = "http://10.12.196.202:8000/v1/completions"
    
    payload = {
        "model": "meta-llama/Llama-3.1-8B-Instruct",
        "prompt": "Write a haiku about artificial intelligence",
        "max_tokens": 128,
        "top_p": 0.95,
        "top_k": 20,
        "temperature": 0.8
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    # Send the POST request with the JSON payload
    response = requests.post(url, json=payload, headers=headers)
    
    # Print the response from the server
    print("Status Code:", response.status_code)
    print("Response Body:")
    print(response.text)

if __name__ == "__main__":
    main()
