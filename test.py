import sys

N = int(sys.stdin.readline().strip())

board = []
for i in range(N):
    split = sys.stdin.readline().strip().split(' ')
    board.append(split)
print(board)