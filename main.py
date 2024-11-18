import sys
import importlib
        

def parse_args():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} shape parameters")
        sys.exit(1)
    
    shape = sys.argv[1].lower()  # shape name
    params = sys.argv[2:]  # parameters
    
    # Parameters check for min parameters for each shape:
    shape_min_args = {
        "square": 5,      # TopRight X Y Side L
        "rectangle": 6,   # TopRight X1 Y1 BottomLeft X2 Y2
        "circle": 5,      # Center X Y Radius R
    }

    if shape not in shape_min_args: # check for shapes available
        print(f"Error: Unknown shape '{shape}'. Supported shapes: {', '.join(shape_min_args.keys())}")
        sys.exit(1)

    if len(params) < shape_min_args[shape]: # check if enough parameters for each shape:
        print(f"Error: Not enough parameters for shape '{shape}'. Expected at least {shape_min_args[shape]} parameters.")
        sys.exit(1)

    return shape, params
    
    
def main():
    try:
        shape, params = parse_args()

        # dynamic module import for exact shape:
        module = importlib.import_module(f"shapes.{shape}")

        # params parsing
        parsed_data = module.parse(params)
        # generating output 
        output = module.output(**parsed_data)
        return output
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()