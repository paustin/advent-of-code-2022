import functools
import json

with open("input") as f:
    lines = f.readlines()
    
class Packet:
    def __init__(self, left, right):
        self.left = json.loads(left)
        self.right = json.loads(right)
        
    def _correct_order(self, left, right):
        # recursive helper function
        try:
            if left < right:
                return -1
            elif left > right:
                return 1
            return 0
        except TypeError:
            # comparing lists and ints is no bueno
            pass
        
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]
        
        i = 0
        while i < len(left) and i < len(right):
            ans = self._correct_order(left[i], right[i])
            if ans:
                return ans
            i += 1
        
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        return 0
        
    def correct_order(self):
        return self._correct_order(self.left, self.right)

        
packets = []
packets2 = []
for i in range(0, len(lines), 3):
    left = lines[i].strip()
    right = lines[i + 1].strip()
    packets.append(Packet(left, right))
    
    packets2.append(left)
    packets2.append(right)
    
sum = 0
for i in range(len(packets)):
    if packets[i].correct_order() < 0:
        sum += (i + 1)
        
print(f"P1: {sum}")

dividers = ["[[2]]", "[[6]]"]

packets2.append(dividers[0])
packets2.append(dividers[1])

def compare(left, right):
    packet = Packet(left, right)
    return packet.correct_order()

sorted_packets2 = sorted(packets2, key=functools.cmp_to_key(compare))

answer = 1
for i in range(len(sorted_packets2)):
    if sorted_packets2[i] in dividers:
        answer *= (i + 1)

print(f"P2: {answer}")
