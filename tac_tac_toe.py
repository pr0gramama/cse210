

def main():

    player = next_turn("")
    grid = make_grid()

    while not (winning_player(grid) or cats_game(grid)):
        game_grid(grid)
        take_turn(player, grid)
        player = next_turn(player)
    game_grid(grid)
    print("Good Game!  Thanks for playing.")


def make_grid():
    grid = []

    for space in range(9):
        grid.append(space + 1)
    return grid


def game_grid(grid):
    print("\n")
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print("-|-|-")
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print("-|-|-")
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")
    print("\n")

# if game is a draw:


def cats_game(grid):
    for space in range(9):
        if grid[space] != "x" and grid[space] != "o":
            return False
    return True


def winning_player(grid):

    # Winning combos
    return (grid[0] == grid[1] == grid[2] or
            grid[3] == grid[4] == grid[5] or
            grid[6] == grid[7] == grid[8] or
            grid[0] == grid[3] == grid[6] or
            grid[1] == grid[4] == grid[7] or
            grid[2] == grid[5] == grid[8] or
            grid[0] == grid[4] == grid[8] or
            grid[2] == grid[4] == grid[6])


def take_turn(player, grid):
    space = int(input(f"{player}'s turn.  Choose a space (1-9): "))
    grid[space-1] = player


def next_turn(value):
    if value == "" or value == "o":
        return "x"
    elif value == "x":
        return "o"


if __name__ == "__main__":
    main()
