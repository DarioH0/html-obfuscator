from bs4 import BeautifulSoup

html_file = 'example.html'
javascript_file = 'example.js'

with open(html_file, 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    html_lines = soup.prettify().split('\n')

with open(javascript_file, 'w') as js:
    js.write('window.onload = function() {\n')
    for line in html_lines:
        if line.strip() == '' or line.strip().startswith('<!--'):
            continue

        if not line.strip().startswith('<'):
            line = f'<p>{line}</p>'
        js.write(f"document.body.insertAdjacentHTML('beforeend', `{line}`);\n")
    js.write('};')

