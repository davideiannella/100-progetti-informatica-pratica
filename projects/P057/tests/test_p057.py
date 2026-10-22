from pathlib import Path
from io import BytesIO
from PIL import Image
import sys, hashlib
sys.path.append(str(Path(__file__).parents[1]/'src'))
from function import handle_image
buffer = BytesIO()
Image.new('RGB', (3, 2), 'blue').save(buffer, format='PNG')
data = buffer.getvalue()
r = handle_image(data)
assert (r['width'],r['height'],r['format']) == (3,2,'PNG')
assert r['sha256'] == hashlib.sha256(data).hexdigest()
for bad in [b'', b'not an image', data[:25], data[:-20]]:
    try: handle_image(bad)
    except ValueError: pass
    else: raise AssertionError('invalid image accepted')
print('P057 PASS: immagine decodificata, hash e corruzione')
