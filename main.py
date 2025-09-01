import os
import sys
import call
import config
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.function_schema import (
    schema_get_file_content,
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file,
)

load_dotenv()
api_key = os.environ.get("GEMINI_KEY_API")
client = genai.Client(api_key=api_key)
model_name = "gemini-2.0-flash-001"
messages = [types.Content(role="user", parts=[types.Part(text=sys.argv[1])])]
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)


def main():
    if len(sys.argv) == 1:
        print("need argument")
        sys.exit(1)
    is_verbose = False
    if len(sys.argv) >= 3:
        is_verbose = sys.argv[2] == "--verbose"

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    iterations = 0
    while iterations <= config.MAX_ITERATIONS:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt
                ),
            )

            # print(f"response.candidates: {response.candidates}")

            if len(response.candidates) > 0:
                for candidate in response.candidates:
                    messages.append(candidate.content)

            if response.function_calls != None:
                for func in response.function_calls:
                    content = call.call_function(func, is_verbose)
                    if content.parts == None:
                        raise SystemExit("Error: no function's response")
                    messages.append(types.Content(parts=content.parts, role="user"))
                    # print(f"-> {content.parts[0].function_response.response}")
            else:
                print(f"\nFinal response:\n{response.text}")
                break
        except Exception as e:
            print(f"Error: {e}")
            break

        iterations += 1

    if is_verbose:
        print(
            f"User prompt: {sys.argv[1]}\n"
            f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n"
            f"Response tokens: {response.usage_metadata.candidates_token_count}"
        )


if __name__ == "__main__":
    main()
