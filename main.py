# This is a sample Python script.
import sys
from Classes.classes import Point, Direction, Robot, Asteroid, proceed_file
#from memory_profiler import profile

# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    if len(sys.argv) < 2:
        sys.exit("Exit program: No program argument(s) provided.")
    else:
        file = sys.argv[1]

    proceed_file(file)


