"""
main.py - Entry point for LLM-RAG Image Filter Project
"""

import sys
import json
import os
from langchain_openai import ChatOpenAI


def load_key(file_name: str):
    with open(file_name, "r") as file:
        config = json.load(file)
        os.environ["OPENAI_API_KEY"] = config.get("API_KEY")
        os.environ["OPENAI_BASE_URL"] = config.get("OPENAI_API_BASE")


def get_llm():
    llm = ChatOpenAI(
        model="gpt-4o-mini",  # "gpt-4o-mini" to be used as an LLM
        temperature=0,  # Set the temprature to 0
        max_tokens=5000,  # Set the max_tokens = 5000, so that the long response will not be clipped off
        top_p=0.95,
        frequency_penalty=1.2,
        stop_sequences=["INST"],
    )


def process_image(query: str, image_path: str) -> str:
    """Processes the image based on query intent."""
    print(f"[INFO] Received query: {query}")

    # Step 1: Interpret query

    # Step 2: Retrieve background info (via RAG mock)

    # Step 3: Apply the filter and return result
    return ""


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py '<query>' <image_path> <config_file_path>")
        sys.exit(1)

    query = sys.argv[1]
    image_path = sys.argv[2]
    load_key(sys.argv[3])
    llm = get_llm()
    process_image(query, image_path)
