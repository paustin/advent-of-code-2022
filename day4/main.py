
p1_total = 0
p2_total = 0
with open("input", "r") as f:
    for line in f.readlines():
        line = line.strip()
        ranges = line.split(",")
        first = [int(x) for x in ranges[0].split("-")]
        second = [int(x) for x in ranges[1].split("-")]
        if (
            (first[0] <= second[0] and first[1] >= second[1]) or
            (first[0] >= second[0] and first[1] <= second[1])
        ):
            p1_total += 1
            
        if (
            second[0] <= first[0] <= second[1] or 
            second[0] <= first[1] <= second[1] or 
            first[0] <= second[0] <= first[1] or 
            first[0] <= second[1] <= first[1]
        ):
            p2_total += 1
            
print(f"P1 Total: {p1_total}")
print(f"P2 Total: {p2_total}")
