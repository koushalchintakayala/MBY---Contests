s = input().strip()
indices = []
for i in range(len(s)):
    if s[i].isupper():
        indices.append(str(i))
print(" ".join(indices) if indices else "-1")