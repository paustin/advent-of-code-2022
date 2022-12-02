
def get_the_info_i_need(opp, c2):
    # returns (game_score_part1, determine_sign)
    d = {
        "A": {
            "X": (3, 'Z'),
            "Y": (6, 'X'),
            "Z": (0, 'Y')
        },
        "B": {
            "X": (0, 'X'),
            "Y": (3, 'Y'),
            "Z": (6, 'Z')
        },
        "C": {
            "X": (6, 'Y'),
            "Y": (0, 'Z'),
            "Z": (3, 'X')
        }
    }
    return d[opp][c2]

def sign_score(me):
    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    return scores[me]
    
def result_score(result):
    scores = {
        "Z": 6,
        "X": 0,
        "Y": 3
    }
    return scores[result]

part1_total = 0
part2_total = 0
with open("input", "r") as f:
    for line in f.readlines():
        choices = line.strip().split(" ")
        opp = choices[0]
        c2 = choices[1]
        p1_score, determined = get_the_info_i_need(opp, c2)
        
        part1_total += p1_score
        part1_total += sign_score(c2)
        
        part2_total += result_score(c2)
        part2_total += sign_score(determined)
        
print(f"Part 1 Total Score: {part1_total}")

print(f"Part 2 Total Score: {part2_total}")
