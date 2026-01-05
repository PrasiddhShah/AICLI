import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt
from call_function import available_functions,call_function
def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("--verbose",action="store_true",help="Enable verbose output")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("Gemini Key not available")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user",parts=[types.Part(text=args.user_prompt)])]
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    generate_content (client,messages,args.verbose)

def generate_content(client,messages,verbose):
    function_result = list()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions()],
            system_instruction=system_prompt),
        )
    if not response.usage_metadata:
        raise RuntimeError("Metadata Empty!!!! Please check API Key")
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    if response.function_calls:
        for func_call in response.function_calls:
            function_call_result = call_function(func_call,verbose)
            if not function_call_result.parts:
                raise Exception("function_call_result parts empty")
            if not function_call_result.parts[0].function_response:
                raise Exception("function response empty")
            if not function_call_result.parts[0].function_response.response:
                raise Exception("function response response empty")
            function_result.append(function_call_result.parts[0])
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    else:
        print(response.text)

if __name__ == "__main__":
    main()