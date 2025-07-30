import os
import re
from openai import OpenAI 

repo_path = '.' 

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
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
