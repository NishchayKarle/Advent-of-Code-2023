from collections import defaultdict


def part1(data):
    total = 0
    for card in data:
        _, rest = card.split(":")
        winners, curr = rest.split("|")
        winners = {int(i) for i in winners.split() if i.isdigit()}
        curr = {int(i) for i in curr.split() if i.isdigit()}
        n = len(winners.intersection(curr))
        if n != 0:
            total += 2 ** (n - 1)

    return total


def part2(data):
    cards = defaultdict(int)

    for i, card in enumerate(data):
        cards[i] += 1
        _, rest = card.split(":")
        winners, curr = rest.split("|")
        winners = {int(i) for i in winners.split() if i.isdigit()}
        curr = {int(i) for i in curr.split() if i.isdigit()}
        n = len(winners.intersection(curr))
        for j in range(i + 1, i + n + 1):
            cards[j] += cards[i]

    return sum(cards.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    with open("sample.txt", "r") as f:
        sample_data = f.read().splitlines()

    print(part2(data))
