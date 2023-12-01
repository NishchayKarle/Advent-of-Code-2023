def calc_sum():
    total = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            first = ""
            last = ""
            for i in line:
                if '0' <= i <= '9' and first == "":
                    first = i
                
                if '0' <= i <= '9':
                    last = i
            
            total += int(first + last)

    return total

if __name__ == "__main__":
    print(calc_sum())
