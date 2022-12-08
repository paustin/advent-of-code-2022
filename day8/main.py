with open("input") as f:
    lines = f.readlines()
    
def show_visible_trees_only(visible=set(), null_char='-'):
    for i in range(height):
        display = []
        for j in range(len(grid[0])):
            if (i, j) in visible:
                display.append(grid[i][j])
            else:
                display.append(null_char)
        print("".join(display))

grid = []

for line in lines:
    line = line.strip()
    grid.append(list(line))

height = len(grid)
width = len(grid[0])
visible_trees = set()

# trees from the sides
for i in range(height):
    visited_l = set()
    visited_r = set()
    for j in range(width):
        if j == 0 or grid[i][j] > max(visited_l):
            visible_trees.add((i, j))
        visited_l.add(grid[i][j])
        if j:
            if j == 1 or grid[i][-j] > max(visited_r):
                curr_width = width - j
                visible_trees.add((i, curr_width))
            visited_r.add(grid[i][curr_width])
                
# trees from top and bottom
for j in range(width):
    visited_a = set()
    visited_b = set()
    for i in range(height):
        if i == 0 or grid[i][j] > max(visited_a):
            visible_trees.add((i, j))
        visited_a.add(grid[i][j])
        if i:
            curr_height = height - i
            if i ==1 or grid[-i][j] > max(visited_b):
                visible_trees.add((curr_height, j))
            visited_b.add((grid[curr_height][j]))
            
print(f"P1: {len(visible_trees)}")
    
# show_visible_trees_only(visible_trees)

most_scenic = 0
for i, j in visible_trees:
    tree = grid[i][j]
    tree_score = 1
    
    # check left of tree
    current = 1
    for dist in range(1, j):
        if grid[i][j - dist] <= tree:
            current = dist
        if grid[i][j - dist] >= tree:
            break
    tree_score = current
    
    # check right of tree
    current = 1
    for dist in range(1, width - j):
        if grid[i][j + dist] <= tree:
            current = dist
        if grid[i][j + dist] >= tree:
            break
    tree_score *= current

    # check above tree
    current = 1
    for dist in range(1, i + 1):
        if grid[i - dist][j] <= tree:
            current = dist
        if grid[i - dist][j] >= tree:
            break
    tree_score *= current

    # check below tree
    current = 1
    for dist in range(1, height - i):
        if grid[i + dist][j] <= tree:
            current = dist
        if grid[i + dist][j] >= tree:
            break
    tree_score *= current

    most_scenic = max(most_scenic, tree_score)

print(f"P2: {most_scenic}")
