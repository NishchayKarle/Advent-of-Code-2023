from parse import parse
from math import lcm


# AAA = (BBB, CCC)
def part1(data):
    seq = data[0]

    map = {}
    for i in range(2, len(data)):
        p = parse("{} = ({}, {})", data[i])
        map[p[0]] = [p[1], p[2]]

    des = "ZZZ"
    cur = "AAA"
    steps = 0
    while cur != "ZZZ":
        for dir in seq:
            if dir == "L":
                cur = map[cur][0]
            else:
                cur = map[cur][1]

            steps += 1

    return steps


def part2(data):
    seq = data[0]

    map = {}
    for i in range(2, len(data)):
        p = parse("{} = ({}, {})", data[i])
        map[p[0]] = [p[1], p[2]]

    cur_nodes = [node for node in map if node[-1] == "A"]

    steps = 0
    ans = 1
    for cur in cur_nodes:
        steps = 0
        while True:
            for dir in seq:
                steps += 1
                d = 0 if dir == "L" else 1
                cur = map[cur][d]

            if cur[-1] == "Z":
                break

        ans = lcm(ans, steps)

    return ans


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = f.read().splitlines()

    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    # print(part1(sample_data))
    # print(part1(data))

    # print(part2(sample_data))
    print(part2(data))
