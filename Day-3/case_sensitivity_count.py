s = input().strip()
upper = 0
lower = 0

for c in s:
    if c.isupper():
        upper += 1
    elif c.islower():
        lower += 1

print(f"Uppercase Letters : {upper}")
print(f"Lowercase Letters : {lower}")