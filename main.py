import sys
import importlib

from pathlib import Path


def parse_args():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} shape parameters")
        sys.exit(1)
    
    shape = sys.argv[1].lower()  # shape name
    params = sys.argv[2:]  # parameters

    return shape, params
    
    
def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} shape parameters")
        sys.exit(1)
    
    shape = sys.argv[1].lower()  # shape name
    params = sys.argv[2:]  # parameters
    try:
        # Create a platform-independent path to the module:
        module_path = Path("shapes") / f"{shape}.py"
        if module_path.is_file():
        # dynamic module import for exact shape:
            module = importlib.import_module(f"shapes.{shape}")
            # params parsing:
            parsed_data = module.parse(params)
            # generate output: 
            output = module.output(**parsed_data)
            return output
        else:
            print(f"Shape {shape} is not supported.")
            sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()