import sys
import re

input_file = sys.argv[1] + ".html"
output_file = sys.argv[1] + ".txt"

with open(input_file, 'r', encoding='utf-8') as file:
    html = file.read()

body_match = re.search(r'<body.*?>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)

if not body_match:
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('[]')
    sys.exit()

body_content = body_match.group(1)
elements = re.findall(r'<[^>]+>|&[^;]+;|[^<&]+', body_content)

classified_elements = []
for item in elements:
    if item.startswith('<') and item.endswith('>'):
        classified_elements.append({'type': '0', 'content': item})
    elif item.startswith('&') and item.endswith(';'):
        classified_elements.append({'type': '1', 'content': item})
    else:
        classified_elements.append({'type': '2', 'content': item})

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(str(classified_elements))
