heads = int(input())
legs = int(input())

r = (legs - 2 * heads) // 2
c = heads - r

if r >= 0 and c >= 0 and (2 * c + 4 * r) == legs:
    print(c, r)
else:
    print("No solution")