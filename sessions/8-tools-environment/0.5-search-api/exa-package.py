from exa_py import Exa
from dotenv import dotenv_values

config = dotenv_values(".env")

EXA_API_KEY = config.get("EXA_API_KEY")

exa_client = Exa(EXA_API_KEY)

results = exa_client.search_and_contents(
    "Iran Biology Olympiad", 
    text=True
)

print(results)