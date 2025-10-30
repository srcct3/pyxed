import os
from PIL import Image, UnidentifiedImageError


def load_image(path: str) -> Image.Image:
    if not os.path.exists(path):
        print(f"{path} could not be found")
        exit(1)
    try:
        image = Image.open(path)
        return image
    except UnidentifiedImageError as e:
        print(e)
        exit(1)


# TODO: save image
def save_image(image: Image.Image, path: str, format: str):
    raise NotImplementedError()
