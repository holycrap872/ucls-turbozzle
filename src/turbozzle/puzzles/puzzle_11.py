#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right, wait_until_exit


def make_tree(f: int) -> None:
    if f == 0:
        return

    for i in range(f):
        forward()

    left(90)
    make_tree(f - 1)
    right(180)
    make_tree(f - 1)
    right(90)

    for i in range(f):
        forward()
    right(180)


def solve_puzzle_11() -> None:
    make_tree(4)
    right(180)
    make_tree(4)


init_puzzle("levels/puzzle_11.png", x=-0, y=0, speed=0)
solve_puzzle_11()

wait_until_exit()
