import os
from bs4 import BeautifulSoup

def remove_html_tags_and_connect_sentences(html_content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Remove all script and style tags
    for script_or_style in soup(['script', 'style']):
        script_or_style.decompose()
    
    # Get the text content without HTML tags
    text_content = soup.get_text(separator=' ')
    
    # Connect sentences split by tags (no period) with a space
    text_content = ' '.join(text_content.split())
    
    return text_content

def process_html_files(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.html'):
            input_file_path = os.path.join(input_folder, filename)
            
            # Read the HTML file
            with open(input_file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            # Remove HTML tags and connect split sentences
            text_content = remove_html_tags_and_connect_sentences(html_content)
            
            # Write the cleaned text to a new file in the output folder
            output_filename = os.path.splitext(filename)[0] + '_cleaned.txt'
            output_file_path = os.path.join(output_folder, output_filename)
            
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text_content)
            
            print(f"Processed: {filename} -> {output_filename}")

if __name__ == "__main__":
    # Define input and output folders
    input_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input_html')
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output_text')
    
    # Process all HTML files in the input folder
    process_html_files(input_folder, output_folder)
