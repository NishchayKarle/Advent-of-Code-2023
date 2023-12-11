def part1(data):
    empty_rows = set()
    empty_cols = set()

    for i, row in enumerate(data):
        if "#" not in row:
            empty_rows.add(i)

    for j in range(len(data[0])):
        if "#" not in [data[i][j] for i in range(len(data))]:
            empty_cols.add(j)

    count = 0
    for row in sorted(empty_rows):
        r = row + count
        data.insert(r, "." * len(data[0]))
        count += 1

    empty_cols = sorted(empty_cols)
    count = 0
    for i in range(len(data)):
        count = 0
        for col in empty_cols:
            c = col + count
            data[i] = data[i][:c] + "." + data[i][c:]
            count += 1

    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                galaxies.append((i, j))

    total = 0
    galaxies.sort()
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            dist = abs(galaxies[i][0] - galaxies[j][0]) + abs(
                galaxies[i][1] - galaxies[j][1]
            )
            total += dist

    return total


def part2(data):
    empty_rows = set()
    empty_cols = set()

    for i, row in enumerate(data):
        if "#" not in row:
            empty_rows.add(i)

    for j in range(len(data[0])):
        if "#" not in [data[i][j] for i in range(len(data))]:
            empty_cols.add(j)

    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "#":
                galaxies.append((i, j))

    empty_rows = sorted(empty_rows)
    empty_cols = sorted(empty_cols)
    total = 0
    galaxies.sort()
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            rows = 0
            cols = 0
            for row in empty_rows:
                if (
                    galaxies[i][0] < row < galaxies[j][0]
                    or galaxies[j][0] < row < galaxies[i][0]
                ):
                    rows += 1

            for col in empty_cols:
                if (
                    galaxies[i][1] < col < galaxies[j][1]
                    or galaxies[j][1] < col < galaxies[i][1]
                ):
                    cols += 1
            dist = (
                abs(galaxies[i][0] - galaxies[j][0])
                + abs(galaxies[i][1] - galaxies[j][1])
                + rows * (1000000 - 1)
                + cols * (1000000 - 1)
            )
            total += dist

    return total


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = f.read().splitlines()

    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    # print(part1(sample_data))
    # print(part1(data))

    # print(part2(sample_data))
    # print(part2(data))
