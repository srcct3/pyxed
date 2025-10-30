from parsearg import get_parser
from image import load_image
from transform.resize import resize
from transform.rotate import rotate
from transform.crop import crop
from transform.transpose import flip


def main():
    parser = get_parser()
    image = load_image(parser.image)
    print(image.size)
    command = get_command(parser.command)
    image = command(image, parser)
    print(image.size)
    image.show()


def get_command(command):
    commands = {
        "resize": resize,
        "crop": crop,
        "rotate": rotate,
        "flip": flip,
    }
    return commands[command]


if __name__ == "__main__":
    main()
