from PIL import Image, ImageOps

from util import clamp


def scale(image: Image.Image, scale: int) -> Image.Image:
    val = clamp(scale * -1, 1, 99) * -1 if scale < 0 else clamp(scale, 1, 99)
    width, height = image.size

    width += (val / 100) * width
    height += (val / 100) * height
    return image.resize((int(width), int(height)))


def size(image: Image.Image, size: tuple[int, int]):
    width, height = size
    width = max(width, 1)
    height = max(height, 1)
    return image.resize((width, height))


def relative(image: Image.Image, relative_size: tuple[int, int], mode: str):
    match mode:
        case "cover":
            image = ImageOps.cover(image, relative_size)
        case "contain":
            image = ImageOps.contain(image, relative_size)
        case "fit":
            image = ImageOps.fit(image, relative_size)
        case "pad":
            image = ImageOps.pad(image, relative_size)
    return image


def resize(image: Image.Image, parser):
    if parser.scale:
        return scale(image, parser.scale)
    elif parser.relative:
        return relative(image, parser.relative, parser.mode)
    return size(image, parser.size)
