import math


def clamp(value: int | float, _min: float | int, _max: float | int) -> int | float:
    if _min > _max:
        raise ValueError("min cannot by greater than max")
    return max(min(_max, value), _min)


def rad_to_deg(rad: float | int) -> float | int:
    deg = -rad * (180 / math.pi)
    return deg
