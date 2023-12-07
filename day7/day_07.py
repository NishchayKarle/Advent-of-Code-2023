from collections import Counter

strength = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}


def check1(hand):
    count = Counter(hand)

    max_val = max(count.values())
    min_val = min(count.values())

    if max_val == 5:
        return "five"

    if max_val == 4:
        return "four"

    if max_val == 3:
        if min_val == 2:
            return "full"
        return "three"

    if max_val == 2:
        count2 = Counter(count.values())
        if count2[2] == 2:
            return "two"

        return "pair"

    return "high"


def check2(hand):
    if "J" in hand:
        j = hand.count("J")

        hand_n_j = "".join(i for i in hand if i != "J")
        count = Counter(hand_n_j)

        if j == 5:
            return "five"

        max_val = max(count.values())
        min_val = min(count.values())

        if max_val + j == 5:
            return "five"

        if max_val + j == 4:
            return "four"

        if max_val + j == 3:
            if min_val == 2:
                return "full"

            else:
                return "three"

        return "pair"

    count = Counter(hand)

    max_val = max(count.values())
    min_val = min(count.values())

    if max_val == 5:
        return "five"

    if max_val == 4:
        return "four"

    if max_val == 3:
        if min_val == 2:
            return "full"
        return "three"

    if max_val == 2:
        count2 = Counter(count.values())
        if count2[2] == 2:
            return "two"

        return "pair"

    return "high"


def part1(data):
    hands = {}

    for line in data:
        hs, bid = line.split()
        hands[hs] = int(bid)

    order = {
        "five": [],
        "four": [],
        "full": [],
        "three": [],
        "two": [],
        "pair": [],
        "high": [],
    }
    for hs in hands:
        order[check1(hs)].append(hs)

    for key, hs in order.items():
        order[key] = sorted(
            hs,
            key=lambda word: [strength[c] if c in strength else int(c) for c in word],
            reverse=True,
        )

    rank = len(hands)
    total = 0
    for key, hs in order.items():
        for h in hs:
            total += hands[h] * rank
            rank -= 1

    return total


def part2(data):
    hands = {}

    for line in data:
        hs, bid = line.split()
        hands[hs] = int(bid)

    order = {
        "five": [],
        "four": [],
        "full": [],
        "three": [],
        "two": [],
        "pair": [],
        "high": [],
    }
    for h in hands:
        order[check2(h)].append(h)

    for key, hs in order.items():
        order[key] = sorted(
            hs,
            key=lambda word: [strength[c] if c in strength else int(c) for c in word],
            reverse=True,
        )

    rank = len(hands)
    total = 0
    for key, hs in order.items():
        for h in hs:
            total += hands[h] * rank
            rank -= 1

    return total


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = f.read().splitlines()

    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    print(part1(sample_data))
    print(part1(data))

    print(part2(sample_data))
    print(part2(data))
