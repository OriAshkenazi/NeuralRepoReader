import os
import openai
import langchain

openai.api_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('MODEL_SMART')
embedding_model = os.getenv('EMBEDDING_MODEL')

def call_gpt4():
    pass