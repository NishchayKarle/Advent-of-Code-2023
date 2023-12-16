import sys

sys.setrecursionlimit(1000000)


def parse_input(data):
    return data


moves = {
    ".": {"R": ["R"], "L": ["L"], "U": ["U"], "D": ["D"]},
    "-": {"R": ["R"], "L": ["L"], "U": ["L", "R"], "D": ["R", "L"]},
    "|": {"R": ["U", "D"], "L": ["D", "U"], "U": ["U"], "D": ["D"]},
    "\\": {"R": ["D"], "L": ["U"], "U": ["L"], "D": ["R"]},
    "/": {"R": ["U"], "L": ["D"], "U": ["R"], "D": ["L"]},
}


def dfs(m, n, x, y, d, data):
    vis = set()

    def f(x, y, d):
        if not (0 <= x < m) or not (0 <= y < n):
            return

        if (x, y, d) in vis:
            return

        # Key: add direction to visited along with (x, y)
        # Since, the path traversed would only be repeated if direction was the same at x, y
        vis.add((x, y, d))

        for new_d in moves[data[x][y]][d]:
            if new_d == "R":
                dx, dy = 0, 1

            elif new_d == "L":
                dx, dy = 0, -1

            elif new_d == "U":
                dx, dy = -1, 0

            else:
                dx, dy = 1, 0

            f(x + dx, y + dy, new_d)

    f(x, y, d)
    return len(set((i, j) for i, j, _ in vis))


def part1(data):
    m, n = len(data), len(data[0])
    return dfs(m, n, 0, 0, "R", data)


def part2(data):
    m, n = len(data), len(data[0])
    max_illum = 0
    for x, y, d in (
        [(0, j, "D") for j in range(n)]
        + [(m - 1, j, "U") for j in range(n)]
        + [(i, 0, "R") for i in range(m)]
        + [(i, n - 1, "L") for i in range(m)]
    ):
        max_illum = max(max_illum, dfs(m, n, x, y, d, data))

    return max_illum


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = parse_input(f.read().splitlines())

    with open("input.txt", "r") as f:
        data = parse_input(f.read().splitlines())

    print(part1(sample_data))
    print(part1(data))

    print(part2(sample_data))
    print(part2(data))
