import requests
from dotenv import load_dotenv
load_dotenv()
import os

PIPE_URL = os.getenv("PIPEFY_URL", "https://api.pipefy.com/graphql")
PIPE_ID = os.getenv("PIPEFY_PIPE_ID", "303843596")
API_TOKEN = os.getenv("PIPEFY_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def execute_graphql(query: str, variables: dict):
    response = requests.post(PIPE_URL, json={"query": query, "variables": variables}, headers=HEADERS)
    response.raise_for_status()
    return response.json()