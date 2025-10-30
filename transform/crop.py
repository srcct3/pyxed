from PIL import Image
from util import clamp


def box(image: Image.Image, box: tuple[int, int, int, int]):
    width, height = image.size
    left, upper, right, lower = box

    left = max(0, min(left, width))
    upper = max(0, min(upper, height))
    right = max(0, min(right, width))
    lower = max(0, min(lower, height))

    return image.crop((int(left), int(upper), int(right), int(lower)))


def xy(image: Image.Image, xy: tuple[int, int]):
    x, y = xy
    width, height = image.size

    x_max = (width // 2) - 1
    y_max = (height // 2) - 1

    new_x = min(x, x_max)
    new_y = min(y, y_max)

    left, upper = new_x, new_x
    right, lower = width - new_x, height - new_y

    return image.crop((left, upper, right, lower))


def center(image: Image.Image, size: int):
    width, height = image.size
    val = clamp(size, 0, 100)
    frac = 1 - (val / 100)
    new_width = max(1, int(width * frac))
    new_height = max(1, int(height * frac))

    left = (width - new_width) // 2
    upper = (height - new_height) // 2
    right = left + new_width
    lower = upper + new_height

    return image.crop((left, upper, right, lower))


def crop(image: Image.Image, parser):
    if parser.box:
        return box(image, parser.box)
    elif parser.xy:
        return xy(image, parser.xy)
    return center(image, parser.center)
