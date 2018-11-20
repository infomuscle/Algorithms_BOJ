import sys

octal = sys.stdin.readline().rstrip()

decimal = int(octal, 8)

binary = bin(decimal)

print(binary[2:])