# 12R, 13G, 14B

def sum_game_ids():
    total = 0
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            game, cubes = line.split(":")

            game = int(game.split()[1])
            cubes = cubes.split(";")

            for i, v in enumerate(cubes):
                cubes[i] = v.split(",")

            flag = True
            for g in cubes:
                for t in g:
                    _, num, col = t.split(" ")
                    num = int(num)

                    if (col == "blue" and num > 14) or (col == "red" and num > 12) or (col == "green" and num > 13):
                        flag = False
                        break
                    
            total += game if flag else 0

    return total

if __name__ == "__main__":
    print(sum_game_ids())

