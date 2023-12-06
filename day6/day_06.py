def part1(time, distance):
    total = 1
    for i, t in enumerate(time):
        count = 0
        l = 0
        r = t
        while l < r:
            mid = l + (r - l) // 2
            if (t - mid) * mid > distance[i]:
                r = mid

            else:
                l = mid + 1

        count -= r

        l = 0
        r = t
        while l < r:
            mid = l + (r - l) // 2
            if (t - mid) * mid > distance[i]:
                l = mid + 1

            else:
                r = mid

        count += l
        total *= count

    return total


def part2(time, distance):
    count = 0
    l = 0
    r = time
    while l < r:
        mid = l + (r - l) // 2
        if (time - mid) * mid > distance:
            r = mid

        else:
            l = mid + 1

    count -= r

    l = 0
    r = time
    while l < r:
        mid = l + (r - l) // 2
        if (time - mid) * mid > distance:
            l = mid + 1

        else:
            r = mid

    count += l

    return count


if __name__ == "__main__":
    time = 71530
    distance = 940200

    time = 34908986
    distance = 204171312101780

    print(part2(time, distance))
