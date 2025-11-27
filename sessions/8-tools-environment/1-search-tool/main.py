import json
import logging
from dotenv import dotenv_values
from exa_py import Exa
from openai import OpenAI

# ANSI color codes for beautiful terminal output
class Colors:
    # Basic colors
    BLUE = '\033[34m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    RED = '\033[31m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bright colors
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    BRIGHT_BLACK = '\033[90m'

    # Styles
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    # Text colors
    BLACK = '\033[30m'
    WHITE = '\033[37m'

    # Background colors
    BG_BLUE = '\033[44m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_RED = '\033[41m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'

logging.basicConfig(
    level=logging.WARNING,
    format='%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)

config = dotenv_values(".env")

openai_api_key = config["API_KEY"]
openai_base_url = config["BASE_URL"]
exa_api_key = config["EXA_API_KEY"]

openai_client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_base_url,
)

exa_client = Exa(api_key=exa_api_key)

def web_search(query, num_results=5):
    """
    Search the internet using EXA AI-powered search engine.
    Returns a list of search results with title, URL, and content preview.
    """
    print(f"{Colors.CYAN}🔍 Searching for: '{Colors.BRIGHT_CYAN}{query}{Colors.CYAN}'{Colors.RESET}")
    try:
        response = exa_client.search(
            query,
            num_results=num_results,
            contents={"text": True}
        )

        results = []
        for i, result in enumerate(response.results, 1):
            # Ensure we have valid data
            title = result.title or f"Untitled Result {i}"
            url = result.url or "No URL available"
            text = result.text or ""

            result_data = {
                "title": title,
                "url": url,
                "text": text[:500] if text else ""
            }
            results.append(result_data)

            # Pretty print each result with colors
            print(f"\n{Colors.BG_YELLOW}{Colors.BLACK}{Colors.BOLD} 📄 RESULT {i} {Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}")
            print(f"{Colors.BRIGHT_YELLOW}🏷️  TITLE:{Colors.RESET} {title}")
            print(f"{Colors.BLUE}🔗  SOURCE:{Colors.RESET} {url}")
            print(f"{Colors.GREEN}📖  CONTENT:{Colors.RESET}")

            if text:
                # Clean up and format the text content with higher limits
                preview = text.replace('\n\n', '\n').strip()

                # Split into paragraphs
                paragraphs = [p.strip() for p in preview.split('\n') if p.strip()]

                # Show first 8 paragraphs or limit to 1500 characters, whichever comes first
                display_paragraphs = paragraphs[:8]  # Increased from 3 to 8 paragraphs
                total_chars = 0
                truncated_paragraphs = []

                for para in display_paragraphs:
                    if total_chars + len(para) > 1500:  # Increased character limit
                        # Truncate this paragraph if it would exceed the limit
                        remaining_chars = 1500 - total_chars
                        if remaining_chars > 50:  # Only add if we have meaningful space
                            truncated_para = para[:remaining_chars].rstrip()
                            if len(para) > remaining_chars:
                                truncated_para += "..."
                            truncated_paragraphs.append(truncated_para)
                        break
                    truncated_paragraphs.append(para)
                    total_chars += len(para)

                # If we still have content after limits, add truncation indicator
                if len(paragraphs) > len(truncated_paragraphs) or total_chars >= 1500:
                    truncated_paragraphs.append("...")

                # Format each paragraph nicely
                for i, para in enumerate(truncated_paragraphs):
                    if para == "...":
                        print(f"   {Colors.GREEN}📖  {Colors.WHITE}{para}{Colors.RESET}")
                    else:
                        # Wrap long lines for better readability
                        wrapped = []
                        words = para.split()
                        line = ""
                        for word in words:
                            if len(line + word) < 80:  # Reasonable line length
                                line += word + " "
                            else:
                                wrapped.append(line.strip())
                                line = word + " "
                        if line.strip():
                            wrapped.append(line.strip())

                        for j, line in enumerate(wrapped):
                            if i == 0 and j == 0:  # First line of first paragraph
                                print(f"   {Colors.GREEN}📖  {Colors.RESET}{line}")
                            else:
                                print(f"      {Colors.RESET}{line}")

                print()  # Extra spacing after content

            print(f"{Colors.BRIGHT_BLACK}{'═' * 80}{Colors.RESET}")

        print(f"\n{Colors.BRIGHT_GREEN}✅ Found {len(results)} results total{Colors.RESET}")
        return results
    except Exception as e:
        print(f"{Colors.RED}❌ Search failed: {e}{Colors.RESET}")
        return []

messages = [  # Conversation setup with AI assistant instructions and user query
    {
        "role": "developer",
        "content": """You are a helpful web search assistant that can search the internet for information.
        When users ask questions, use the web_search tool to find relevant information from the web.
        Always answer in English and provide helpful, accurate information based on search results.
        """,
    },
    {
        "role": "user",
        "content": "What is the latest Campbell Biology edition?",
    }
    ]

tools = [  # Define available tools that the AI can use
        {
            "type": "function",
            "function": {
                "name": "web_search",
                "description": "Search the internet for information using AI-powered web search.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query to look up on the internet"
                        },
                        "num_results": {
                            "type": "integer",
                            "description": "Number of search results to return (default: 5)",
                            "default": 5
                        }
                    },
                    "required": ["query"]
                }
            }
        }
    ]

print(f"{Colors.BRIGHT_BLUE}🤖 AI Web Search Agent starting...{Colors.RESET}")
print(f"{Colors.YELLOW}💬 User asked: {Colors.BRIGHT_YELLOW}{messages[1]['content']}{Colors.RESET}")

response = openai_client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
)

message = response.choices[0].message

if message.tool_calls:
    print(f"{Colors.MAGENTA}🔧 AI is using web search tool...{Colors.RESET}")

    for tool_call in message.tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)

        if function_name == "web_search":
            query = function_args["query"]
            num_results = function_args.get("num_results", 5)
            result = web_search(query, num_results)

            messages.append(message)
            tool_message = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            }
            messages.append(tool_message)

            print(f"{Colors.BLUE}🧠 AI is analyzing search results...{Colors.RESET}")

            response = openai_client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages,
                tools=tools,
            )

            response_text = response.choices[0].message.content
            print(f"\n{Colors.BG_CYAN}{Colors.WHITE}{'='*50}{Colors.RESET}")
            print(f"{Colors.BG_CYAN}{Colors.WHITE}{Colors.BOLD}📝 ANSWER:{Colors.RESET}")
            print(f"{Colors.BG_CYAN}{Colors.WHITE}{'='*50}{Colors.RESET}")
            print(f"{Colors.BRIGHT_WHITE}{response_text}{Colors.RESET}")
else:
    response_text = message.content
    print(f"\n{Colors.BG_CYAN}{Colors.WHITE}{'='*50}{Colors.RESET}")
    print(f"{Colors.BG_CYAN}{Colors.WHITE}{Colors.BOLD}📝 ANSWER:{Colors.RESET}")
    print(f"{Colors.BG_CYAN}{Colors.WHITE}{'='*50}{Colors.RESET}")
    print(f"{Colors.BRIGHT_WHITE}{response_text}{Colors.RESET}")

