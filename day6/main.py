with open("input", "r") as f:
    line = f.readline().strip()

def find_n_unique(line, num):
    for i in range(len(line) - num):
        current = line[i: i + num]
        if len(set(current)) == num:
            return i + num
        
print(f"P1: {find_n_unique(line, 4)}")
print(f"P2: {find_n_unique(line, 14)}")

import re

def build_regex(num):
    neg_la = r"(?!\1)"
    reg = f"(.){neg_la}"
    for i in range(num - 1):
        i += 2
        if i < num:
            neg_la = neg_la.replace(")", rf"|\{i})")
        else:
            neg_la = ""
        reg = f"{reg}(.){neg_la}"
    return reg

def find_n_unique2(line, num):
    reg = build_regex(num)
    s = "".join(re.search(reg, line).groups())
    return line.index(s) + num

print("Regex version:")

print(f"P1: {find_n_unique2(line, 4)}")
# regex: (.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3)(.)

print(f"P1: {find_n_unique2(line, 14)}")
# regex is 364 characters long:
# (.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3)(.)(?!\1|\2|\3|\4)(.)(?!\1|\2|\3|\4|\5)(.)(?!\1|\2|\3|\4|\5|\6)(.)(?!\1|\2|\3|\4|\5|\6|\7)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11|\12)(.)(?!\1|\2|\3|\4|\5|\6|\7|\8|\9|\10|\11|\12|\13)(.)
