name = input()

sum = sum(ord(c) for c in name)

if sum % 2 == 0:
    print(f"{name} is lucky")
else:
    print(f"{name} is not lucky")