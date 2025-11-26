from openai import OpenAI
from dotenv import dotenv_values
import json
from pprint import pprint
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

config = dotenv_values(".env")

api_key = config["API_KEY"]
base_url = config["BASE_URL"]

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

def ysc_calculator(a, b):
    logger.info(f"Executing ysc_calculator with a={a}, b={b}")
    result = a + b + 5
    logger.info(f"ysc_calculator result: {result} (calculated as {a} + {b} + 5)")
    return result

messages = [
    {
        "role": "developer",
        "content": """You are a helpful assistant that only answers in English. 
        Never in any other language , even if the user asks you to do so.
        Young Scholars Club in our game is like a country with a capital city. The capital is located at floor 2 , right next to the entrance.
        """,
    },
    {
        "role": "user",
        "content": "In young scholars club, what is the sum of 2 and 3?",
    }
    ]

tools = [
        {
            "type": "function",
            "function": {
                "name": "ysc_calculator",
                "description": "Adds two numbers together in Young Scholars Club way.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "number",
                            "description": "The first number to add"
                        },
                        "b": {
                            "type": "number",
                            "description": "The second number to add"
                        }
                    },
                    "required": ["a", "b"]
                }
            }
        }
    ]

logger.info("Making initial API call with messages and tools")
logger.info(f"Messages: {json.dumps(messages, indent=2)}")
logger.info(f"Tools available: {[tool['function']['name'] for tool in tools]}")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    tools=tools,
)

logger.info("API response received")
message = response.choices[0].message

if message.tool_calls:
    logger.info(f"Tool calls detected: {len(message.tool_calls)} tool call(s)")
    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        
        logger.info(f"Processing tool call: {function_name}")
        logger.info(f"Tool call arguments: {function_args}")
        
        if function_name == "ysc_calculator":
            result = ysc_calculator(function_args["a"], function_args["b"])
            
            logger.info("Appending assistant message and tool result to conversation")
            messages.append(message)
            tool_message = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
            messages.append(tool_message)
            logger.info(f"Tool message added: {tool_message}")
            
            logger.info("Making follow-up API call with tool result")
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
                tools=tools,
            )
            
            logger.info("Follow-up API response received")
            response_text = response.choices[0].message.content
            logger.info(f"Final response: {response_text}")
            print(response_text)
else:
    logger.info("No tool calls detected, using direct response")
    response_text = message.content
    logger.info(f"Response: {response_text}")
    print(response_text)

