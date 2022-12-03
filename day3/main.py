
def letter_priority(letter):
    indexes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return indexes.index(letter) + 1

def find_dup(items):
    half = int(len(items) / 2)
    for i in items[:int(half)]:
        if i in items[int(half):]:
            return i

sum = 0
with open("input", "r") as f:
    for line in f.readlines():
        items = line.strip()
        sum += letter_priority(find_dup(items))
                
print(f"Part1: {sum}")

def find_dup2(first, second, third):
    for item in first:
        if item in second and item in third:
            return item

sum = 0
with open("input", "r") as f:
    lines = f.readlines()
    while lines:
        first = lines.pop()
        second = lines.pop()
        third = lines.pop()
        
        sum += letter_priority(find_dup2(first, second, third))
        
print(f"Part2: {sum}")
        