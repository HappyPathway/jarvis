import openai
import os

def upload_file_to_openai(file_path):
    try:
        with open(file_path, 'rb') as file:
            response = openai.File.create(file=file, purpose='fine-tune')
        print(f"File uploaded successfully: {response['id']}")
    except Exception as e:
        print(f"An error occurred: {e}")
