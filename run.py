import requests
import json

if __name__ == "__main__":
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "gemma3",
        "prompt": "What is water made of?"
    }

    try:
        response = requests.post(url, headers=headers, json=data, stream=True)

        if response.status_code == 200:
            # Streaming response: each line is a JSON object
            for line in response.iter_lines():
                if line:
                    obj = json.loads(line.decode('utf-8'))
                    print(obj.get('response', ''))
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Ollama server. Please ensure Olloma is running and accessible at http://localhost:11434.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")