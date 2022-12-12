import string
from typing import List, Tuple

from dijkstar import Graph, find_path

with open("input") as f:
    lines = f.readlines()
    
def char_to_int(char):
    if char == "S":
        return char_to_int("a")
    elif char == "E":
        return char_to_int("z")
    return string.ascii_lowercase.index(char)

grid: List[List[Tuple[int, int, int]]] = []
start = []
end = None
graph = Graph(undirected=True)
for line in lines:
    line = line.strip()
    row = []
    for char in line:
        current_height = len(grid)
        current_width = len(row)
        node = (current_height, current_width, char_to_int(char))
        graph.add_node(node)
        if char == "S":
            temp = [node]
            temp.extend(start)
            start = temp
        if char == "a":
            start.append(node)
        if char == "E":
            end = node
        
        # Add up and left edges
        if current_height > 0:
            up = grid[current_height - 1][current_width]
            graph.add_edge(node, (current_height - 1, current_width, up[2]))
        if current_width > 0:
            left = row[-1]
            graph.add_edge(node, (current_height, current_width - 1, left[2]))
        
        row.append(node)
    grid.append(row)
    
height = len(grid)
width = len(grid[0])
            
def cost_func(u, v, edge, prev_edge):
    if v[2] - u[2] <= 1:
        return 1
    return 99999999999999999999999999999999
        
path = find_path(graph, start[0], end, cost_func=cost_func)
print(f"P1: {path.total_cost}")

shortest = path.total_cost
for starting_loc in start[1:]:
    path = find_path(graph, starting_loc, end, cost_func=cost_func)
    shortest = min(shortest, path.total_cost)

print(f"P2: {shortest}")
    