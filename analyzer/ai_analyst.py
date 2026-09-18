import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("QWEN_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://ws-59mgowi0mha0m6y5.ap-southeast-1.maas.aliyuncs.com/compatible-mode/v1"
)


def analyze_alert(alert):
    """
    Analyze a security alert using Qwen AI
    and retrieved security knowledge.
    """

    security_knowledge = alert.get("security_knowledge", [])

    knowledge_text = ""

    for item in security_knowledge:
        knowledge_text += f"""
Knowledge Source: {item['file']}
Relevance Score: {item['score']}

{item['content']}

--------------------------------
"""

    prompt = f"""
You are an expert Cybersecurity SOC Analyst.

Analyze the following security alert.

SECURITY ALERT:
{alert}

RETRIEVED SECURITY KNOWLEDGE:
{knowledge_text}

Use the retrieved security knowledge as guidance for your analysis.

IMPORTANT:
- Treat the security alert as the actual observed evidence.
- Treat retrieved knowledge as reference material, not proof.
- Do not invent facts that are not present in the alert.
- Clearly distinguish confirmed evidence from assumptions.
- Do not claim an attack was successful unless the evidence supports it.

Provide:

1. Attack Type
2. Severity
3. Risk Assessment
4. Why This Is Suspicious
5. Possible Attacker Objective
6. Investigation Steps
7. Recommended Defensive Action

Keep the response practical and concise.
"""

    response = client.chat.completions.create(
        model="qwen-plus-character",
        messages=[
            {
                "role": "system",
                "content": "You are a professional cybersecurity SOC analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content