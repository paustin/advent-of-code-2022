with open("input") as f:
    lines = f.readlines()
    
class Info:
    def __init__(self):
        self.register = 1
        self.cycle = 0
        self.signal_strength = 0
        self.pixels = [[], [], [], [], [], [], []]
        
    def bump_cycle(self):
        row = self.cycle // 40
        pixel = "."
        diff = (self.register % 40) - (self.cycle % 40)
        if abs(diff) < 2 or 40 - diff < 2:
            pixel = "#"
        self.pixels[row].append(pixel)
        
        self.cycle += 1
        if (self.cycle - 20) % 40 == 0:
            self.signal_strength += (self.register * self.cycle)

info = Info()

for line in lines:
    split = line.strip().split(" ")
    if split[0] == "noop":
        info.bump_cycle()
    else:
        num = int(split[1])
        info.bump_cycle()
        info.bump_cycle()
        info.register += num
    
print(f"P1: {info.signal_strength}")

print(f"P2:")
for row in info.pixels:
    print("".join(row))