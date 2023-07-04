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
    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "You are an assistant helping to a complex code deciphering process."},
            {"role": "user", "content": prompt},
        ]
    )
    # Log the call and the full response
    logging.info(f"GPT-4 call from:\n{origin}\n\nwith prompt:\n{prompt}\n\n\n")
    logging.info(f"Full response:\n{response}\n\n\n")

    # The assistant's reply will be in the last message's 'content'
    reply = response['choices'][0]['message']['content']
    return reply
