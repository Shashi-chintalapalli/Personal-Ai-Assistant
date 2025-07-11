import os
import cohere
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Initialize Cohere client
co = cohere.Client("CV9oorwaFIT3iKABnIVn7C0m6YXqfsBXL4RJoW8i")

def get_gpt_reply(prompt: str) -> str:
    """
    Generate a response using Cohere's language model.
    """
    try:
        response = co.generate(
            model="command",  # Options: command, command-nightly, etc.
            prompt=prompt,
            max_tokens=100,
            temperature=0.7,
            stop_sequences=["--"]
        )
        # Access the first generation's text safely
        return response.generations[0].text.strip()
    except Exception as e:
        print("❌ Error during Cohere API call:", e)
        return "I'm sorry, I couldn't process that request right now."
