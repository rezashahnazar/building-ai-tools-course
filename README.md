# AI Agent Tutorial

A comprehensive educational project designed for **non-technical professionals** who want to understand and build AI agents. This course makes AI accessible to everyone, from fundamentals to advanced implementations, with practical applications for your work and life.

## Overview

This tutorial series guides you through the complete journey of understanding and building AI agents. Each session builds upon previous concepts, providing both theoretical understanding and practical implementation. The course is specifically designed for professionals in various fields who want to leverage AI in their work, even without a technical background.

**Who This Course Is For:**

- Healthcare workers looking to summarize patient notes
- Marketing teams wanting to generate content at scale
- Educators creating personalized learning experiences
- Business analysts needing to extract insights from data
- Anyone curious about AI and its practical applications

## Project Structure

The project is organized into numbered sessions, each focusing on a specific topic:

```
sessions/
├── 0-intro/                          # Introduction to AI agents
├── 1-next-token-prediction/          # Understanding language model fundamentals
├── 2-chat-completions/               # Chat completion APIs
├── 3-embeddings/                     # Vector embeddings and semantic search
├── 4-transformers/                   # Transformer architecture
├── 5-rag/                            # Retrieval-Augmented Generation
├── 6-json-api-completions/           # JSON and API interactions
├── 7-responses-messages-genai/       # Response handling and message management
├── 8-tools-environment/              # Tools and environment integration
├── 9-workflows-agents/               # Agent workflows
├── 10-search-api-multimodal-rag-agent/  # Multimodal RAG with search APIs
├── 11-database-safeguards-local-agents/ # Database integration and safeguards
├── 12-semantic-rag-agents/           # Semantic RAG implementations
├── 13-context-mcp-subagents/         # Context management and sub-agents
└── 14-scheduled-agents/              # Scheduled and automated agents
```

## Getting Started

### Prerequisites

- Python 3.14 or higher
- Basic understanding of Python programming
- Familiarity with command-line interfaces
- (Optional) Understanding of machine learning concepts

### Installation

Each session may have its own dependencies. Navigate to the specific session directory and follow its setup instructions.

For sessions using `uv` (Python package manager):

```bash
cd sessions/<session-name>/
uv sync
```

For sessions using `pip`:

```bash
cd sessions/<session-name>/
pip install -r requirements.txt
```

### Environment Setup

Many sessions require API keys or configuration. Look for `env.example` files in session directories and create your own `.env` file:

```bash
cp env.example .env
# Edit .env with your credentials
```

## Learning Path

### Foundation (Sessions 0-3)

Start here to understand the basics of AI and how language models work.

#### [Session 0: Introduction to AI and LLMs](sessions/0-intro/)

**Status:** Complete

Learn the fundamental concepts and practical considerations for working with AI:

- What are Large Language Models (LLMs) and how do they work?
- Cloud vs. local models: privacy and deployment options
- Personalization, bias, and ethical considerations
- Practical applications: content classification, rewriting, editing
- Safeguards, prompt optimization, and evaluation methods
- Real-world use cases across professions

**Key Takeaways:** Understanding AI capabilities, limitations, privacy considerations, and responsible usage.

#### [Session 1: Next Token Prediction](sessions/1-next-token-prediction/)

**Status:** Complete

Understand the fundamental mechanism behind AI text generation:

- How AI predicts text one token at a time
- The role of training data in prediction quality
- Context windows and why they matter
- Temperature and creativity controls
- Why AI sometimes "hallucinates"
- How to write better prompts based on prediction mechanics

**Key Takeaways:** The core mechanism of language models, how to optimize prompts, understanding AI limitations.

#### [Session 2: Chat Completions](sessions/2-chat-completions/)

**Status:** Complete

Learn how conversations with AI work and how to control AI behavior:

- Architecture of chat completion systems
- Message roles: system, user, and assistant
- System prompt engineering for specific behaviors
- Multi-turn conversations and context management
- Parameters that control AI responses (temperature, tokens, etc.)
- Building conversational applications

**Key Takeaways:** Structuring effective conversations, controlling AI personality, building chat applications.

#### [Session 3: Embeddings](sessions/3-embeddings/)

**Status:** Complete

Discover how AI understands meaning and relationships:

- Converting text to meaningful numbers (vectors)
- Static vs. contextual embeddings
- Semantic similarity and vector space
- Building semantic search systems
- Document clustering and recommendations
- Practical applications across domains

**Key Takeaways:** Understanding semantic similarity, building search systems, finding related content.

### Intermediate (Sessions 4-6)

Dive deeper into AI architecture and practical implementations.

#### [Session 4: Transformers](sessions/4-transformers/)

**Status:** Complete

Understand the architecture powering modern AI:

- The three core components: positional encoding, self-attention, feed-forward networks
- How self-attention helps AI understand relationships between words
- Why positional encoding matters for word order
- Multi-head attention and parallel processing
- How transformers process entire sentences simultaneously
- Connection to GPT, BERT, and other models

**Key Takeaways:** The architecture behind modern AI, why transformers are so powerful, how attention mechanisms work.

#### [Session 5: RAG and Agents](sessions/5-rag/)

**Status:** Complete

Extend AI with external knowledge and actions:

- **RAG (Retrieval-Augmented Generation):** Giving AI access to your documents
- Six-step RAG process: from question to answer
- Building semantic search for your knowledge base
- **Agents:** AI that takes actions beyond just responding
- Agent architecture: state, actions, environment, side effects
- Combining RAG with agents for powerful applications

