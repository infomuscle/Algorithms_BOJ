#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    card = 20000
    split = sys.stdin.readline().strip().split(' ')
    for token in split:
        distance = int(token)
        if distance < 4 or distance > 178:
            sys.stdout.write(str(card))
            break
        else:
            distance -= 40
            card -= 720
            if distance <= 0:
                continue
            else:
                while True:
                    distance -= 8
                    card -= 80
                    if distance <= 0:
                        break
        if card <= 0:
            break
    sys.stdout.write(str(card))