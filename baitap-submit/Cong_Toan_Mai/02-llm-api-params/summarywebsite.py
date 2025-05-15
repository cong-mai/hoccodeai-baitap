import os
import requests
from openai import OpenAI
from bs4 import BeautifulSoup

# Initialize Groq client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://console.groq.com/keys để lấy API Key nha
    api_key='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',
)

#get website content
while True:
    #Get the URL of the website
    url = input("\nEnter the URL of the website(If you want to exit, please enter 'exit'): ")
    if url == "exit":
        break  
    response = requests.get(url)
    response.raise_for_status() #check if the request is successful
    
    #parse the html with BeautifulSoup
    content = BeautifulSoup(response.text, 'html.parser')
    #get clean text content
    content = content.get_text()

    #create a summary of the content
    summary_prompt = f"""Summarize the text delimited by triple quotes, 
    providing a brief summary and list all the key words mentioned in the text
    '''{content}'''
    """
    messages = [{
        "role": "user",
        "content": summary_prompt
    }]

    stream = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        stream=True
    )
    print("\nSummary:")
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")





