from io import BytesIO
from PIL import Image
from rich.table import Table
from rich.console import Console
from rich.panel import Panel
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

    console = Console()
    console.print(table)


def image_to_ascii(img: Image.Image):
    img = img.convert("RGB")

    max_dim = max(img.width, img.height)
    scale_factor = 1.0

    if max_dim > 1000:
        scale_factor = 1000 / max_dim
    elif max_dim < 500:
        scale_factor = 800 / max_dim

    if scale_factor != 1.0:
        new_w = int(img.width * scale_factor)
        new_h = int(img.height * scale_factor)
        img = img.resize((new_w, new_h))

    # Compute corrected height
    cell_width = int(img.width // (100 * 0.1))
    cell_height = int(img.height // (100 * 0.2))

    # Resize image to braille cell grid (2x4 pixels per cell)
    img = img.resize((cell_width * 2, cell_height * 4))
    pixels = img.load()

    output_lines = []
    for y in range(0, img.height, 4):
        line = ""
        for x in range(0, img.width, 2):
            bits = 0
            dots = [
                (0, 0, 0x01),
                (0, 1, 0x02),
                (0, 2, 0x04),
                (1, 0, 0x08),
                (1, 1, 0x10),
                (1, 2, 0x20),
                (0, 3, 0x40),
                (1, 3, 0x80),
            ]

            r_sum = g_sum = b_sum = count = 0
            for dx, dy, bit in dots:
                px, py = x + dx, y + dy
                if px < img.width and py < img.height:
                    r, g, b = pixels[px, py]
                    r_sum += r
                    g_sum += g
                    b_sum += b
                    count += 1
                    bits |= bit

            if count == 0:
                continue

            r = r_sum // count
            g = g_sum // count
            b = b_sum // count
            braille_char = chr(0x2800 + bits)
            line += f"[rgb({r},{g},{b})]{braille_char}[/rgb({r},{g},{b})]"
        output_lines.append(line)

    return "\n".join(output_lines)


def ascii(image: Image.Image, parser):
    console = Console()
    ascii_image = image_to_ascii(image)
    panel = Panel(ascii_image, title=parser.image, border_style="green", expand=False)
    console.print(panel)


def metadata(image: Image.Image, parser):
    get_image_metadata(image, parser.image)
