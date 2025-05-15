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

print("Please enter your question (type 'exit' to quit)")
# get question from user
while True:
    question = input("Question: ")
    if question == "exit":
        break   

     # Add programming context to the question
    prompt = f"Write Python code for: {question}. Provide just only the code without any markdown formatting or ```python tags."

    # add question to message
    messages.append({
        "role": "user", 
        "content": prompt
        })

    stream = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
        stream=True
    )

  # collect and save the code
    code_response = ""
    for chunk in stream:
        code_response += chunk.choices[0].delta.content or ""

    # Save code to final.py
    with open("final.py", "w", encoding="utf-8") as f:
        f.write(code_response)
    print("Code saved to final.py")

    # add assistant response to message
    messages.append({
        "role": "assistant", 
        "content": code_response
    })