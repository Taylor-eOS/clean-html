import sys
import re

input_file = sys.argv[1]
output_file = "output.txt"

with open(input_file, 'r', encoding='utf-8') as file:
    html = file.read()

body_match = re.search(r'<body.*?>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)

if not body_match:
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write('[]')
    sys.exit()

body_content = body_match.group(1)
elements = re.findall(r'<[^>]+>|[^<]+', body_content)

with open(output_file, 'w', encoding='utf-8') as outfile:
    outfile.write(str(elements))
