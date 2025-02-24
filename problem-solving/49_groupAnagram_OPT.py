from collections import defaultdict
strs=['eat','tea','tan','ate','nat','bat']

result=defaultdict(list)
# creates a dictionary with each key having value as a empty list

for s in strs:
    count=[0]*26
    for c in s:
        count[ord(c)-ord('a')]+=1
    result[tuple(count)].append(s)
    # because python doesnt allow a key as list so we convert it into a tuple

print(result.values())