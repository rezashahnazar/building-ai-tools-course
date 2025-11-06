# Chat Completions API

This project demonstrates how to interact with AI language models using the Chat Completions API. You'll learn how to send requests to an AI service and receive structured JSON responses.

## Overview

The Chat Completions API is a RESTful API that allows you to send conversational messages to an AI model and receive text responses. This is the foundation of how modern AI applications like ChatGPT work behind the scenes.

## Prerequisites

- Python 3.14 or higher
- An API key for your AI service provider
- Basic understanding of JSON and APIs (see `../0-json-and-apis/README.md`)

## Setup

### 1. Install Dependencies

This project uses `uv` for dependency management. Install dependencies with:

```bash
uv sync
```

Or if you prefer pip:

```bash
pip install openai python-dotenv
```

### 2. Configure Environment Variables

Copy the example environment file:

```bash
cp env.example .env
```

Edit `.env` and add your credentials:

```
API_KEY=your_api_key_here
BASE_URL=https://api.openai.com/v1
```

**Important**: Never commit your `.env` file to version control. It contains sensitive credentials.

## Running the Project

Execute the main script:

```bash
python main.py
```

Or with uv:

```bash
uv run python main.py
```

## Understanding the Code

Let's break down what happens in `main.py`:

### 1. Loading Configuration

```python
from dotenv import dotenv_values

config = dotenv_values(".env")
api_key = config["API_KEY"]
base_url = config["BASE_URL"]
```

This loads your API credentials from the `.env` file. Environment variables keep sensitive information out of your code.

### 2. Creating the Client

```python
from openai import OpenAI

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)
```

The `OpenAI` client is initialized with your credentials. The `base_url` determines which API endpoint to use.

### 3. Making a Chat Completion Request

```python
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "developer",
            "content": "You are a helpful assistant that only answers in Persian..."
        },
        {
            "role": "user",
            "content": "What is the capital of France?"
        },
    ]
)
```

This sends a POST request to the Chat Completions API with:

- **model**: The AI model to use (e.g., `gpt-4.1-mini`)
- **messages**: An array of message objects representing the conversation

### 4. Understanding Message Roles

Each message has a `role` that defines its purpose:

- **developer/system**: Instructions for the AI's behavior and personality
- **user**: Questions or requests from the user
- **assistant**: Previous responses from the AI (for conversation history)

### 5. Extracting the Response

```python
response_text = response.choices[0].message.content
print(response_text)
```

The API returns a JSON response with this structure:

```json
{
  "id": "chatcmpl-...",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "gpt-4.1-mini",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The response text here"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 20,
    "total_tokens": 30
  }
}
```

We access `choices[0].message.content` to get the actual text response.

## Key Concepts

### API Request Structure

When you call `client.chat.completions.create()`, the library sends an HTTP POST request like this:

```
POST /v1/chat/completions
Headers:
  Authorization: Bearer YOUR_API_KEY
  Content-Type: application/json

Body (JSON):
{
  "model": "gpt-4.1-mini",
  "messages": [
    {"role": "developer", "content": "..."},
    {"role": "user", "content": "..."}
  ]
}
```

### API Response Structure

The API returns JSON with:

- **id**: Unique identifier for this completion
- **choices**: Array of possible responses (usually one)
- **usage**: Token usage statistics
- **model**: The model that generated the response

### Message Array

The `messages` array represents the conversation history:

- Messages are processed in order
- The AI uses previous messages as context
- You can build multi-turn conversations by including previous exchanges

### Developer/System Role

The `developer` role (or `system` in some APIs) sets the AI's behavior:

- Defines personality and constraints
- Sets response format preferences
- Provides context about the task

## Working with JSON Data

This project includes `olympiad.json` as an example of structured JSON data. You can:

1. Load JSON files in Python:

```python
import json

with open('olympiad.json', 'r') as f:
    data = json.load(f)
```

2. Send JSON data to the AI:

```python
messages.append({
    "role": "user",
    "content": f"Analyze this data: {json.dumps(data)}"
})
```

3. Request structured JSON responses:

```python
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    response_format={"type": "json_object"}
)
```

## Common Use Cases

- **Question Answering**: Ask questions and get answers
- **Text Generation**: Create content, stories, or summaries
- **Translation**: Convert text between languages
- **Code Generation**: Write code based on descriptions
- **Data Analysis**: Analyze JSON data and extract insights
- **Conversational Agents**: Build chatbots and virtual assistants

## Error Handling

The API can return errors. Common issues:

- **401 Unauthorized**: Invalid or missing API key
- **429 Too Many Requests**: Rate limit exceeded
- **400 Bad Request**: Invalid request format
- **500 Internal Server Error**: Service temporarily unavailable

Always handle potential errors in production code.

## Next Steps

- Experiment with different models
- Try multi-turn conversations by including assistant messages
- Use the `olympiad.json` file to practice sending structured data
- Explore response formatting options
- Learn about streaming responses for real-time interactions

## Resources

- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference/chat)
- [JSON and APIs Guide](../0-json-and-apis/README.md)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
