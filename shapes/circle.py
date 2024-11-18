import math


def parse(args):
    """Parameters parcing for circle"""
    if len(args) != 5 or args[0].lower() != "center" or args[3].lower() != "radius":
        raise ValueError("Invalid format for Circle. Expected: 'Center X Y Radius R'")
    center = (int(args[1]), int(args[2]))
    radius = int(args[4])
    # return {"center": center, "radius": radius}
    return {"radius": radius}


def area(radius): # S = πr^2
    a = round((math.pi * radius ** 2), 2) # rounding, 2 symbols after point
    return a


def perimeter(radius): #  C = 2πr
    p = round((2 * math.pi * radius), 2) # rounding, 2 symbols after point
    return p


def output(radius):
    a = area(radius)
    p = perimeter(radius)
    print(f"Circle Perimeter {p} Area {a}")
    return f"Circle Perimeter {p} Area {a}"