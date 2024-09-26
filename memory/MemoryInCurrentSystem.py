import sys
def main():
    my_val = 13
    # Print value of my_val
    print(f"Value of integer 'my_val': {my_val}")
    # Print size of my_val (using sys.getsizeof to get size of the integer)
    print(f"Size of integer 'my_val': {sys.getsizeof(my_val)} bytes")
    # Print address of my_val (using id() to get memory address in Python)
    print(f"Address of 'my_val': {hex(id(my_val))}")
    # Print size of the address (Python doesn't have pointer sizes, so we use size of id())
    print(f"Size of the address of 'my_val': {sys.getsizeof(id(my_val))} bytes")

if __name__ == "__main__":
    main()