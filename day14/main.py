def print_grid(grid):
    if len(grid) < 200:
        row_max, col_min, col_max = 13, 480, 515
    else:
        row_max, col_min, col_max = 170, 330, 670

    for row in range(0, row_max):
        l = []
        for col in range(col_min, col_max):
            l.append(grid.get((col, row), "."))
        print("".join(l))
     
def populate_grid(lines):
    grid = {}
    greatest_height = 0
    for line in lines:
        split = line.strip().split(" -> ")
        for i in range(len(split) - 1):
            curr_split = split[i].split(",")
            current = int(curr_split[0]), int(curr_split[1])
            curr_x, curr_y = current[0], current[1]
            next_split = split[i + 1].split(",")
            next = int(next_split[0]), int(next_split[1])
            next_x, next_y = next[0], next[1]
        
            while (curr_x, curr_y) != (next_x, next_y):
                grid[(curr_x, curr_y)] = "#"
                if curr_x < next_x:
                    curr_x += 1
                elif curr_x > next_x:
                    curr_x -= 1
                elif curr_y < next_y:
                    curr_y += 1
                elif curr_y > next_y:
                    curr_y -= 1
            grid[next] = "#"
            greatest_height = max(greatest_height, curr_y, next_y)
    return grid, greatest_height

with open("input") as f:
    lines = f.readlines()
        
grid, greatest_height = populate_grid(lines)
num_sand = 0
start = 500, 0
curr_x, curr_y = start

while curr_y <= greatest_height:
    dy = curr_y + 1 # down y
    lx = curr_x - 1 # left x
    rx = curr_x + 1 # right x
    if not grid.get((curr_x, dy)):
        curr_y = dy
    elif not grid.get((lx, dy)):
        curr_y = dy
        curr_x = lx
    elif not grid.get((rx, dy)):
        curr_y = dy
        curr_x = rx
    else:
        grid[(curr_x, curr_y)] = "o"
        num_sand += 1
        curr_x, curr_y = start
    
# print_grid(grid)

print(f"P1: {num_sand}")

grid, greatest_height = populate_grid(lines)
num_sand = 0
curr_x, curr_y = start

while True:
    dy = curr_y + 1 # down y
    lx = curr_x - 1 # left x
    rx = curr_x + 1 # right x
    new_grain = False
    
    if curr_y == greatest_height + 1 and not grid.get((curr_x, curr_y)):
        new_grain = True
    elif not grid.get((curr_x, dy)):
        curr_y = dy
    elif not grid.get((lx, dy)):
        curr_y = dy
        curr_x = lx
    elif not grid.get((rx, dy)):
        curr_y = dy
        curr_x = rx
    else:
        new_grain = True

    if new_grain:
        grid[(curr_x, curr_y)] = "o"
        num_sand += 1
        curr_x, curr_y = start
        if grid.get((curr_x, curr_y)):
            break

# print_grid(grid)

print(f"P2: {num_sand}")