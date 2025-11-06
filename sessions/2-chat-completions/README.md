# Session 2: Chat Completions - Conversing with AI

Building on our understanding of next-token prediction, this session explores how AI systems handle conversations and how you can interact with them programmatically through Chat Completion APIs.

## What You'll Learn

- How chat conversations work with AI
- The structure of chat completion requests
- Different message roles and their purposes
- How to control AI behavior through system prompts
- The complete flow from question to answer

## From Prediction to Conversation

In Session 1, we learned that AI predicts one token at a time. But how does that become a natural conversation?

**The Magic**: Each message in a conversation becomes context for predicting the next response.

**Example Conversation:**

```
You: "What's the weather like?"
AI: "I don't have access to real-time weather data, but I can help
     you understand how to check it."
You: "How do I check it?"
AI: [Predicts response based on BOTH previous messages]
```

The AI sees the entire conversation history and uses it to predict relevant next tokens.

## Chat Completion Architecture

Based on the flow diagram, here's how a complete chat system works:

### The Complete Flow

```
1. User Input
   ↓
2. Message History (context)
   ↓
3. System Instructions (personality/behavior)
   ↓
4. API Request → LLM (Language Model)
   ↓
5. Token Generation (next-token prediction)
   ↓
6. Response Assembly
   ↓
7. Return to User
   ↓
8. Update Message History
```

### Component Breakdown

**1. User Input**

- Your question or request
- Gets added to the conversation

**2. Message History**

- Previous messages in the conversation
- Provides context for the AI
- Helps maintain coherence

**3. System Instructions**

- Defines AI personality and behavior
- Sets constraints and guidelines
- Establishes response format

**4. API Request**

- Packages everything together
- Sends to the language model
- Includes model selection and parameters

**5. Token Generation**

- AI predicts tokens one by one
- Uses conversation context
- Applies system instructions

**6. Response Assembly**

- Tokens combined into complete response
- Formatted appropriately
- Ready for delivery

**7. Return to User**

- Complete response displayed
- May include metadata (tokens used, etc.)

**8. Update History**

- New exchange added to conversation
- Becomes context for next interaction

## Message Roles

Chat completions use three main message roles:

### 1. System/Developer Role

**Purpose**: Set AI behavior and personality

**Example:**

```json
{
  "role": "system",
  "content": "You are a helpful legal assistant. Provide accurate
             information about law, but always remind users to
             consult a licensed attorney for legal advice."
}
```

**Use Cases:**

- Define expertise area
- Set tone and style
- Establish constraints
- Provide background context

**Best Practices:**

- Be specific about desired behavior
- Include what NOT to do
- Set output format preferences
- Define scope boundaries

### 2. User Role

**Purpose**: Represent the human's messages

**Example:**

```json
{
  "role": "user",
  "content": "Can I break a lease if my landlord won't fix the heat?"
}
```

**Characteristics:**

- Questions or requests
- Follow-up queries
- Additional context
- Feedback or corrections

### 3. Assistant Role

**Purpose**: Represent AI's previous responses

**Example:**

```json
{
  "role": "assistant",
  "content": "Lease termination laws vary by jurisdiction. In many
             places, landlords must provide habitable conditions,
             including heat. However, you should consult a local
             attorney for specific advice..."
}
```

**Why Include Previous Responses?**

- Maintains conversation context
- Ensures consistency
- Enables multi-turn discussions
- Allows references to earlier points

## Building Effective Conversations

### Single-Turn Completion

Simplest form: One question, one answer

```
Messages:
[
  {
    "role": "system",
    "content": "You are a concise assistant."
  },
  {
    "role": "user",
    "content": "What is Python?"
  }
]

Response:
"Python is a high-level programming language known for
its readability and versatility..."
```

### Multi-Turn Conversation

More natural dialogue with history:

