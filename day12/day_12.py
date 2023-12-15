from functools import cache


def parse_input(data):
    r = []
    for row in data:
        pattern, nums = row.split()
        nums = list(map(int, nums.split(",")))
        r.append([pattern, nums])

    return r


def calc(pattern, nums):
    @cache
    def f(pindex, nindex, left):
        if pindex == len(pattern):
            if nindex == len(nums) - 1 and left == 0:
                return 1

            return 0

        if nindex >= len(nums):
            return 0

        c = 0
        if pattern[pindex] == ".":
            # cannot be at this point without having completed the sequence
            if left == 0:
                if nindex + 1 != len(nums):
                    # next point in the pattern could be '?' or '#'. Need to start new sequence
                    c += f(pindex + 1, nindex + 1, nums[nindex + 1])

                # next point in the pattern could be '.' as well. No need to start new sequence
                c += f(pindex + 1, nindex, 0)

        # continue current sequence by count this '#'
        elif pattern[pindex] == "#":
            if left != 0:
                c += f(pindex + 1, nindex, left - 1)

        else:
            # current sequence is finished, ignore this '?'
            if left == 0:
                if nindex + 1 != len(nums):
                    # next sequence could start from the next point - '?' or '#'
                    c += f(pindex + 1, nindex + 1, nums[nindex + 1])

                # next sequence may not start from the next point - '.' or '?'
                c += f(pindex + 1, nindex, 0)

            # current sequence is not finished. hanlde this'?' as '#'
            else:
                c += f(pindex + 1, nindex, left - 1)

        return c

    return f(0, 0, 0)


def part1(data):
    total = 0
    for pattern, nums in data:
        total += calc("." + pattern, [0] + nums)

    return total


def part2(data):
    total = 0
    for pattern, nums in data:
        total += calc("." + "?".join([pattern] * 5), [0] + nums * 5)

    return total


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = parse_input(f.read().splitlines())

    with open("input.txt", "r") as f:
        data = parse_input(f.read().splitlines())

    print(part1(sample_data))
    print(part1(data))

    print(part2(sample_data))
    print(part2(data))
