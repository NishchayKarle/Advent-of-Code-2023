from collections import deque
import sys

sys.setrecursionlimit(100_000)


def parse_input(data):
    return data


def part1(data):
    R = len(data)
    C = len(data[0])
    sx, sy = 0, 1

    vis = [[False] * C for _ in range(R)]
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    slopes = "^v><"

    longest = 0

    def dfs(x, y, d):
        if x == R - 1 and y == C - 2:
            nonlocal longest
            if d > longest:
                longest = d

            return

        if data[x][y] != ".":
            dir = [directions[slopes.index(data[x][y])]]

        else:
            dir = directions

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not vis[nx][ny] and data[nx][ny] != "#":
                vis[nx][ny] = True
                dfs(nx, ny, d + 1)
                vis[nx][ny] = False

    dfs(sx, sy, 0)
    return longest


def part2(data):
    R = len(data)
    C = len(data[0])

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    points = {(0, 1), (R - 1, C - 2)}
    for x in range(R):
        for y in range(C):
            if data[x][y] == "#":
                continue

            c = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and data[nx][ny] != "#":
                    c += 1

            if c > 2:
                points.add((x, y))

    graph = {pt: {} for pt in points}
    for sx, sy in points:
        seen = set((sx, sy))
        stack = [(sx, sy, 0)]

        while stack:
            x, y, d = stack.pop()
            if d != 0 and (x, y) in points:
                graph[(sx, sy)][(x, y)] = d
                continue

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < R
                    and 0 <= ny < C
                    and data[nx][ny] != "#"
                    and (nx, ny) not in seen
                ):
                    stack.append((nx, ny, d + 1))
                    seen.add((nx, ny))

    seen = set()
    best = 0

    def dfs(x, y, d):
        nonlocal best
        if x == R - 1 and y == C - 2:
            if d > best:
                print(d)
                best = d
            return

        seen.add((x, y))
        for nx, ny in graph[(x, y)]:
            if (nx, ny) not in seen:
                dfs(nx, ny, d + graph[(x, y)][(nx, ny)])
        seen.remove((x, y))

    dfs(0, 1, 0)
    return best


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = parse_input(f.read().splitlines())

    with open("input.txt", "r") as f:
        data = parse_input(f.read().splitlines())

    print(part1(sample_data))
    print(part1(data))

    print(part2(sample_data))
    print(part2(data))
