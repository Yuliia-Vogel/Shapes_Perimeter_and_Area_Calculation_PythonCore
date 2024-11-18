def parse(args):
    """Parameters parcing for rectangle"""
    if len(args) != 6 or args[0].lower() != "topright" or args[3].lower() != "bottomleft":
        raise ValueError("Invalid format for Rectangle. Expected: 'TopRight X1 Y1 BottomLeft X2 Y2'")
    top_right = (int(args[1]), int(args[2]))
    bottom_left = (int(args[4]), int(args[5]))
    return {"top_right": top_right, "bottom_left": bottom_left}


def area(top_right, bottom_left) -> int: 
    width = abs(top_right[0] - bottom_left[0])
    lenght = abs(top_right[1] - bottom_left[1])
    return width * lenght


def perimeter(top_right, bottom_left) -> int:
    width = abs(top_right[0] - bottom_left[0])
    lenght = abs(top_right[1] - bottom_left[1])
    perim = width * 2 + lenght * 2
    return perim


def output(top_right, bottom_left) -> str:
    a = area(top_right, bottom_left)
    p = perimeter(top_right, bottom_left)
    print(f"Rectangle Perimeter {p} Area {a}")
    return f"Rectangle Perimeter {p} Area {a}"