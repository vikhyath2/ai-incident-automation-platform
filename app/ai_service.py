import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_incident(log_text: str):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": """
You are an AI Incident Automation Engineer.

Return ONLY valid JSON in this exact format:

{
  "issue_summary": "",
  "root_cause": "",
  "severity": "Low | Medium | High | Critical",
  "suggested_fix": "",
  "next_action": ""
}

Do not include markdown.
Do not include extra explanation.
"""
            },
            {
                "role": "user",
                "content": f"Analyze this log:\n{log_text}"
            }
        ]
    )

    ai_output = response.choices[0].message.content

    return json.loads(ai_output)