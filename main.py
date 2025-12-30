import sys
import os
from openai import OpenAI

# The client automatically picks up the API key from the OPENAI_API_KEY environment variable
client = OpenAI()

INPUT_PROMPT_PLAN = "./prompts/plan.txt"
INPUT_PROMPT_IMPLEMENTATION = "./prompts/implementation.txt"

OUTPUT_PLAN = "./results/plan.txt"
OUTPUT_IMPLEMENTATION = "./results/implementation.html"

INPUT_PRD_SPEC = "./1_PRD_Fishing_In_The_Deep.md"

def write_file(filename, content):
    """Saves the given content to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)


def read_file(filename):
    """Reads and returns the content of a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


def get_chat_response(prompt):
    """Sends a prompt to the ChatGPT API and returns the response."""
    try:
        completion = client.chat.completions.create(
            model="gpt-5.1",
            messages=[
                {"role": "system", "content": "You are a coding assistant for web game development."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def generate_implementation_plan():
    print("$ 1 - IMPLEMENTATION PLAN")
    prompt = read_file(INPUT_PROMPT_PLAN)
    prd_content = read_file(INPUT_PRD_SPEC)
    
    final_prompt = prompt.format(prd=prd_content)
    print(f"$ 1 - FINAL PROMPT:\n{final_prompt}\n")
    print("$ 1 - GENERATING RESPONSE...")
    
    ai_response = get_chat_response(final_prompt)
    
    write_file(OUTPUT_PLAN, ai_response)
    print(f"$ 1 - DONE! Saved to {OUTPUT_PLAN}")

def generate_implementation_code():
    print("$ 2 - IMPLEMENTATION CODE")
    prompt = read_file(INPUT_PROMPT_IMPLEMENTATION)
    plan_content = read_file(OUTPUT_PLAN)
    
    final_prompt = prompt.format(plan=plan_content)
    print(f"$ 2 - FINAL PROMPT:\n{final_prompt}\n")
    print("$ 2 - GENERATING RESPONSE...")
    
    ai_response = get_chat_response(final_prompt)
    
    write_file(OUTPUT_IMPLEMENTATION, ai_response)
    print(f"$ 2 - DONE! Saved to {OUTPUT_IMPLEMENTATION}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--plan":
        generate_implementation_plan()
    else:
        generate_implementation_code()