**Key Takeaways:** Building knowledge-based AI systems, creating agents that take actions, combining retrieval with generation.

#### [Session 6: JSON and APIs](sessions/6-json-api-completions/)

**Status:** Complete

Master data exchange and API integration:

- **Part 1:** [Understanding JSON and APIs](sessions/6-json-api-completions/0-json-and-apis/)
  - JSON structure and why it's essential
  - HTTP methods: GET, POST, PUT, PATCH, DELETE
  - API architecture and data flow
  - Using JSONPlaceholder for hands-on practice
- **Part 2:** [Chat Completions API](sessions/6-json-api-completions/1-chat-completions-api/)
  - Connecting to AI services via API
  - Request/response structure
  - Environment configuration and security
  - Building your first AI application

**Key Takeaways:** Working with APIs, integrating AI services, handling JSON data, building practical applications.

### Advanced (Sessions 7-9)

_Coming Soon_ - Advanced patterns for production applications.

- **Session 7**: Responses, messages, and GenAI patterns
- **Session 8**: Tools and environment - extending agent capabilities
- **Session 9**: Workflows and agents - orchestrating complex tasks

### Production (Sessions 10-14)

_Coming Soon_ - Building production-ready AI systems.

- **Session 10**: Multimodal RAG with search APIs
- **Session 11**: Database safeguards and local agents
- **Session 12**: Semantic RAG agents
- **Session 13**: Context management and sub-agents
- **Session 14**: Scheduled and automated agents

## What You'll Build

By the end of this course, you'll be able to:

- **Understand AI fundamentals** and make informed decisions about AI tools
- **Write effective prompts** that get better results from AI
- **Build semantic search systems** for your documents and knowledge bases
- **Create RAG applications** that answer questions using your company's data
- **Develop AI agents** that take actions beyond simple conversations
- **Integrate AI services** into your workflows via APIs
- **Design chatbots** with specific personalities and capabilities
- **Implement safety measures** for responsible AI usage
- **Build production systems** (upcoming sessions)
- **Create multi-agent workflows** (upcoming sessions)

## Key Concepts Covered

**Completed Sessions:**

- **Language Models**: How AI generates text token by token
- **Chat Completions**: Structuring conversations and controlling AI behavior
- **Vector Embeddings**: Semantic search and similarity
- **Transformers**: The architecture powering modern AI
- **RAG Systems**: Combining retrieval with generation
- **Agent Architecture**: Building autonomous AI systems
- **API Integration**: Working with AI service APIs
- **JSON & Data**: Understanding data exchange formats

**Upcoming Sessions:**

- **Tool Integration**: Extending agents with external capabilities
- **Workflow Orchestration**: Managing complex multi-step processes
- **Production Patterns**: Safeguards, monitoring, and best practices
- **Database Integration**: Working with persistent data
- **Multimodal AI**: Beyond text - images, audio, and more

## Quick Start

1. **Start with Session 0** if you're new to AI
2. **Follow sessions in order** - each builds on previous concepts
3. **Do the hands-on exercises** in each session
4. **Join discussions** - use the discussion questions to deepen understanding
5. **Build something** - apply concepts to your own use case

### Recommended Path by Profession

**Legal Professionals:**

- Sessions 0-3 (foundations)
- Session 5 (RAG for document search)
- Session 6 (API integration)

**Marketing & Content:**

- Sessions 0-2 (LLMs and chat)
- Session 3 (embeddings for content recommendations)
- Session 6 (API integration)

**Researchers & Analysts:**

- Sessions 0-3 (foundations)
- Session 5 (RAG for research papers)
- Sessions 3 & 5 (semantic search and clustering)

**Everyone:**

- All sessions provide valuable understanding of AI!

## Progress Tracking

Track your learning progress:

- [ ] Session 0: AI Introduction
- [ ] Session 1: Next Token Prediction
- [ ] Session 2: Chat Completions
- [ ] Session 3: Embeddings
- [ ] Session 4: Transformers
- [ ] Session 5: RAG and Agents
- [ ] Session 6: JSON and APIs

## Contributing

This is an educational project. Contributions, improvements, and suggestions are welcome:

- Report issues or suggest improvements
- Share your use cases and examples
- Contribute session materials
- Help make AI more accessible to everyone

## Additional Resources

### Official Documentation

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude Documentation](https://docs.anthropic.com/)
- [Python Documentation](https://docs.python.org/3/)
- [JSON Specification](https://www.json.org/)

### Learning Resources

- [The Illustrated Transformer](http://jalammar.github.io/illustrated-transformer/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain Documentation](https://python.langchain.com/)
- [Understanding Word2Vec](https://jalammar.github.io/illustrated-word2vec/)

## License

MIT

## Author

Reza Shahnazar

- GitHub: [rezashahnazar](https://github.com/rezashahnazar)
- Email: reza.shahnazar@gmail.com

## Course Status

**Completed:** Sessions 0-6 (Foundations and Intermediate)

- Comprehensive tutorials with examples
- Hands-on exercises
- Discussion questions
- Real-world applications

**In Development:** Sessions 7-14 (Advanced and Production)

- Coming soon based on demand and feedback

**Last Updated:** November 2025

## Getting Help

- **Questions?** Open an issue in this repository
- **Discussion:** Use GitHub Discussions for course-related questions
- **Feedback:** Contributions and suggestions are welcome

## Acknowledgments

This course is designed to make AI accessible to everyone, regardless of technical background. Special thanks to all learners who provide feedback to improve the material.
