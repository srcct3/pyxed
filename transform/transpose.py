from PIL import Image


def horizontal(image: Image.Image):
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)


def vertical(image: Image.Image):
    return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)


def flip(image: Image.Image, parser):
    if parser.horizontal:
        return horizontal(image)
    return vertical(image)
