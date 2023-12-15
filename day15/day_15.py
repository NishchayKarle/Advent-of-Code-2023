def parse_input(data):
    return data[0].split(",")


def hash_this(seq):
    val = 0
    for l in seq:
        val += ord(l)
        val *= 17
        val %= 256

    return val


def part1(data):
    total = 0
    for seq in data:
        total += hash_this(seq)

    return total


def part2(data):
    boxes = [dict() for _ in range(256)]
    for seq in data:
        if seq[-1] == "-":
            label = seq[:-1]
            box = hash_this(label)
            if label in boxes[box]:
                del boxes[box][label]

        else:
            label = seq[:-2]
            fl = int(seq[-1])
            box = hash_this(label)
            boxes[box][label] = fl

    total = 0
    for i in range(256):
        j = 0
        for _, fl in boxes[i].items():
            total += (i + 1) * (j + 1) * fl
            j += 1

    return total


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = parse_input(f.read().splitlines())

    with open("input.txt", "r") as f:
        data = parse_input(f.read().splitlines())

    # print(part1(sample_data))
    # print(part1(data))

    print(part2(sample_data))
    print(part2(data))