```
Messages:
[
  {
    "role": "system",
    "content": "You are a helpful programming tutor."
  },
  {
    "role": "user",
    "content": "What is Python?"
  },
  {
    "role": "assistant",
    "content": "Python is a high-level programming language..."
  },
  {
    "role": "user",
    "content": "Is it good for beginners?"
  },
  {
    "role": "assistant",
    "content": "Yes! Python is excellent for beginners because..."
  },
  {
    "role": "user",
    "content": "How do I get started?"
  }
]

Response:
"To start with Python, I recommend: 1) Install Python from
python.org, 2) Try an interactive tutorial..."
```

Notice how later questions ("Is it good for beginners?") make sense because of the conversation history.

## System Prompt Engineering

The system message is your most powerful tool for controlling AI behavior.

### Basic System Prompts

**General Assistant:**

```
"You are a helpful, respectful, and honest assistant."
```

**Specialized Expert:**

```
"You are an experienced financial advisor. Provide practical
advice about personal finance, budgeting, and investing.
Always remind users that this is educational information,
not personalized financial advice."
```

**Stylistic Constraints:**

```
"You are a concise technical writer. Use simple language,
short sentences, and bullet points. Avoid jargon unless
necessary. Maximum 3 paragraphs per response."
```

### Advanced System Prompts

**With Output Format:**

```
"You are a research assistant. When answering questions:
1. Start with a brief summary (2-3 sentences)
2. Provide detailed explanation
3. List 3 key takeaways
4. Suggest related topics

Always cite sources when possible."
```

**With Safety Constraints:**

```
"You are a medical information assistant. Provide general
health information from reputable sources. NEVER diagnose
conditions or prescribe treatments. Always recommend
consulting healthcare professionals for medical concerns."
```

**Personality and Tone:**

```
"You are an encouraging career coach. Be supportive and
positive, but also realistic. Help users identify their
strengths and opportunities. Use motivating language while
acknowledging challenges."
```

## Parameters That Control Behavior

Beyond the messages themselves, several parameters affect output:

### Temperature (0.0 - 2.0)

**0.0 - 0.3: Deterministic**

- Same input → same output
- Focused and predictable
- Best for: Factual answers, code, structured data

**0.7 - 1.0: Balanced**

- Varied but sensible responses
- Default setting
- Best for: General conversation, content creation

**1.5 - 2.0: Creative**

- Surprising and diverse outputs
- May be less coherent
- Best for: Brainstorming, creative writing, ideation

### Max Tokens

Limits response length

- Shorter: Concise answers, lower cost
- Longer: Detailed responses, complete answers

### Top P (Nucleus Sampling)

Alternative to temperature

- Controls diversity of word choice
- 0.1: Very focused, only top choices
- 1.0: Consider all possibilities

### Frequency Penalty

Reduces repetition

- 0.0: No penalty
- 2.0: Strongly avoid repeating tokens

### Presence Penalty

Encourages new topics

- 0.0: No penalty
- 2.0: Strongly favor new tokens

## Practical Applications

### Customer Service Bot

**System Prompt:**

```
"You are a customer service representative for an online bookstore.
Be friendly, helpful, and patient. You can help with:
- Order status
- Returns and refunds
- Product recommendations
- Account issues

For billing problems, escalate to a human agent."
```

**Conversation:**

```
User: "I haven't received my order yet"
AI: "I'm sorry to hear that! I'd be happy to help check on your
     order. Could you provide your order number?"

User: "ORDER12345"
AI: "Thank you! I'm looking that up... Your order shipped on the
     15th via standard delivery (5-7 business days). Based on the
     tracking, it should arrive by the 22nd. Would you like the
     tracking number?"
```

### Content Drafting Assistant

**System Prompt:**

```
"You are a marketing content writer. Create engaging, professional
content optimized for social media and blogs. Use active voice,
compelling headlines, and clear calls-to-action."
```

**Single Request:**

```
User: "Write a LinkedIn post about the importance of work-life balance"
AI: [Generates complete post with hook, body, and CTA]
```

### Research Helper

**System Prompt:**

