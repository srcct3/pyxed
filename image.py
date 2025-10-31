import os
from typing import Literal, Union
from PIL import Image, UnidentifiedImageError


def load_image(path: str):
    if not os.path.exists(path):
        print(f"{path} could not be found")
        exit(1)
    try:
        image = Image.open(path)
        return image
    except UnidentifiedImageError as e:
        print(e)
        exit(1)


def get_supported_format(purpose: Literal["all", "convertable"] = "all") -> list[str]:
    Image.init()
    readable = set(Image.registered_extensions().values())
    writable = set(Image.SAVE.keys())
    supported = readable & writable
    convertable = [
        "AVIF",
        "BMP",
        "DDS",
        "DIB",
        "GIF",
        "ICNS",
        "ICO",
        "JPEG",
        "JPEG2000",
        "JPEG",
        "PCX",
        "PNG",
        "PPM",
        "QOI",
        "SGI",
        "TGA",
        "TIFF",
        "WEBP",
    ]
    return list(supported) if purpose == "all" else convertable


# TODO: save image
def save_image(image: Image.Image, path: str, format: str):
    raise NotImplementedError()
