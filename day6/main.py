with open("input", "r") as f:
    line = f.readline().strip()

def find_n_unique(line, num):
    for i in range(len(line) - num):
        current = line[i: i + num]
        if len(set(current)) == num:
            return i + num
        
print(f"P1: {find_n_unique(line, 4)}")

print(f"P2: {find_n_unique(line, 14)}")
