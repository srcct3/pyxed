import argparse

from image import get_supported_format

type subparser_type = argparse._SubParsersAction[argparse.ArgumentParser]


def get_parser():
    parser = argparse.ArgumentParser(
        prog="main.py", description="Basic Image editing CLI"
    )

    subparser = parser.add_subparsers(dest="command", required=True)
    resize_parser(subparser)
    rotate_parser(subparser)
    flip_parser(subparser)
    crop_parser(subparser)
    convert_parser(subparser)
    metadata_parser(subparser)
    print_parser(subparser)
    canvas_parser(subparser)

    parsed = parser.parse_args()
    if parsed.command == "resize":
        if parsed.relative and not parsed.mode:
            parsed.mode = "cover"
        elif parsed.mode and not parsed.relative:
            parser.error("--mode can only be used with --relative")

    return parsed


def canvas_parser(subparser: subparser_type):
    parser = init_parser(subparser, "canvas", "Expand image canvas")
    parser.add_argument(
        "--expand",
        "-e",
        required=True,
        type=int,
        help="Expand percentage",
    )
    parser.add_argument(
        "--color",
        "-c",
        nargs=3,
        type=int,
        metavar=("R", "G", "B"),
        default=(255, 255, 255),
    )


def print_parser(subparser: subparser_type):
    init_parser(subparser, "print", "Print image as ascii")


def metadata_parser(subparser: subparser_type):
    init_parser(subparser, "metadata", "Show image metadata")


def convert_parser(subparser: subparser_type):
    fmt = get_supported_format("convertable")
    parser = init_parser(subparser, "convert", f"Convert image formats: {fmt}")
    parser.add_argument(
        "--fmt",
        "-f",
        required=True,
        type=str.upper,
        choices=fmt,
        help="Format to convert to",
    )


def crop_parser(subparser: subparser_type):
    parser = init_parser(subparser, "crop", "Crop image [--box, --center, --xy]")
    crop_group = parser.add_mutually_exclusive_group(required=True)
    crop_group.add_argument(
        "--box",
        nargs=4,
        type=int,
        metavar=("TX", "TY", "BX", "BY"),
        help="Top x, y and bottom x, y positions",
    )
    crop_group.add_argument("--center", type=int, help="Center anchored crop")
    crop_group.add_argument(
        "--xy", nargs=2, metavar=("X", "Y"), type=int, help="Symmetric crop"
    )


def flip_parser(subparser: subparser_type):
    parser = init_parser(subparser, "flip", "Flip image [-H, -V]")
    flip_group = parser.add_mutually_exclusive_group(required=True)
    flip_group.add_argument(
        "-H", "--horizontal", action="store_true", help="Flip image horizontal"
    )
    flip_group.add_argument(
        "-V", "--vertical", action="store_true", help="Flip image vertical"
    )


def rotate_parser(subparser: subparser_type):
    parser = init_parser(
        subparser, "rotate", "Rotate image [--angle, --rad, --expand(optional)]"
    )
    rotate_group = parser.add_mutually_exclusive_group(required=True)
    rotate_group.add_argument(
        "--angle",
        type=int,
        help="Angle in degrees (positive for CW, negative for CCW).",
    )
    rotate_group.add_argument(
        "--rad", type=float, help="Angle in radian (positive for CW, negative for CCW)"
    )
    parser.add_argument(
        "--expand",
        type=bool,
        default=False,
        help="Expand to fit full image",
    )


def resize_parser(subparser: subparser_type):
    parser = init_parser(
        subparser, "resize", "Resize image [--size, --scale, --relative]"
    )
    group_parser = parser.add_mutually_exclusive_group(required=True)
    group_parser.add_argument(
        "--size",
        "-s",
        nargs=2,
        type=int,
        metavar=("WIDTH", "HIGHT"),
        help="Target width and hight in pixel",
    )
    group_parser.add_argument("--scale", "-S", type=int, help="Scale percentage")
    group_parser.add_argument(
        "--relative",
        nargs=2,
        metavar=("WIDTH", "HIGHT"),
        help="Scale relative to a given size [w h] mode (cover, contain, fit, pad)",
    )
    parser.add_argument(
        "--mode",
        "-m",
        choices=["contain", "cover", "fit", "pad"],
        help="Scale mode for --relative [contain, cover(default), fit, pad]",
    )


def init_parser(
    subparser: subparser_type, name: str, help: str, out: str | None = None
):
    parser = subparser.add_parser(name, help=help)
    parser.add_argument("image", help="Path to the image")
    parser.add_argument("--output", "-o", default=out, help="Path to save edited image")
    return parser
