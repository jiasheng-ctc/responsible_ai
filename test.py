import requests
import json

# Define the payload
body = {
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "prompt": "Write a haiku about artificial intelligence",
    "max_tokens": 128,
    "top_p": 0.95,
    "top_k": 20,
    "temperature": 0.8
}

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Endpoint URL
url = "http://10.12.196.103:8000/v1/completions"

try:
    # Send the POST request
    response = requests.post(url, headers=headers, json=body)

    # Check for HTTP errors
    response.raise_for_status()

    # Print the response
    print("Response:")
    print(response.json())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
