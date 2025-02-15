import os
import sys

SEARCH_REPLACE_LIST = [
    ("  ", " "),
]

def apply_search_replace(content, search_replace_list):
    for search_term, replacement in search_replace_list:
        content = content.replace(search_term, replacement)
    return content

def process_txt_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            modified_content = apply_search_replace(content, SEARCH_REPLACE_LIST)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            print(f"Processed: {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search_replace.py <folder_path>")
        sys.exit(1)
    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        sys.exit(1)
    process_txt_files(folder_path)
