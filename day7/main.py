from heapq import heapify, heappop, heappush

p1_max = 100000
p1_dirs = []
p2_dirs = []
heapify(p2_dirs)

class Dir:
    def __init__(self, parent):
        self.children = {}
        self.parent = parent
        self._size = -1
    
    def size(self):
        if self._size != -1:
            return self._size
        sum = 0
        for item in self.children.values():
            sum += item.size()
        self._size = sum
    
        # Store info for answers
        if self._size <= p1_max:
            p1_dirs.append(self)
        heappush(p2_dirs, self._size)
    
        return sum
        
class Root(Dir):
    def __init__(self):
        super().__init__(self)

class File:
    def __init__(self, size):
        self._size = size
    
    def size(self) -> int:
        return self._size
        
with open("input", "r") as f:
    lines = f.readlines()

root = Root()
current = root

for line in lines[1:]:
    line = line.strip()
    split = line.split(" ")
    if line.startswith("$ cd"):
        cd = split[-1]
        if cd == "..":
            current = current.parent
        else:
            current = current.children[cd]
    elif line == "$ ls":
        # don't need to do anything, but
        # this is easier to check for than a file
        pass
    elif split[0] == "dir":
        dir = split[-1]
        current.children[dir] = Dir(current)
    else:
        size = int(split[0])
        name = split[1]
        current.children[name] = File(size)
        
# sets all dir sizes
root_size = root.size()

p1_total = sum([x.size() for x in p1_dirs])

total_disk_size = 70000000
disk_req = 30000000
disk_avail = total_disk_size - root_size
space_needed = disk_req - disk_avail

p2_dir_size = 0
while not p2_dir_size:
    size = heappop(p2_dirs)
    if size >= space_needed:
        p2_dir_size = size

################################ Print answers ################################
print(f"P1: {p1_total}")
print(f"P2: {p2_dir_size}")
