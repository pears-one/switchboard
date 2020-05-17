above = "above"
below = "below"
left = "left"
right = "right"
directions = [above, right, below, left]


def opposite(direction):
    directions = [above, left, below, right]
    return directions[(directions.index(direction)+2) % 4]
