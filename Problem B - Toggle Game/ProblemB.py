
import sys
import queue
import copy

class Board():
    def __init__(self):
        "Initalizing the board with depth 0 (since no moves have been made)"
        self.depth = 0
        self.board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
        self.goal = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

    def read_goal_board(self, line, linenr):
        "Inserts the goal into self.goal line by line"
        for c in range(0, 3):
            self.goal[linenr][c] = line[c]

    def print_goal_board(self):
        "Checks if the goal has been implemented correctly"
        print("Print current goal: ", self.goal)

    def toggle(self, row, col):
        "Flips the color of the tile and all adjencent tiles"
        if row == 0 and col == 0:
            "Top left corner"
            self.switch(row, col)
            self.switch(row + 1, col)
            self.switch(row, col + 1)

        elif row == 0 and col == 2:
            "Top right corner"
            self.switch(row, col)
            self.switch(row - 1, col)
            self.switch(row, col - 1)

        elif row == 2 and col == 0:
            "Bottom left corner"
            self.switch(row, col)
            self.switch(row - 1, col)
            self.switch(row, col + 1)

        elif row == 2 and col == 2:
            "Bottom right corner"
            self.switch(row, col)
            self.switch(row, col - 1)
            self.switch(row - 1, col)

        elif row == 1 and col == 1:
            "Middle"
            self.switch(row, col)
            self.switch(row, col + 1)
            self.switch(row, col - 1)
            self.switch(row + 1, col)
            self.switch(row - 1, col)

        elif row == 0 and col == 1:
            "Top middle"
            self.switch(row, col)
            self.switch(row + 1, col)
            self.switch(row, col - 1)
            self.switch(row, col + 1)

        elif row == 1 and col == 0:
            "Mid left"
            self.switch(row, col)
            self.switch(row - 1, col)
            self.switch(row + 1, col)
            self.switch(row, col + 1)

        elif row == 1 and col == 2:
            "Mid right"
            self.switch(row, col)
            self.switch(row - 1, col)
            self.switch(row + 1, col)
            self.switch(row, col - 1)

        elif row == 2 and col == 1:
            "Bottom middle"
            self.switch(row, col)
            self.switch(row - 1, col)
            self.switch(row, col - 1)
            self.switch(row, col + 1)

    def switch(self, row, col):
        "Flips color"
        if self.board[row][col] == '.':
            self.board[row][col] = '*'
        elif self.board[row][col] == '*':
            self.board[row][col] = '.'

    def check_board(self):
        "Checks if the current board is the same as the goal board"
        ck = 0
        for k in range(0, 3):
            if self.board[k] == self.goal[k]:
                ck += 1
        if ck == 3:
            return 1
        return 0

    def copy(self):
        "Makes a deep copy/independent object of our current board"
        b = copy.deepcopy(self)
        return b

    def set_depth(self,depth):
        "Updates how many moves have been made to the board"
        self.depth = depth

    def add_neighbours(self):
        "Makes a list of all 9 different outcomes of our current board"
        list = []
        for row in range(0, 3):
            for col in range(0,3):
                b = self.copy()
                b.set_depth(self.depth+1)
                b.toggle(row, col)
                list.append(b)
        return list

    def bfs_search(self):
        "Using breadth first search, the minimum required moves to reach a goal board is found."
        Q = queue.Queue()
        Q.put(self)
        while not Q.empty():
            u = Q.get()
            if u.check_board():
                print(u.depth)
                return
            else:
                BS = u.add_neighbours()
                for i in range(len(BS)):
                    Q.put(BS[i])

linenr = -1
boardlines = []

for line in sys.stdin:
    linenr += 1

    if linenr != 0:
        "Adds line to boardlines"
        ab = line.split()
        boardlines.append(list(ab[0]))

    if linenr % 3 == 0 and linenr != 0:
        "For every board(three lines), each char in the lines is assigned to the board's goal state"
        "Then run bfs on the board"
        board = Board()
        for i in range(0, 3):
            board.read_goal_board(boardlines[i], i)

        board.bfs_search()
        boardlines = []

    if linenr == 0:
        "First line in input indicates how many boards shall be tested"
        ab = line.split()
        num = int(ab[0])

