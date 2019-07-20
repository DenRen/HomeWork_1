from uuid import uuid4
from qrcode import make
from jinja2 import Template
from imgkit import from_file
from os import remove
from base64 import b64encode


s = str(uuid4())
img = make(s)
img.save(s, format='jpeg')

data_uri = str(b64encode(open(s, 'rb').read()))[2:-1]
print(s)
remove(s)
with open('index.html', 'r+') as f:
    template = Template(f.read())
    with open('index_new.html', 'w') as f1:
        f1.write(template.render(qr_code=data_uri))
from_file('index_new.html','out.jpg')

remove('index_new.html')