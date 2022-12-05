import re
from typing import List, Tuple

def read_starting_pos(lines: List[str]) -> List[List[str]]:
    crates_regex = r"^.(.). .(.). .(.). .(.). .(.). .(.). .(.). .(.). .(.).$" # cause lol
    crates = [[], [], [], [], [], [], [], [], []]
    for line in lines:
        matches = re.search(crates_regex, line)
        for j in range(9):
            group = matches.group(j + 1).strip()
            if group:
                temp = [group]
                temp.extend(crates[j])
                crates[j] = temp
    return crates

def read_move(line: str) -> Tuple[int, int, int]:
    moves_regex = r"^move (\d+) from (\d+) to (\d+)"
    matches = re.search(moves_regex, line)
    m_num = int(matches.group(1))
    m_from = int(matches.group(2)) - 1
    m_to = int(matches.group(3)) - 1
    
    return m_num, m_from, m_to
    
def move_crates_p1(lines: List[str], crates: List[List[str]]) -> List[List[str]]:
    for line in lines:
        m_num, m_from, m_to = read_move(line)
        for _ in range(m_num):
            moving = crates[m_from].pop()
            crates[m_to].append(moving)
    
    return crates

def move_crates_p2(lines: List[str], crates: List[List[str]]) -> List[List[str]]:
    for line in lines:
        m_num, m_from, m_to = read_move(line)
        m_num = m_num * -1 # ease of use for array indexes

        moving = crates[m_from][m_num:]
        crates[m_from] = crates[m_from][:m_num]
            
        crates[m_to].extend(moving)
    
    return crates
            
with open("input", "r") as f:
    lines = f.readlines()

crates1 = read_starting_pos(lines[:8])
crates1 = move_crates_p1(lines[10:], crates1)

crates2 = read_starting_pos(lines[:8])
crates2 = move_crates_p2(lines[10:], crates2)

print(f"P1: {[crate[-1] for crate in crates1]}")
print(f"P2: {[crate[-1] for crate in crates2]}")
