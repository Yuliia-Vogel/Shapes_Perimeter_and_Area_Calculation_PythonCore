
def parse(args):
    """Parameters parcing for square"""
    if len(args) != 5 or args[0].lower() != "topright" or args[3].lower() != "side":
        raise ValueError("Invalid format for Square. Expected: 'TopRight X Y Side L'")
    
    side = int(args[4]) 
    return {"side": side}


def area(side): 
    a = side ** 2
    return a


def perimeter(side):
    p = side * 4
    return p


def output(side):
    a = area(side)
    p = perimeter(side)
    print(f"Square Perimeter {p} Area {a}")
    return f"Square Perimeter {p} Area {a}"