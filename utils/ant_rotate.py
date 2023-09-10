def ant_rotate(
        cell: int,
        direction: int
) -> int:
    if cell:
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction