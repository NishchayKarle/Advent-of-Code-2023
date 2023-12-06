import sys
from multiprocessing import Pool


def part1(data):
    seeds = list(map(int, data[0].split(": ")[1].split(" ")))

    seed_soil = {}
    idx = 3
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        seed_soil[(s, s + r)] = d
        idx += 1

    soil_fert = {}
    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        soil_fert[(s, s + r)] = d
        idx += 1

    fert_water = {}
    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        fert_water[(s, s + r)] = d
        idx += 1

    water_light = {}
    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        water_light[(s, s + r)] = d
        idx += 1

    light_temp = {}
    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        light_temp[(s, s + r)] = d
        idx += 1

    temp_humd = {}
    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        temp_humd[(s, s + r)] = d
        idx += 1

    humd_loc = {}
    idx += 2
    while idx < len(data) and data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        humd_loc[(s, s + r)] = d
        idx += 1

    min_loc = float("inf")
    for i in range(0, len(seeds), 2):
        s, r = seeds[i], seeds[i + 1]
        for seed in range(s, s + r):
            a = seed
            for key in seed_soil:
                if key[0] <= seed < key[1]:
                    a = seed_soil[key] + (seed - key[0])
            b = a
            for key in soil_fert:
                if key[0] <= a < key[1]:
                    b = soil_fert[key] + (a - key[0])

            c = b
            for key in fert_water:
                if key[0] <= b < key[1]:
                    c = fert_water[key] + (b - key[0])

            d = c
            for key in water_light:
                if key[0] <= c < key[1]:
                    d = water_light[key] + (c - key[0])

            e = d
            for key in light_temp:
                if key[0] <= d < key[1]:
                    e = light_temp[key] + (d - key[0])

            f = e
            for key in temp_humd:
                if key[0] <= e < key[1]:
                    f = temp_humd[key] + (e - key[0])

            g = f
            for key in humd_loc:
                if key[0] <= f < key[1]:
                    g = humd_loc[key] + (f - key[0])

            min_loc = min(min_loc, g)

    print(min_loc)


def search(
    s, r, seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humd, humd_loc
):
    local_min = float("inf")
    for seed in range(s, s + r):
        a = seed
        for key in seed_soil:
            if key[0] <= seed < key[1]:
                a = seed_soil[key] + (seed - key[0])
        b = a
        for key in soil_fert:
            if key[0] <= a < key[1]:
                b = soil_fert[key] + (a - key[0])

        c = b
        for key in fert_water:
            if key[0] <= b < key[1]:
                c = fert_water[key] + (b - key[0])

        d = c
        for key in water_light:
            if key[0] <= c < key[1]:
                d = water_light[key] + (c - key[0])

        e = d
        for key in light_temp:
            if key[0] <= d < key[1]:
                e = light_temp[key] + (d - key[0])

        f = e
        for key in temp_humd:
            if key[0] <= e < key[1]:
                f = temp_humd[key] + (e - key[0])

        g = f
        for key in humd_loc:
            if key[0] <= f < key[1]:
                g = humd_loc[key] + (f - key[0])

        local_min = min(local_min, g)
    return local_min


def part2(data):
    seeds = list(map(int, data[0].split(": ")[1].split(" ")))

    seed_soil = {}
    soil_fert = {}
    fert_water = {}
    water_light = {}
    light_temp = {}
    temp_humd = {}
    humd_loc = {}

    idx = 3
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        seed_soil[(s, s + r)] = d
        idx += 1

    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        soil_fert[(s, s + r)] = d
        idx += 1

    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        fert_water[(s, s + r)] = d
        idx += 1

    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        water_light[(s, s + r)] = d
        idx += 1

    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        light_temp[(s, s + r)] = d
        idx += 1

    idx += 2
    while data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        temp_humd[(s, s + r)] = d
        idx += 1

    idx += 2
    while idx < len(data) and data[idx] != "":
        d, s, r = list(map(int, data[idx].split()))
        humd_loc[(s, s + r)] = d
        idx += 1

    min_loc = float("inf")

    def c(val):
        min_loc = min(min_loc, val)

    # for s, r in [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]:
    #     min_loc = min(
    #         min_loc,
    #         search(
    #             s,
    #             r,
    #             seed_soil,
    #             soil_fert,
    #             fert_water,
    #             water_light,
    #             light_temp,
    #             temp_humd,
    #             humd_loc,
    #         ),
    #     )

    with Pool(150) as pool:
        for g in pool.starmap(
            search,
            [
                (
                    seeds[i],
                    seeds[i + 1],
                    seed_soil,
                    soil_fert,
                    fert_water,
                    water_light,
                    light_temp,
                    temp_humd,
                    humd_loc,
                )
                for i in range(0, len(seeds), 2)
            ],
        ):
            print(g)
            min_loc = min(min_loc, g)

    print(min_loc)


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = f.read().splitlines()

    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    # part1(sample_data)
    # part1(data)

    # part2(sample_data)
    part2(data)
