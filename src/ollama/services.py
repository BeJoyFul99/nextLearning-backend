import ollama
from os import environ as env

desiredModel = env['OLLAMA_MODEL']
ollama_api_url = env['OLLAMA_API_URL']
oClient = ollama.Client(host=ollama_api_url)

def get_answer(question: str) -> list:
    res = oClient.chat(model=desiredModel, messages=[
        {"role": "user", "content": question}
    ])
        
    return res