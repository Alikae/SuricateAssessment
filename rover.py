import sys

DIRECTIONS = {
    "N":    [0, 1],
    "E":    [1, 0],
    "W":    [-1, 0],
    "S":    [0, -1],
}

class Rover:
    maxpos = [0, 0]
    
    def __init__(self, pos, heading):
        self.pos = pos
        self.heading = heading

    def assert_position_validity(self):
        if self.pos[0] < 0 or \
                self.pos[0] > Rover.maxpos[0] or \
                self.pos[1] < 0 or \
                self.pos[1] > Rover.maxpos[1]:
            print("Whoups: The rover is out of range! Exiting.")
            sys.exit(2)

    def rotate(self, c):
        clockwise_directions = "NESW"
        i = clockwise_directions.index(self.heading)
        if c == "R":
            i += 1
        elif c == "L":
            i -= 1
        self.heading = clockwise_directions[i % 4]

    def move(self):
        self.pos[0] += DIRECTIONS[self.heading][0]
        self.pos[1] += DIRECTIONS[self.heading][1]

