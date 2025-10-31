from PIL import Image
from util import rad_to_deg


def angle(image: Image.Image, angle: int, expand: bool):
    return image.rotate(angle, expand=expand)


def rad(image: Image.Image, rad: float, expand: bool):
    return image.rotate(rad_to_deg(rad), expand=expand)


def rotate(image: Image.Image, parser):
    if parser.angle:
        return angle(image, parser.angle, parser.expand)
    return rad(image, parser.rad, parser.expand)
