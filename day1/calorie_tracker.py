from heapq import heapify, heappush, heappop

heap = []
heapify(heap)

with open("input", "r") as f:
    cals = 0
    for line in f.readlines():
        if line == '\n':
            heappush(heap, -1 * cals)
            cals = 0
        else:
            cals += int(line)

f = -1 * heappop(heap)
s = -1 * heappop(heap)
t = -1 * heappop(heap)

print(f"First three: {f} {s} {t}")

print(f"First Three Total: {sum([f, s, t])}")
