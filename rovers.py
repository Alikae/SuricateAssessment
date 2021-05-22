import sys
from rover import Rover, DIRECTIONS
from utils import get_input, bad_format

def parse_map_size(line):
    try:
        line = line.split()
        if len(line) != 2:
            raise ValueError
        Rover.maxpos = [int(line[0]), int(line[1])]
        if Rover.maxpos[0] < 0 or Rover.maxpos[1] < 0:
            raise ValueError
    # ValueError also catch content not parsable as int
    except ValueError:
        bad_format("unsigned-integer unsigned-integer")

def init_rover(line):
    try:
        line = line.split()
        if len(line) != 3 or len(line[2]) != 1 or line[2] not in DIRECTIONS.keys():
            raise ValueError
        pos = [int(line[0]), int(line[1])]
        rover = Rover(pos, line[2])
    # ValueError also catch content not parsable as int
    except ValueError:
        bad_format("unsigned-integer unsigned-integer S|N|E|W")
    rover.assert_position_validity()
    return rover

def move_rover(rover, line):
    for c in line:
        if c == "M":
            rover.move()
            rover.assert_position_validity()
        elif c == "L" or c == "R":
            rover.rotate(c)
        else:
            bad_format("[L|R|M]*")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Bad Usage.\nUsage: 'rovers.py [file]'")
        sys.exit(3)
    input_file = None
    if len(sys.argv) == 2:
        try:
            input_file = open(sys.argv[1], "r")
        except FileNotFoundError:
            print(f"{sys.argv[1]} not found. Exiting.")
            sys.exit(4)
    parse_map_size(get_input(input_file, False))
    while True:
        rover = init_rover(get_input(input_file, True))
        move_rover(rover, get_input(input_file, False).strip())
        print(f"{rover.pos[0]} {rover.pos[1]} {rover.heading}")