```
"You are a research assistant helping with academic work.
Provide accurate, well-sourced information. Explain complex
concepts clearly. Admit when you're uncertain."
```

**Multi-Turn Research:**

```
User: "What is machine learning?"
AI: [Explains basics]

User: "How does it differ from traditional programming?"
AI: [Explains difference, references previous explanation]

User: "Give me an example from healthcare"
AI: [Provides healthcare example, connecting to earlier points]
```

## Best Practices

### 1. Clear System Instructions

Good:

```
"You are a Python tutor. Explain concepts with code examples.
For each concept: 1) Define it simply, 2) Show an example,
3) Explain common mistakes."
```

Poor:

```
"Help with Python."
```

### 2. Maintain Conversation Context

Include relevant message history, but:

- Trim very old messages to save tokens
- Keep essential context
- Summarize long conversations

### 3. Error Handling

Plan for:

- API failures
- Incomplete responses
- Unexpected output formats
- Rate limits

### 4. User Privacy

- Don't log sensitive information
- Sanitize inputs before sending
- Follow data protection regulations
- Provide opt-out options

### 5. Cost Management

- Set token limits
- Monitor usage
- Use caching when possible
- Choose appropriate models

## Understanding the Response

A typical API response includes:

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1699123456,
  "model": "gpt-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The response text..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 50,
    "total_tokens": 70
  }
}
```

**Key Fields:**

- **message.content**: The actual response text
- **finish_reason**: Why generation stopped (stop/length/etc.)
- **usage**: Token counts (for billing and monitoring)

## Common Patterns

### Few-Shot Learning

Teach by example in the system prompt:

```
"You are a sentiment classifier. Examples:

Input: 'This product is amazing!'
Output: Positive

Input: 'Terrible experience, would not recommend'
Output: Negative

Input: 'It's okay, nothing special'
Output: Neutral

Now classify new inputs in the same format."
```

### Chain of Thought

Ask AI to show its reasoning:

```
User: "Solve this math problem, showing your work step by step"
AI: "Let me break this down:
     Step 1: ...
     Step 2: ...
     Therefore: ..."
```

### Iterative Refinement

Use conversation to improve output:

```
User: "Write a product description"
AI: [First draft]

User: "Make it more exciting and add benefits"
AI: [Revised version]

User: "Shorten to 50 words"
AI: [Final version]
```

## Key Takeaways

1. **Chat completions transform token prediction** into natural conversations
2. **Three message roles** (system, user, assistant) structure interactions
3. **System prompts are powerful** - use them to control behavior precisely
4. **Conversation history** provides context for coherent multi-turn dialogue
5. **Parameters like temperature** fine-tune response creativity
6. **Include relevant examples** for better performance
7. **Plan for costs and errors** in production applications
8. **Privacy and safety** must be built into the system

## Hands-On Exercise

Try building these conversation flows:

**Exercise 1: Personal Assistant**
Create a system prompt for an assistant that:

- Helps organize tasks
- Uses encouraging language
- Provides practical advice
- Never gives financial or medical advice

**Exercise 2: Multi-Turn Dialogue**
Have a conversation where:

- First message asks a general question
- Second message asks for clarification
- Third message requests an example
- Notice how context builds

**Exercise 3: Style Comparison**
Same question with different system prompts:

- Formal academic style
- Casual friendly style
- Concise bullet-point style
- Compare the outputs

## Connection to Next Session

Now you understand how to converse with AI. In Session 3, we'll explore **Embeddings** - how AI understands the meaning and relationships between words and concepts, enabling powerful features like semantic search and recommendations.

## Resources

- [OpenAI Chat Completion API](https://platform.openai.com/docs/api-reference/chat)
- [Anthropic Claude API](https://docs.anthropic.com/claude/reference/messages)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## Discussion Questions

1. How would you design a system prompt for a use case in your field?
2. What conversation patterns would be most useful for your work?
3. How might you handle sensitive information in chat applications?
4. What temperature settings would suit different tasks in your domain?
