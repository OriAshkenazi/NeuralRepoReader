import os
import openai
from dotenv import load_dotenv
import logging

load_dotenv("./.env")

openai.api_key = os.getenv('OPENAI_API_KEY')
gpt_model = os.getenv('MODEL_SMART')
embedding_model = os.getenv('EMBEDDING_MODEL')

import logging

def call_gpt4(prompt, origin):
    logging.info(f"GPT-4 call from {origin} with prompt: {prompt}")
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are an assistant helping to a complex code deciphering process."},
            {"role": "user", "content": prompt},
        ]
    )
    reply = response['choices'][0]['message']['content']
    logging.info(f"GPT-4 response from {origin}\nCall: {prompt}\nResponse: {reply}")
    return reply
