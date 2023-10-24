class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.status = "ongoing"
        self.turns = 0
        self.winning_combinations = self.generate_winning_combinations()

    @staticmethod
    def generate_winning_combinations():
        """Generate all winning combinations for a 3x3 board."""
        rows = [[(i, j) for j in range(3)] for i in range(3)]
        cols = [[(i, j) for i in range(3)] for j in range(3)]
        diags = [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
        return rows + cols + diags

    def display_board(self):
        """Display the current game board."""
        for row in self.board:
            print("|", end="")
            for cell in row:
                print(f" {cell if cell else ' '} |", end="")
            print("\n" + "-" * 13)

    def check_win(self):
        """Check if the current player has won the game."""
        for combo in self.winning_combinations:
            if self.board[combo[0][0]][combo[0][1]] == \
                    self.board[combo[1][0]][combo[1][1]] == \
                    self.board[combo[2][0]][combo[2][1]] != '':
                return True
        return False

    def check_tie(self):
        """Check if the game is a tie."""
        return all(self.board[i][j] for i in range(3) for j in range(3)) and not self.check_win()

    def valid_move(self, x, y):
        """Check if a move is valid."""
        return 0 <= x < 3 and 0 <= y < 3 and not self.board[x][y]

    def player_move(self, x, y):
        """Player makes a move on the board."""

        if self.valid_move(x, y):
            self.board[x][y] = self.current_player
            self.turns += 1
            return True
        return False

    # Rest of your methods remain unchanged

    def play_with_users(self):
        """Play the game with two users."""
        print("Welcome to Tic Tac Toe!")
        while True:
            self.display_board()
            print(f"Player {self.current_player}'s turn!")
            try:
                x, y = map(int, input("Enter row and column (comma separated): ").split(","))
                if not self.player_move(x, y):
                    print("Invalid input. Please enter numbers separated by a comma.")
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers separated by a comma.")
                continue

            if self.check_win():
                self.display_board()
                print(f"Player {self.current_player} wins!")
                break
            elif self.check_tie():
                self.display_board()
                print("It's a tie!")
                break

            self.current_player = "O" if self.current_player == "X" else "X"

    print("Thanks for playing!")


# Play the game with two users
tic = TicTacToe()
tic.play_with_users()
