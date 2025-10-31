from io import BytesIO
from PIL import Image
from image import get_supported_format


def convert_image(image: Image.Image, fmt: str) -> Image.Image:
    supported = get_supported_format("convertable")
    fmt = fmt.upper()
    if fmt not in supported:
        print(f"{fmt} not supported")
        exit(1)

    try:
        buffer = BytesIO()
        image.save(buffer, fmt)
        return Image.open(buffer)
    except Exception as e:
        print(f"image conversion to {fmt} failed with error:")
        print(e)
        exit(1)


def convert(image: Image.Image, parser):
    return convert_image(image, parser.fmt)
