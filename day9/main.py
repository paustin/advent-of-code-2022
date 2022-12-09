from typing import List

class Node:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.positions = []
        self.positions.append((self.x, self.y))
        
    def move_position(self, x=0, y=0):
        self.x += x
        self.y += y
        self.positions.append((self.x, self.y))
        
    def move_direction(self, direction):
            if direction == "R":
                self.move_position(x=1)
            elif direction == "L":
                self.move_position(x=-1)
            elif direction == "U":
                self.move_position(y=1)
            elif direction == "D":
                self.move_position(y=-1)

class Knot(Node):
    def adjacent(self, node) -> bool:
        return abs(self.x - node.x) < 2 and abs(self.y - node.y) < 2
    
    def move_towards(self, node):
        # move in the direction of node
        move_x = 0
        if self.x < node.x:
            move_x += 1
        elif self.x > node.x:
            move_x -= 1
            
        move_y = 0
        if self.y < node.y:
            move_y += 1
        elif self.y > node.y:
            move_y -= 1
        
        self.move_position(move_x, move_y)

with open("input") as f:
    lines = f.readlines()
    
# P1 variables
head1 = Node()
tail = Knot()

# P2 variables
head2: Node = Node()
knots: List[Node] = [head2]
for i in range(9):
    knots.append(Knot())

for line in lines:
    split = line.strip().split(" ")
    dir = split[0]
    num = int(split[1])
    for i in range(num):
        # P1 movements
        head1.move_direction(dir)
        if not tail.adjacent(head1):
            tail.move_towards(head1)

        # P2 movements
        head2.move_direction(dir)
        for i in range(1, 10):
            if not knots[i].adjacent(knots[i - 1]):
                knots[i].move_towards(knots[i - 1])

print(f"P1: {len(set(tail.positions))}")
print(f"P2: {len(set(knots[-1].positions))}")        
