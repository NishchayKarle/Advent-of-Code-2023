from heapq import heappush, heappop


def parse_input(data):
    return [[int(i) for i in row] for row in data]


moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def part1(data):
    m = len(data)
    n = len(data[0])

    pq = [
        (0, 0, 0, 0, 0, 0)
    ]  # heat loss, positionx, positiony, directionx, directiony, streak
    vis = set()

    while pq:
        d, x, y, dirx, diry, s = heappop(pq)

        if (x, y) == (m - 1, n - 1):
            return d

        if (x, y, dirx, diry, s) in vis:
            continue

        vis.add((x, y, dirx, diry, s))

        if s + 1 <= 3 and (dirx, diry) != (0, 0):
            nx, ny = x + dirx, y + diry
            if 0 <= nx < m and 0 <= ny < n:
                heappush(pq, (d + data[nx][ny], nx, ny, dirx, diry, s + 1))

        for dx, dy in moves:
            if (dx, dy) == (dirx, diry) or (dx, dy) == (-dirx, -diry):
                continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                heappush(pq, (d + data[nx][ny], nx, ny, dx, dy, 1))


def part2(data):
    m = len(data)
    n = len(data[0])

    pq = [
        (0, 0, 0, 0, 0, 0)
    ]  # heat loss, positionx, positiony, directionx, directiony, streak
    vis = set()

    while pq:
        d, x, y, dirx, diry, s = heappop(pq)

        if (x, y) == (m - 1, n - 1) and s >= 4:
            return d

        if (x, y, dirx, diry, s) in vis:
            continue

        vis.add((x, y, dirx, diry, s))

        if s + 1 <= 10 and (dirx, diry) != (0, 0):
            nx, ny = x + dirx, y + diry
            if 0 <= nx < m and 0 <= ny < n:
                heappush(pq, (d + data[nx][ny], nx, ny, dirx, diry, s + 1))

        for dx, dy in moves:
            if (dx, dy) == (dirx, diry) or (dx, dy) == (-dirx, -diry):
                continue

            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (s >= 4 or (dirx, diry) == (0, 0)):
                heappush(pq, (d + data[nx][ny], nx, ny, dx, dy, 1))


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = parse_input(f.read().splitlines())

    with open("input.txt", "r") as f:
        data = parse_input(f.read().splitlines())

    print(part1(sample_data))
    print(part1(data))

    print(part2(sample_data))
    print(part2(data))
