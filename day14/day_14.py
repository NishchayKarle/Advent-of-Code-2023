def parse_input(data):
    for i, row in enumerate(data):
        data[i] = list(row)

    return data


def part1(data):
    r = len(data)
    c = len(data[0])

    for j in range(c):
        empty = []
        i = 0
        while i < r:
            if i < r and data[i][j] == "#":
                empty = []

            elif i < r and data[i][j] == ".":
                empty.append(i)

            elif i < r and data[i][j] == "O" and empty != []:
                data[empty.pop(0)][j] = "O"
                data[i][j] = "."
                empty.append(i)

            i += 1

    total = 0
    for i, row in enumerate(data):
        c = 0
        for rock in row:
            if rock == "O":
                c += 1

        total += c * (r - i)

    return total


def rotate(arr, r, c):
    for j in range(c):
        empty = []
        for i in range(r):
            if i < r and arr[i][j] == "#":
                empty = []

            elif i < r and arr[i][j] == ".":
                empty.append(i)

            elif i < r and arr[i][j] == "O" and empty != []:
                arr[empty.pop(0)][j] = "O"
                arr[i][j] = "."
                empty.append(i)

    for i in range(r):
        empty = []
        for j in range(c):
            if arr[i][j] == "#":
                empty = []

            elif arr[i][j] == ".":
                empty.append(j)

            elif arr[i][j] == "O" and empty != []:
                arr[i][empty.pop(0)] = "O"
                arr[i][j] = "."
                empty.append(j)

    for j in range(c):
        empty = []
        for i in range(r - 1, -1, -1):
            if i < r and arr[i][j] == "#":
                empty = []

            elif i < r and arr[i][j] == ".":
                empty.append(i)

            elif i < r and arr[i][j] == "O" and empty != []:
                arr[empty.pop(0)][j] = "O"
                arr[i][j] = "."
                empty.append(i)

    for i in range(r):
        empty = []
        for j in range(c - 1, -1, -1):
            if arr[i][j] == "#":
                empty = []

            elif arr[i][j] == ".":
                empty.append(j)

            elif arr[i][j] == "O" and empty != []:
                arr[i][empty.pop(0)] = "O"
                arr[i][j] = "."
                empty.append(j)

    return arr


def convert_to_str(arr):
    str = "".join(["".join(row) for row in arr])
    return str


def part2(data):
    r = len(data)
    c = len(data[0])

    new = []
    for i in range(r):
        arr = []
        for j in range(c):
            arr.append(data[i][j])

        new.append(arr)

    hashmap = {}
    ct = 0
    init, cycle = None, None
    while True:
        data = rotate(data, r, c)
        ct += 1
        string = convert_to_str(data)
        if string in hashmap:
            init, cycle = hashmap[string], ct - hashmap[string]
            break

        else:
            hashmap[string] = ct

    print(init, cycle)
    for _ in range(init + (1000000000 - init) % cycle):
        new = rotate(new, r, c)

    total = 0
    for i, row in enumerate(new):
        c = 0
        for rock in row:
            if rock == "O":
                c += 1

        total += c * (r - i)

    return total


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = parse_input(f.read().splitlines())

    with open("input.txt", "r") as f:
        data = parse_input(f.read().splitlines())

    # print(part1(sample_data))
    # print(part1(data))

    # print(part2(sample_data))
    # print(part2(data))
