from parsearg import get_parser
from image import load_image
from ops.resize import resize
from ops.rotate import rotate
from ops.crop import crop
from ops.transpose import flip
from ops.convert import convert
from ops.metadata import metadata


def main():
    parser = get_parser()
    image = load_image(parser.image)
    command = get_command(parser.command)
    if parser.command == "metadata":
        command(image, parser)
        exit(0)
    image = command(image, parser)
    image.show()


def get_command(command):
    commands = {
        "resize": resize,
        "crop": crop,
        "rotate": rotate,
        "flip": flip,
        "convert": convert,
        "metadata": metadata,
    }
    return commands[command]


if __name__ == "__main__":
    main()
