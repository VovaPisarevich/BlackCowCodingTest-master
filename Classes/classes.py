import sys
import json
from enum import Enum
from memory_profiler import profile


class Point:
    """
    Creates a point on a coordinate plane with values x and y.
    """

    def __init__(self, x=0, y=0):
        """
        Defines x and y variables
        """
        self.x = x
        self.y = y


class Direction(Enum):
    north = 1
    east = 2
    south = 3
    west = 4


class Asteroid(Point):

    def __init__(self, size: Point):
        """
        Asteroid class
        :param size:
        :type size: Point(x,y)
        """
        self.x = size.x
        self.y = size.y


class Robot:
    """
    A class describing a single robot
    """

    def __init__(self, position: Point = Point(), bearing: Direction = Direction.north, asteroid: Asteroid = None) -> object:
        """
        :param position: Initial position of the Robot in Asteroid coordinate plane
        :type Point: (x,y)
        :param bearing: Initial bearing of the Robot e.g. north, east, south, west
        :type Direction:
        :param asteroid: the asteroid the robot belongs to
        :type Asteroid class

        """

        self.position = position
        # VP todo: check if a bearing is valid
        self.bearing = bearing
        self.asteroid = asteroid

    # For memory monitoring uncomment next line
    # @profile
    def turn(self, turn_to: str):
        """
        Purpose: to turn a robot (change the bearing)
        :param turn_to: turn_right or turn_left
        :type turn_to: str
        :return: None

        """
        b = self.bearing
        ib = self.bearing.value

        values = [member.value for member in Direction]
        min_value = min(values)
        max_value = max(values)

        if turn_to == 'turn-left':
            ib -= 1
            if ib < min_value:
                ib = max_value
        elif turn_to == 'turn-right':
            ib += 1
            if ib > max_value:
                ib = min_value

        # north = 1
        # east =  2
        # south =  3
        # west =   4

        self.bearing = Direction(ib)

    # @profile
    def move(self, move="move-forward"):
        """
        Purpose: to move a robot (change position)
        :param move: where to move
        :type move: str
        :return: None
        """
        # For boundaries checking
        old_position = Point(self.position.x, self.position.y)

        if move == "move-forward":
            if self.bearing == Direction.north:
                self.position.y += 1
            elif self.bearing == Direction.east:
                self.position.x += 1
            elif self.bearing == Direction.south:
                self.position.y -= 1
            elif self.bearing == Direction.west:
                self.position.x -= 1

        # check for boundaries VP todo write a private method check_boundaries 
        if self.asteroid is not None:
            if self.position.x > self.asteroid.x or self.position.y > self.asteroid.y \
                    or self.position.x < 0 or self.position.y < 0:
                self.position = old_position  # dont' move
    #
    # End of class Robot


# @profile
def printout(robotlist: [Robot]):
    """
    Purpose: To print robot's final positions in a given format.
    :param robotlist: List of existing robots
    :type robotlist:
    :return:
    :rtype:
    """
    for r in robotlist:
        dr = {"type": "robot", "position": r.position.__dict__, "bearing": r.bearing.name}
        print(dr)


# @profile
def proceed_file(filename: str) -> object:
    #messagelist = []
    robots: Robot = []

    with open(filename) as f:
        for line in f:
            message = json.loads(line)

            # we got a message which is a dictionary
            #messagelist.append(message)
            # proceed each message: analyze message dict
            messagetype = message["type"]

            if messagetype == 'asteroid':
                size = message["size"]
                size = Point(size["x"], size["y"])
                a = Asteroid(size)
                continue
            if messagetype == 'new-robot':  # create a new robot
                position = message["position"]
                bearing = message["bearing"]
                direction = Direction[bearing]
                starting_point = Point(position["x"], position["y"])
                r: Robot = Robot(starting_point, direction, a)
                #print("New Robot Initial position = ", r.position.x, ", ", r.position.y, " Bearing= ", r.bearing)
                robots.append(r)
                continue
            if messagetype == 'move':
                movement = message["movement"]
                if movement.rfind("move") != -1:  # found "move" e.g. "move-forward"
                    r.move(movement)
                    #print("Robot moving position = ", r.position.x, ", ", r.position.y, " Bearing= ", r.bearing)
                elif movement.rfind("turn") != -1:  # found "turn... left or right"
                    r.turn(movement)
                    #print("Robot turning position = ", r.position.x, ", ", r.position.y, " Bearing= ", r.bearing)
                continue

        printout(robots)


