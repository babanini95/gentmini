import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_KEY_API")
client = genai.Client(api_key=api_key)

messages = [types.Content(role="user", parts=[types.Part(text=sys.argv[1])])]


def main():
    if len(sys.argv) == 1:
        print("need argument")
        sys.exit(1)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print(response.text)
    if len(sys.argv) >= 3:
        if sys.argv[2] == "--verbose":
            print(
                f"User prompt: {sys.argv[1]}\n"
                f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
                f"Response tokens: {response.usage_metadata.candidates_token_count}"
            )


if __name__ == "__main__":
    main()
