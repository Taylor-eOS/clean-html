from bs4 import BeautifulSoup

with open('1.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')
body = soup.body
if body:
    raw_text = body.get_text(separator=' ')
    new_body = soup.new_tag('body')
    new_body.string = ' '.join(raw_text.split())
    body.replace_with(new_body)
    with open('1_cleaned.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

