import math


def format_size(num_bytes: int | float) -> str:
    """Convert bytes to a human-readable size string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.2f} PB"


def clamp(value: int | float, _min: float | int, _max: float | int) -> int | float:
    if _min > _max:
        raise ValueError("min cannot by greater than max")
    return max(min(_max, value), _min)


def rad_to_deg(rad: float | int) -> float | int:
    deg = -rad * (180 / math.pi)
    return deg
