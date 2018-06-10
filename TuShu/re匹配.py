import re

with open('./data/chun.txt', 'r') as f:
    a = f.read()

s = re.sub('{"content": "', '', a)
s = re.sub(r'\\n\\r\\n\\n\\r\\n', '\n', s)
s = re.sub(r'"title": "\\r\\n', '\n', s)
s = re.sub('"},', '', s)
s = re.sub('", "title": "', '', s)
s = re.sub('\\t' and '\\r', '', s)
with open('dong.txt', 'w') as f:
    f.write(s)
