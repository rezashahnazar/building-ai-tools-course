from openai import OpenAI
from dotenv import dotenv_values
import json

config = dotenv_values(".env")

api_key = config["API_KEY"]
base_url = config["BASE_URL"]

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

def ysc_calculator(a, b):
    result = a + b + 5
    return result

messages = [
        {
            "role": "developer",
            "content": """You are a helpful assistant that only answers in English. 
            Never in any other language , even if the user asks you to do so.
            Young Scholars Club in our game is like a country with a capital city. 
            The capital is located at floor 2 , right next to the entrance.
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

# Start of Execution
print("Starting to send the first request to the API")
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    tools=tools,
)
print("First request sent to the API")

message = response.choices[0].message

print("The response of the first request is:")
print(message)

print("Checking if the response has tool calls")
if message.tool_calls:
    print("The response has tool calls")
    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        
        print(f"The function name is: {function_name}")
        print(f"The function arguments are: {function_args}")
        
        
        if function_name == "ysc_calculator":
            result = ysc_calculator(function_args["a"], function_args["b"])
            print(f"The result of the ysc_calculator function with function arguments {function_args} is: {result}")
            
            messages.append(message)
            print("Appending the tool call response message to the messages list. the resulted messages list is now:")
            print(messages)
            
            tool_message = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
            messages.append(tool_message)
            print("Appending the tool call result message to the messages list. the resulted messages list is now:")
            print(messages)
            
            print("Sending the second request to the API")
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
                tools=tools,
            )
            print("Second request sent to the API")
            
            response_text = response.choices[0].message.content
            
            print("The response of the second request is:")
            print(response_text)
else:
    print("The response does not have tool calls")
    response_text = message.content
    print("The response is:")
    print(response_text)



[
    {'role': 'developer', 'content': 'You are a helpful assistant that only answers in English. \n            Never in any other language , even if the user asks you to do so.\n            Young Scholars Club in our game is like a country with a capital city. \n            The capital is located at floor 2 , right next to the entrance.\n            '},
    {'role': 'user', 'content': 'In young scholars club, what is the sum of 2 and 3?'}, 
    ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=[ChatCompletionMessageFunctionToolCall(id='call_2q7AreLPaQ5L8Xa5c6J8bpen', function=Function(arguments='{"a":2,"b":3}', name='ysc_calculator'), type='function')]),
    {'role': 'tool', 'tool_call_id': 'call_2q7AreLPaQ5L8Xa5c6J8bpen', 'content': '10'}
]