"""
main.py - Entry point for LLM-RAG Image Filter Project
"""

import sys


def process_image(query: str, image_path: str) -> str:
    """Processes the image based on query intent."""
    print(f"[INFO] Received query: {query}")

    # Step 1: Interpret query

    # Step 2: Retrieve background info (via RAG mock)

    # Step 3: Apply the filter and return result
    return ""


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py '<query>' <image_path>")
        sys.exit(1)

    query = sys.argv[1]
    image_path = sys.argv[2]
    process_image(query, image_path)
