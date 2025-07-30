import os
import re
from openai import OpenAI 

repo_path = '.' 

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("API key not found in environment variables")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    #count = len(re.findall(r'\bprint\s*\(', content))
                    #print(f"{file_path}: {count} print statement(s)")
                    completion = client.chat.completions.create(
                        extra_body={},
                        model="qwen/qwen3-coder:free",
                        messages=[
                            {
                                "role": "assisstant",
                                "content": "You are a helpful coding assistant, with deep knowledge in coding"
                            },
                            {
                                "role": "user",
                                "content": f"Summarize the code \n \n {content}"
                            }
                        ]
                    )
                    print(f"{file_path} Summary : {completion.choices[0].message.content}")

            except Exception as e:
                print(f"Error reading {file_path}: {e}")
