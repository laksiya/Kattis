def toggle(self, row, col):
    b = self.copy()
    print("Before toggle: ", b.board)
    if row == 0 and col == 0:
        "Top left corner"
        b.switch(row, col)
        b.switch(row + 1, col)
        b.switch(row, col + 1)

    elif row == 0 and col == 2:
        "Top right corner"
        b.switch(row, col)
        b.switch(row + 1, col)
        b.switch(row, col - 1)

    elif row == 2 and col == 0:
        "Bottom left corner"
        b.switch(row, col)
        b.switch(row - 1, col)
        b.switch(row, col + 1)

    elif row == 2 and col == 2:
        "Bottom right corner"
        b.switch(row, col)
        b.switch(row, col - 1)
        b.switch(row - 1, col)

    elif row == 1 and col == 1:
        "Middle"
        b.switch(row, col)
        b.switch(row, col + 1)
        b.switch(row, col - 1)
        b.switch(row + 1, col)
        b.switch(row - 1, col)

    elif row == 0 and col == 1:
        "Top middle"
        b.switch(row, col)
        b.switch(row + 1, col)
        b.switch(row, col - 1)
        b.switch(row, col + 1)

    elif row == 1 and col == 0:
        "Mid left"
        b.switch(row, col)
        b.switch(row - 1, col)
        b.switch(row + 1, col)
        b.switch(row, col + 1)

    elif row == 1 and col == 2:
        "Mid right"
        b.switch(row, col)
        b.switch(row - 1, col)
        b.switch(row + 1, col)
        b.switch(row, col - 1)

    elif row == 2 and col == 1:
        "Bottom middle"
        b.switch(row, col)
        b.switch(row - 1, col)
        b.switch(row, col - 1)
        b.switch(row, col + 1)
    print("After toggle: ", b.board)
    return b


        def toggle(self, board, row, col):
            if row == 0 and col == 0:
                "Top left corner"
                self.switch(board, row, col)
                self.switch(board, row + 1, col)
                self.switch(board, row, col + 1)

            elif row == 0 and col == 2:
                "Top right corner"
                self.switch(board, row, col)
                self.switch(board, row - 1, col)
                self.switch(board, row, col + 1)

            elif row == 2 and col == 0:
                "Bottom left corner"
                self.switch(board, row, col)
                self.switch(board, row - 1, col)
                self.switch(board, row, col + 1)

            elif row == 2 and col == 2:
                "Bottom right corner"
                self.switch(board, row, col)
                self.switch(board, row, col - 1)
                self.switch(board, row - 1, col)

            elif row == 1 and col == 1:
                "Middle"
                self.switch(board, row, col)
                self.switch(board, row, col + 1)
                self.switch(board, row, col - 1)
                self.switch(board, row + 1, col)
                self.switch(board, row - 1, col)

            elif row == 0 and col == 1:
                "Top middle"
                self.switch(board, row, col)
                self.switch(board, row + 1, col)
                self.switch(board, row, col - 1)
                self.switch(board, row, col + 1)

            elif row == 1 and col == 0:
                "Mid left"
                self.switch(board, row, col)
                self.switch(board, row - 1, col)
                self.switch(board, row + 1, col)
                self.switch(board, row, col + 1)

            elif row == 1 and col == 2:
                "Mid right"
                self.switch(board, row, col)
                self.switch(board, row - 1, col)
                self.switch(board, row + 1, col)
                self.switch(board, row, col - 1)

            elif row == 2 and col == 1:
                "Bottom middle"
                self.switch(board, row, col)
                self.switch(board, row - 1, col)
                self.switch(board, row, col - 1)
                self.switch(board, row, col + 1)

        def switch(self, board, row, col):
            if board.board[row][col] == '.':
                board.board[row][col] = '*'
            elif board.board[row][col] == '*':
                board.board[row][col] == '.'



    def add_neighbours(self):
        for row in range(0, 3):
            for col in range(0,3):
                b = self.copy()
                b.toggle(row, col)
                print("Toggling row:", row, "col:", col, "which results in", b)
                list.append(b)
        return list


print("Running add_neighbours")
list = []
init_board = self.board
print("This is out initial board: ", init_board)
board = self.copy()
board.set_board(init_board)
print("It should been copied now:", board.board)



    def bfs_search(self):
        Q = queue.Queue()
        Q.put(self.board)
        print("FIRST NEIGHBOUR LIST")
        list = self.add_neighbours()
        print(list)
        for i in list:
            Q.put(list[i])

        while not Q.empty():
            u = Q.get()
            if self.check_board(u):
                return 1
            else:
                list = u.add_neighbours
                for i in list:
                    Q.put(list[i])

   " Sunday morning"


        def copy(self):
            b = copy.copy(self)
            """depth = self.depth
            board = self.board
            goal = self.goal
            b.set_board(board)
            b.set_goal(goal)"""
            return b


        def set_board(self, board):
            self.board = board


        def set_goal(self, goal):
            self.goal = goal


        def add_neighbours(self):
            b = self.copy()
            list = []
            for row in range(0, 3):
                for col in range(0, 3):
                    next = b.toggle(row, col)
                    print("Toggling row:", row, "col:", col, "from", b.board, "which results in", next.board)
                    list.append(next)


        def bfs_search(self):
            Q = queue.Queue()
            Q.put(self.board)
            while not Q.empty():
                u = Q.get()
                if self.check_board(u):
                    return 1
                else:
                    list = u.add_neighbours
                    for i in list:
                        Q.put(list[i])



