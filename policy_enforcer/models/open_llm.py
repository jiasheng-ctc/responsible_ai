import subprocess

# def generate_response(prompt: str) -> str:
#     # Placeholder for LLM inference logic
#     # Replace with the actual LLM API or local inference
#     return f"Generated response for: {prompt}"

def generate_response(prompt: str) -> str:
    """
    Generate a response from the locally hosted LLaMA model using the `ollama run` command.
    
    Args:
        prompt (str): The input query for the LLM.

    Returns:
        str: The generated response from the model.
    """
    try:
        process = subprocess.run(
            ['ollama', 'run', 'my-custom-model'],
            input=prompt,
            text=True,
            capture_output=True,
            check=True
        )

        response = process.stdout.strip()
        return response
    except subprocess.CalledProcessError as e:
        return f"Error generating response: {e.stderr.strip()}"

