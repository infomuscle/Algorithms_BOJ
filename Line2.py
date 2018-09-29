#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def wayChecker(before, now):
    if before == "F":
            return now
    elif before == "R":
        if now == "F":
            return "R"
        elif now == "R":
            return "B"
        elif now == "L":
            return "F"
        elif now == "B":
            return "L"
    elif before == "L":
        if now == "F":
            return "L"
        elif now == "R":
            return "F"
        elif now == "L":
            return "B"
        elif now == "B":
            return "R"
    elif before == "B":
        if now == "F":
            return "B"
        elif now == "R":
            return "L"
        elif now == "L":
            return "R"
        elif now == "B":
            return "F"

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())

    board = []
    for i in range(N):
        split = sys.stdin.readline().strip().split(' ')
        board.append(split)

    visited = []
    for i in range(N):
        a = []
        for j in range(N):
            b = []
            a.append(b)
        visited.append(a)

    row, col = 0,0
    before = "B"
    while True:
        visited[row][col].append(board[row][col][0])
        way = wayChecker(before, board[row][col][0])
        if way == "F":
            row -= int(board[row][col][1])
        elif way == "B":
            row += int(board[row][col][1])
        elif way == "L":
            col -= int(board[row][col][1])
        elif way == "R":
            col += int(board[row][col][1])
        before = way
        if board[row][col][0] in visited[row][col]:
            break

    print("%d %d" % (col, row))
