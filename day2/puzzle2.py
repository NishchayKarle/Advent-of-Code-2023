import math
def sum_game_ids():
    total = 0
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            _, cubes = line.split(":")

            cubes = cubes.split(";")

            for i, v in enumerate(cubes):
                cubes[i] = v.split(",")

            max_balls = {"red": 0, "blue": 0, "green": 0}
            for g in cubes:
                for t in g:
                    _, num, col = t.split(" ")
                    num = int(num)
                    max_balls[col] = max(max_balls[col], num)

            total += math.prod(max_balls.values())


    return total

if __name__ == "__main__":
    print(sum_game_ids())

