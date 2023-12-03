from collections import defaultdict
from math import prod

def part1(grid):
    r = len(grid)
    c = len(grid[0])

    total = 0
    yes = False

    num = 0
    for i in range(r):
        if yes:
            total += num

        num = 0
        yes = False
        for j in range(c):
            if not '0' <= grid[i][j] <= '9':
                if yes:
                    total += num

                num = 0
                yes = False

                continue

            else:
                num = num * 10 + int(grid[i][j])

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < r  and 0 <= y < c and (not grid[x][y].isdigit()) and grid[x][y] != ".":
                    yes = True
    
    if yes:
        total += num
    return total

def part2(grid):
    r = len(grid)
    c = len(grid[0])

    gear_dict = defaultdict(set)
    yes = False

    for i in range(r):
        if yes:
            gear_dict[index].add(num)

        num = 0
        yes = False
        for j in range(c):
            if not '0' <= grid[i][j] <= '9':
                if yes:
                    gear_dict[index].add(num)

                num = 0
                yes = False

            else:
                num = num * 10 + int(grid[i][j])

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < r  and 0 <= y < c and grid[x][y] == "*" and grid[i][j].isdigit():
                    index = (x, y)
                    yes = True
    
    if yes:
        gear_dict[index].add(num)

    total = 0
    for v in gear_dict.values():
        if len(v) == 2:
            total += prod(v)

    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        grid = f.read().splitlines()

    with open("sample.txt", "r") as f:
        sample_grid = f.read().splitlines()

    print(part2(grid))
