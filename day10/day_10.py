import sys

sys.setrecursionlimit(100_000)


def find_loop(data, m, n, total, px, py, x, y, vis):
    if data[x][y] == "S" and px != None:
        return total

    if not data[x][y] == "S":
        vis.add((x, y))

    l = 0
    if data[x][y] == "|":
        if (
            x + 1 < m
            and data[x + 1][y] in {"|", "L", "J", "S"}
            and (x + 1, y) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x + 1, y, vis))

        if (
            0 <= x - 1
            and data[x - 1][y] in {"|", "7", "F", "S"}
            and (x - 1, y) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x - 1, y, vis))

    elif data[x][y] == "-":
        if (
            y + 1 < n
            and data[x][y + 1] in {"-", "7", "J", "S"}
            and (x, y + 1) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x, y + 1, vis))

        if (
            0 <= y - 1
            and data[x][y - 1] in {"-", "L", "F", "S"}
            and (x, y - 1) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x, y - 1, vis))

    elif data[x][y] == "L":
        if (
            y + 1 < n
            and data[x][y + 1] in {"-", "7", "J", "S"}
            and (x, y + 1) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x, y + 1, vis))

        if (
            0 <= x - 1
            and data[x - 1][y] in {"|", "7", "F", "S"}
            and (x - 1, y) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x - 1, y, vis))

    elif data[x][y] == "J":
        if (
            0 <= x - 1
            and data[x - 1][y] in {"|", "7", "F", "S"}
            and (x - 1, y) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x - 1, y, vis))

        if (
            0 <= y - 1
            and data[x][y - 1] in {"-", "L", "F", "S"}
            and (x, y - 1) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x, y - 1, vis))

    elif data[x][y] == "7":
        if (
            x + 1 < m
            and data[x + 1][y] in {"|", "L", "J", "S"}
            and (x + 1, y) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x + 1, y, vis))

        if (
            0 <= y - 1
            and data[x][y - 1] in {"-", "L", "F", "S"}
            and (x, y - 1) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x, y - 1, vis))

    elif data[x][y] == "F":
        if (
            x + 1 < m
            and data[x + 1][y] in {"|", "L", "J", "S"}
            and (x + 1, y) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x + 1, y, vis))

        if (
            y + 1 < n
            and data[x][y + 1] in {"-", "7", "J", "S"}
            and (x, y + 1) not in vis
        ):
            l = max(l, find_loop(data, m, n, total + 1, x, y, x, y + 1, vis))

    elif data[x][y] == "S":
        if x + 1 < m and (x + 1, y) not in vis and data[x + 1][y] != ".":
            l = max(l, find_loop(data, m, n, total + 1, x, y, x + 1, y, vis))

        if 0 <= x - 1 and (x - 1, y) not in vis and data[x - 1][y] != ".":
            l = max(l, find_loop(data, m, n, total + 1, x, y, x - 1, y, vis))

        if y + 1 < n and (x, y + 1) not in vis and data[x][y + 1] != ".":
            l = max(l, find_loop(data, m, n, total + 1, x, y, x, y + 1, vis))

        if 0 <= y - 1 and (x, y - 1) not in vis and data[x][y - 1] != ".":
            l = max(l, find_loop(data, m, n, total + 1, x, y, x, y - 1, vis))

    return l


def part1(data):
    m = len(data)
    n = len(data[0])
    for i, v in enumerate(data):
        for j, w in enumerate(v):
            if w == "S":
                x, y = i, j

    loop = 0
    prev = "."
    vis = set()
    return find_loop(data, m, n, 0, None, None, x, y, vis) // 2


def part2(data):
    m = len(data)
    n = len(data[0])
    for i, v in enumerate(data):
        for j, w in enumerate(v):
            if w == "S":
                x, y = i, j

    loop = 0
    prev = "."
    vis = set()
    find_loop(data, m, n, 0, None, None, x, y, vis)


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = f.read().splitlines()

    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(part1(sample_data))
    print(part1(data))

    # print(part2(sample_data))
    # print(part2(data))
