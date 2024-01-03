import numpy as np
import z3


def parse_input(data):
    hail = []
    for line in data:
        pos, vel = line.split("@")
        x, y, _ = list(map(int, pos.split(",")))
        vx, vy, _ = list(map(int, vel.split(",")))
        hail.append((x, y, vx, vy))

    return hail

def parse_input_2(data):
    hail = []
    for line in data:
        pos, vel = line.split("@")
        x, y, z = list(map(int, pos.split(",")))
        vx, vy, vz = list(map(int, vel.split(",")))
        hail.append(((x, y, z), (vx, vy, vz)))

    return hail


def intersect_lines(x1, y1, vx1, vy1, x2, y2, vx2, vy2, b1, b2):
    m1 = vy1 / vx1
    m2 = vy2 / vx2

    if m1 == m2:
        return False

    # (y - y1) = m (x - x1) -> (m, -1, -m * x1 + y1)
    a = np.array([[m1, -1], [m2, -1]])
    b = np.array([m1 * x1 - y1, m2 * x2 - y2])
    x, y = np.linalg.solve(a, b)
    if (
        abs(x1 + vx1 - x) > abs(x1 - x)
        or abs(x2 + vx2 - x) > abs(x2 - x)
        or abs(y1 + vy1 - y) > abs(y1 - y)
        or abs(y2 + vy2 - y) > abs(y2 - y)
        or not b1 <= x <= b2
        or not b1 <= y <= b2
    ):
        return False

    # print(x1, y1, x2, y2, x, y)
    return True


def intersect_lines_3d(p1, p2):
    # (𝑥,𝑦,𝑧)=(𝑥0,𝑦0,𝑧0)+𝑡(𝑎,𝑏,𝑐)
    pass


def part1(data):
    N = len(data)
    b1, b2 = 200000000000000, 400000000000000
    # b1, b2 = 7, 27

    c = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            x1, y1, vx1, vy1 = data[i]
            x2, y2, vx2, vy2 = data[j]
            if intersect_lines(x1, y1, vx1, vy1, x2, y2, vx2, vy2, b1, b2):
                c += 1

    return c


def part2(data):
    answer = 0

    solver = z3.Solver()
    x, y, z, vx, vy, vz = [z3.Int(var) for var in ["x", "y", "z", "vx", "vy", "vz"]]

    for itx in range(4):
        (cpx, cpy, cpz), (cvx, cvy, cvz) = data[itx]

        t = z3.Int(f"t{itx}")
        solver.add(t >= 0)
        solver.add(x + vx * t == cpx + cvx * t)
        solver.add(y + vy * t == cpy + cvy * t)
        solver.add(z + vz * t == cpz + cvz * t)

    if solver.check() == z3.sat:
        model = solver.model()
        (x, y, z) = (model.eval(x), model.eval(y), model.eval(z))
        answer = x.as_long() + y.as_long() + z.as_long()
    
    return answer


if __name__ == "__main__":
    with open("sample.txt", "r") as f:
        sample_data = parse_input(f.read().splitlines())

    with open("input.txt", "r") as f:
        data = parse_input_2(f.read().splitlines())

    print(part1(sample_data))
    print(part1(data))

    print(part2(sample_data))
    print(part2(data))
