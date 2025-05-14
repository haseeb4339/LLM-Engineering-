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

# response = requests.post(OLLAMA_API, json=Payload, headers=HEADERS)

# print(response.json()['message']['content'])


##### we can also use ollama module #####

# import ollama

# response = ollama.chat(model=MODEL, messages=messages)

# print(f'response from ollam: {response['message']['content']}')




def web_scraper(url):

   
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.title.string if soup.title else "No title found"

    for irrelevent in soup.body(['script', 'style', 'img', 'input']):
        irrelevent.decompose()

    text =  soup.body.get_text(separator="\n", strip=True)

    return title, text


web=web_scraper("https://edwarddonner.com")


# print(web[1])

    





system_prompt = "You are an assistant that analyzes the contents of a website\
    and provides a short summery, ignoring test that might be navigation related\
    Respond in markdown."



def user_prompt_for(web):
    user_prompt = f"\nYou are looking at a website titled {web.title}"
    user_prompt += "The contents of this website is as follows:\
        please provide a short summary of this website in markdown.\
        If it include news or announcements, then summarize these too.\n\n"
    
    user_prompt +=web.text
    
    return user_prompt


##### i will pass web[1]
def messages_for(web):

    return [
        {'role':'system', 'content':system_prompt},
        {'role':'user', 'content':user_prompt_for(web)}
    ]
