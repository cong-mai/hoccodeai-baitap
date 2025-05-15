import os
from openai import OpenAI

# Initialize Groq client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    # Làm theo hướng dẫn trong bài, truy cập https://console.groq.com/keys để lấy API Key nha
    api_key='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',
)

input_file = input("Enter the path to the file (.txt): ").strip()
target_lang = input("Enter target language (Vietnamese, Spanish, etc): ")

try:
     # Verify file is .txt
    if not input_file.endswith('.txt'):
        print("Error: Please select a .txt file")
        exit()
    
    # Convert to raw string to handle Windows paths
    input_file = rf"{input_file}"
    # Read the input file
    print(f"\nReading file: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    # Split into words
    words = text.split()
    total_words = len(words)
    current_position = 0
    translations = []
    
    print("processing...")
    # Process 500 words at a time
    while current_position < total_words:
        # Get next 500 words
        chunk = ' '.join(words[current_position:current_position + 500])

        # Translate chunk
        messages = [{
            "role": "user",
            "content": f"Translate the following text to {target_lang}: {chunk}"
        }]
        
        stream = client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            stream=True
        )
        
        # Get translation
        translation = ""
        for response in stream:
            translation += response.choices[0].delta.content or ""
        translations.append(translation)
        
        # Move to next chunk
        current_position += 500
    
    # Save all translations
    output_file = input_file.replace('.txt', '_translated.txt')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(translations))
    
    print(f"\nTranslation saved to: {output_file}")

except FileNotFoundError:
    print(f"Error: File not found: {input_file}")





