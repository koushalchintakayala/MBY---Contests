s1 = input().strip().replace(" ", "") 
s2 = input().strip().replace(" ", "")
s2_set = set(s2) 
common_chars = []

for char in s1:
    if char in s2_set and (not common_chars or common_chars.count(char) < s2.count(char)):
        common_chars.append(char)

print("".join(common_chars) if common_chars else -1)