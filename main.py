import random

row = 6
column = 6

maze = []

lastRow = 0
lastColumn = 0


def setup():
    for r in range(max(1, row)):
        col = list()
        for c in range(max(1, column)):
            col.append("[ ]")
        maze.append(col)


def clean():
    for r in range(0, row):
        for c in range(0, column):
            maze[r][c] = "[ ]"


def randomTeleport():
    maze[lastRow][lastColumn] = "[ ]"
    r = random.randint(0, row - 1)
    c = random.randint(0, column - 1)
    maze[r][c] = "[x]"


def printMaze():
    for r in maze:
        for c in r:
            print(c, end='')
        print()
    print("---------------------")


def waitKey():
    return input("")


def move(s):
    global lastRow, lastColumn
    nextColumn = lastColumn
    nextRow = lastRow
    if s == "w":
        nextRow = max(0, lastRow - 1)
    elif s == "s":
        nextRow = min(row - 1, lastRow + 1)
    elif s == "a":
        nextColumn = max(0, lastColumn - 1)
    elif s == "d":
        nextColumn = min(column - 1, lastColumn + 1)
    if maze[nextRow][nextColumn][1] == "|":
        return
    maze[lastRow][lastColumn] = "[ ]"
    lastRow = nextRow
    lastColumn = nextColumn
    maze[lastRow][lastColumn] = "[x]"


def placeRandomObject():
    r = random.randint(0, row - 1)
    c = random.randint(0, column - 1)
    maze[r][c] = "[|]"


def start():
    for i in range(0, random.randint(0, 10)):
        placeRandomObject()
    while True:
        move(waitKey())
        printMaze()


if __name__ == '__main__':
    setup()
    start()
