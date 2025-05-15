import os
from openai import OpenAI

# Initialize Groq client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://console.groq.com/keys để lấy API Key nha
    api_key='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',
)

# create a list to store messages
messages = []

# get question from user
while True:
    question = input("Question(If you want to exit, please enter 'exit'): ")
    if question == "exit":
        break   

    # add question to message
    messages.append({
        "role": "user", 
        "content": question
        })

    stream = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        stream=True
    )

    # print the answer  
    print("\nAnswer: ", end="")
    assistant_response = ""
    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        assistant_response += content
        print(content, end="")
    print("\n")

    # add assistant response to message
    messages.append({
        "role": "assistant", 
        "content": assistant_response
        })
    



