import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display



OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {'Content-Type': 'application/json'}
MODEL = "llama3.2"


messages = [
    {'role':'user', 'content':'Describe some of the business application of Generative AI'}

]

Payload = {
    "model":MODEL,
    "messages":messages,
    "stream":False
}

response = requests.post(OLLAMA_API, json=Payload, headers=HEADERS)

print(response.json()['message']['content'])


##### we can also use ollama module #####

# import ollama

# response = ollama.chat(model=MODEL, messages=messages)

# print(f'response from ollam: {response['message']['content']}')

