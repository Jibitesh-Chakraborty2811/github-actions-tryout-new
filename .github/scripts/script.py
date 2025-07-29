import os
import re

repo_path = '.'  # root of the repo

for root, dirs, files in os.walk(repo_path):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    count = len(re.findall(r'\bprint\s*\(', content))
                    print(f"{file_path}: {count} print statement(s)")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
