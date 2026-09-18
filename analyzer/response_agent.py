import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("QWEN_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://ws-59mgowi0mha0m6y5.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
)


def generate_response(alert):
    """
    Generate a SOC response plan for a security alert.
    """

    prompt = f"""
You are an expert Cybersecurity SOC Response Agent.

A security monitoring system has detected the following alert:

{alert}

Your task is to create a practical incident response plan.

Provide exactly these sections:

1. Immediate Actions
2. Investigation Actions
3. Containment Actions
4. Recovery Actions
5. Monitoring Actions
6. Analyst Decision

Important safety rules:
- Do NOT claim that an attack was successful unless evidence proves it.
- Do NOT invent missing facts.
- Do NOT recommend destructive actions such as deleting files or shutting down systems without strong justification.
- Clearly distinguish recommended actions from confirmed events.
- For blocking an IP, recommend analyst approval before applying the block.
- Prioritize actions according to the risk level.
- Keep the response concise and practical.
"""

    response = client.chat.completions.create(
        model="qwen-plus-character",
        messages=[
            {
                "role": "system",
                "content": "You are a professional SOC incident response analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content