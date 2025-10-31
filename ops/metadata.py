from io import BytesIO
from PIL import Image
from rich.table import Table
from rich.console import Console
from rich import box
from pathlib import Path
from util import format_size


def get_image_metadata(image: Image.Image, filename: str):
    buffer = BytesIO()
    image.save(buffer, image.format)
    file_size = format_size(buffer.tell())
    mode = image.mode
    dimensions = image.size
    fmt = image.format

    table = Table(
        show_header=True, header_style="bold green", expand=True, box=box.ROUNDED
    )
    table.add_column("Property", justify="left", style="cyan", ratio=1)
    table.add_column("Value", justify="left", style="magenta", ratio=2)

    table.add_row("File name", Path(filename).name)
    table.add_row("File size", f"{file_size}")
    table.add_row("Format", fmt)
    table.add_row("Size (WxH)", f"{dimensions[0]}x{dimensions[1]}")
    table.add_row("Mode", mode)

    # panel = Panel(table, title="Image Info", border_style="green")
    console = Console()
    console.print(table)


def metadata(image: Image.Image, parser):
    get_image_metadata(image, parser.image)
