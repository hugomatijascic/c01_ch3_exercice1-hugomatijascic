#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def square_root(number: int) -> float:
    # TODO completer la fonction
    return math.sqrt(number)


def square(number: int) -> int:
    # TODO completer la fonction
    return math.pow(number, 2)


def main() -> None:
    for i in range(25):
        print(f"Square root: {square_root(i)}, square: {square(i)}")


if __name__ == '__main__':
    main()
