#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Imports.
from __future__ import annotations
from functools import reduce
# * ─── Read Input.
def read_input(filepath, raw=False):
    with open(filepath, "r") as f:
        if raw:
            return f.read()

        return f.read().splitlines()


# * ─── Get Trees.
def get_trees(grid: list[str], row: int, col: int, reverse: bool = False) -> list[list]:
    rows = [x[col] for x in grid]
    cols = list(grid[row])

    top, bottom = rows[:row], rows[row + 1 :]
    left, right = cols[:col], cols[col + 1 :]

    if reverse:
        return reversed(top), bottom, reversed(left), right
    return top, bottom, left, right


# * ─── Is Visible.
def is_visible(grid: list[str], row: int, col: int) -> bool:
    tree = grid[row][col]

    for direction in get_trees(grid, row, col):
        if all(x < tree for x in direction):
            return True

    return False


# * ─── Count Views.
def count_views(grid: list[str], row: int, col: int) -> int:
    score = []
    tree = grid[row][col]

    for direction in get_trees(grid, row, col, reverse=True):
        count = 0
        for x in direction:
            count += 1
            if tree <= x:
                break

        score.append(count)

    return reduce(lambda x, y: x * y, score)


# * ─── Part One.
def part_one(lines: list[str]):
    borders = len(lines) * 2 + len(lines[0]) * 2  # Height x Width x 2 (both sides)
    borders = borders - 4  # Remove Double Corners.
    count = 0 + borders

    for row, line in enumerate(lines[1 : len(lines) - 1], 1):
        for col, _ in enumerate(line[1 : len(line) - 1], 1):
            if is_visible(lines, row, col):
                count += 1

    return count


# * ─── Part Two.
def part_two(lines: list[str]):
    scenic_score = float("-inf")

    for row, line in enumerate(lines[1 : len(lines) - 1], 1):
        for col, _ in enumerate(line[1 : len(line) - 1], 1):
            count = count_views(lines, row, col)
            scenic_score = max(count, scenic_score)

    return scenic_score


# * ─── Main.
if __name__ == "__main__":
    lines = read_input("./test.txt")

    # • Part One.
    result = part_one(lines)
    print(f"Part One: {result}.")

    # • Part Two.
    result = part_two(lines)
    print(f"Part Two: {result}.")

