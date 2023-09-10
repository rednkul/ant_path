def ant_step(
        x: int,
        y: int,
        direction: int
) -> tuple[int, int, int]:
    match direction:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 2:
            y += 1
        case 3:
            x -= 1
    return x, y, direction
