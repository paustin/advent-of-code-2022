import string
from typing import List

from dijkstar import Graph, find_path

with open("input") as f:
    lines = f.readlines()
    
class Node:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
    
def char_to_int(char):
    if char == "S":
        return char_to_int("a")
    elif char == "E":
        return char_to_int("z")
    return string.ascii_lowercase.index(char)

grid: List[List[Node]] = []
start = []
end = None
graph = Graph(undirected=True)
for line in lines:
    line = line.strip()
    row = []
    for char in line:
        current_height = len(grid)
        current_width = len(row)
        node = Node(current_height, current_width, char_to_int(char))
        graph.add_node(node)
        if char == "S":
            temp = [node]
            temp.extend(start)
            start = temp
        if char == "a":
            start.append(node)
        if char == "E":
            end = node
        row.append(node)
    grid.append(row)
    
height = len(grid)
width = len(grid[0])

for row in range(height):
    for col in range(width):
        up = row - 1
        down = row + 1
        left = col - 1
        right = col + 1
        current = grid[row][col]
        
        if 0 <= up < height:
            graph.add_edge(current, grid[up][col])
        if 0 <= down < height:
            graph.add_edge(current, grid[down][col])
        if 0 <= left < width:
            graph.add_edge(current, grid[row][left])
        if 0 <= right < width:
            graph.add_edge(current, grid[row][right])
            
def cost_func(u, v, edge, prev_edge):
    if v.value - u.value <= 1:
        return 1
    return 99999999999999999999999999999999
        
path = find_path(graph, start[0], end, cost_func=cost_func)
print(f"P1: {path.total_cost}")

shortest = path.total_cost
for starting_loc in start[1:]:
    path = find_path(graph, starting_loc, end, cost_func=cost_func)
    shortest = min(shortest, path.total_cost)

print(f"P2: {shortest}")
    