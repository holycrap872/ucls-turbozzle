#!/usr/bin/env python3
from turbozzle.utils.movement_wrapper import forward, init_puzzle, left, on_red, right, wait_until_exit


def solve_puzzle_08() -> None:
    "YOUR CODE HERE"


init_puzzle("levels/puzzle_08.png", x="MUST_REPLACE", y="MUST_REPLACE", speed=0)
solve_puzzle_08()

wait_until_exit()
