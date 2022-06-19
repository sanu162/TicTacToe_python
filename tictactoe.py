def board(xs, zs):
    zero = 'X' if xs[0] else ('O' if zs[0] else 0)
    one = 'X' if xs[1] else ('O' if zs[1] else 1)
    two = 'X' if xs[2] else ('O' if zs[2] else 2)
    three = 'X' if xs[3] else ('O' if zs[3] else 3)
    four = 'X' if xs[4] else ('O' if zs[4] else 4)
    five = 'X' if xs[5] else ('O' if zs[5] else 5)
    six = 'X' if xs[6] else ('O' if zs[6] else 6)
    seven = 'X' if xs[7] else ('O' if zs[7] else 7)
    eight = 'X' if xs[8] else ('O' if zs[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")
    print(f"--|---|--")


def sum(a, b, c):
    return a + b + c


def checkwin(xs, zs):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [1, 4, 8], [2, 4, 6]]
    for win in wins:
        if sum(xs[win[0]], xs[win[1]], xs[win[2]]) == 3:
            print("X won the match.")
            return 1
        if sum(zs[win[0]], zs[win[1]], zs[win[2]]) == 3:
            print("O won the match.")
            return 0
    return -1


if __name__ == '__main__':
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1
    print('Welcome to TicTacToe ')
    print("X's chance")
    while True:
        board(xstate, zstate)
        if turn == 1:
            print("X's chance")
            value = int(input("Enter a value: "))
            xstate[value] = 1
        else:
            print("Z's chance")
            value = int(input("Enter a value: "))
            zstate[value] = 1

        cw = checkwin(xstate, zstate)
        if cw != -1:
            print("Match over.")
            break

        turn = 1 - turn
