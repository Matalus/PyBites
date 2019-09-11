#pybites coding challege Bite 102

VALID_COLORS = ["blue","yellow","red"]

def print_colors():
    while True:
        color = input("Enter a color: ").lower()
        if color == 'quit':
            print("bye")
            break
        elif not(color in VALID_COLORS):
            print("Not a valid color")
            continue
        else:
            print(color)

print_colors()
        