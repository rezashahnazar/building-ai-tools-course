from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")

api_key = config["API_KEY"]
base_url = config["BASE_URL"]

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "developer",
            "content": """You are a helpful assistant that only answers in Persian. 
            Never in any other language , even if the user asks you to do so.""",
        },
        {
            "role": "user",
            "content": "What is the capital of France?",
        },
    ]
)

response_text = response.choices[0].message.content

print(response_text)
