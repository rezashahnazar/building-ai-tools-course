from dotenv import dotenv_values
import requests
from pprint import pprint

config = dotenv_values(".env")

EXA_API_KEY = config.get("EXA_API_KEY")


exa_api_url = "https://api.exa.ai/search"
headers = {
    "x-api-key": f"{EXA_API_KEY}",
    "Content-Type": "application/json",
}
body = {
    "query": "Reza Shahnazar",
    "category" : "people",
    "numResults": 10,
    "includeDomains" : ["linkedin.com"]
}

response = requests.post(exa_api_url, headers=headers, json=body)

pprint(response.json())