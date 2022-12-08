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

# trees from left looking right
for i in range(height):
    visited = set()
    for j in range(width):
        if j == 0 or grid[i][j] > max(visited):
            visible_trees.add((i, j))
        visited.add(grid[i][j])
                
# trees from right looking left
for i in range(height):
    visited = set()
    for j in range(1, width):
        if j==1 or grid[i][-j] > max(visited):
            curr_width = width - j
            visible_trees.add((i, curr_width))
        visited.add(grid[i][curr_width])
                
# trees from top looking down
for j in range(width):
    visited = set()
    for i in range(height):
        if i == 0 or grid[i][j] > max(visited):
            visible_trees.add((i, j))
        visited.add(grid[i][j])

# trees from bottom looking up
for j in range(width):
    visited = set()
    for i in range(1, height):
        curr_height = height - i
        if i == 1 or grid[-i][j] > max(visited):
            visible_trees.add((curr_height, j))
        visited.add(grid[curr_height][j])
            
print(f"P1: {len(visible_trees)}")
    
# show_visible_trees_only(visible_trees)

most_scenic = 0
visible_trees = [(47, 78)]
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
