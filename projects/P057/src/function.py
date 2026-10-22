from io import BytesIO
from hashlib import sha256
from PIL import Image, UnidentifiedImageError

def handle_image(data: bytes):
    if not isinstance(data, bytes) or not data or len(data) > 10 * 1024 * 1024:
        raise ValueError("immagine vuota o oltre 10 MiB")
    try:
        with Image.open(BytesIO(data)) as image:
            if image.width * image.height > 20_000_000:
                raise ValueError("troppi pixel")
            image.verify()
        with Image.open(BytesIO(data)) as image:
            image.load()
            return {"bytes": len(data), "sha256": sha256(data).hexdigest(),
                    "format": image.format, "width": image.width, "height": image.height}
    except (UnidentifiedImageError, OSError, SyntaxError, Image.DecompressionBombError) as exc:
        raise ValueError("immagine non valida") from exc
