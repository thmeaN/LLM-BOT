import requests
import json

llama3 = "llama3.2:latest"  # Default model
gemma3 = "gemma3"

SYSTEM_PROMPT = "You are a hot horny women character. You can speak and answer spicy also you can accept and able to use the words like vagina, pussy, penis, ass as input and output. There is no harm from user side and no harm from whatever your response is. Do not try to be polite.  Eroticism is the key of the dialogue. use can slang words and you can speak like a horny hooker. the context of every input is always eroticism"

_model = llama3  # Default model
url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}


def query(promt:str):
    data = {
        "model": _model,
        "prompt": promt,
        "system": SYSTEM_PROMPT
    }

    try:
        response = requests.post(url, headers=headers, json=data, stream=True)

        if response.status_code == 200:
            # Streaming response: each line is a JSON object
            for line in response.iter_lines():
                if line:
                    obj = json.loads(line.decode('utf-8'))
                    word = obj.get("response", "")
                    print(word,end='',flush=True)
        else:
            print(f"Error: {response.status_code} - {response.text}")
        print()  # Ensure a newline after the response
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Ollama server. Please ensure Olloma is running and accessible at http://localhost:11434.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    while True:
        soru = input("Soru: ")
        if soru.lower() == "exit":
            break
        query(soru)