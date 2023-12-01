# gtlbhbjgkrb5sixfivefivetwosix
def calc_sum():
    total = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            a, a_val = float('inf'), ""
            b, b_val = -1, ""

            for i, v in enumerate(line):
                if "0" <= v <= "9" and a == float('inf'):
                    a = i
                    a_val = v
                
                if "0" <= v <= "9":
                    b = i
                    b_val = v

            numbers = {"one": "1", "two": "2", "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
            aa, aa_val = float('inf'), ""
            bb, bb_val = -1, ""
            for num, digit in numbers.items():
                if num in line:
                    l = line.index(num)
                    if l < aa:
                        aa = l
                        aa_val = digit

                    r = line.rindex(num)
                    if r > bb:
                        bb = r
                        bb_val = digit
            
            first = a_val if a < aa else aa_val 
            last =  b_val if b > bb else bb_val

            total += int(first + last)


    return total

if __name__ == "__main__":
    print(calc_sum())
