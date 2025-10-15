import sys
input = sys.stdin.readline

def min_hums(cowphabet: str, heard: str) -> int:
    pos = {}
    for idx, c in enumerate(cowphabet):
        pos[c] = idx
    count = 1
    prev_pos = pos[heard[0]]
    
    for i in range(1, len(heard)):
        cur = heard[i]
        cur_pos = pos[cur]
        if cur_pos <= prev_pos:
            count += 1
        prev_pos = cur_pos
    return count

cowphabet = input().strip()
heard = input().strip()
print(min_hums(cowphabet, heard))
