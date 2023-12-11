def calc(arr):
    flag = True
    for i in range(1, len(arr)):
        if arr[i] != arr[0]:
            flag = False
            break

    if flag:
        return arr[0]

    diff = []
    for i in range(1, len(arr)):
        diff.append(arr[i] - arr[i - 1])

    return arr[-1] + calc(diff)


def calc2(arr):
    flag = True
    for i in range(1, len(arr)):
        if arr[i] != arr[0]:
            flag = False
            break

    if flag:
        return arr[0]

    diff = []
    for i in range(1, len(arr)):
        diff.append(arr[i] - arr[i - 1])

    return arr[0] - calc2(diff)


def part1(data):
    total = 0
    for arr in data:
        total += calc(list(map(int, arr.split())))

    return total


def part2(data):
    total = 0
    for arr in data:
        total += calc2(list(map(int, arr.split())))

    return total


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = f.read().splitlines()

    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    # print(part1(sample_data))
    # print(part1(data))

    print(part2(sample_data))
    print(part2(data))
