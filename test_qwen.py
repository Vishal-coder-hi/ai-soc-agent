import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("QWEN_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://ws-59mgowi0mha0m6y5.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
)

response = client.chat.completions.create(
    model="qwen-plus-character",
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: QWEN CONNECTION SUCCESS"
        }
    ],
    temperature=0.2
)

print(response.choices[0].message.content)