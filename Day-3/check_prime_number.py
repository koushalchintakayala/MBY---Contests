n = int(input())

if n < 2:
    print("Not a Prime number")
elif n in (2 ,3):
    print("Prime number")
elif n % 2 == 0 or n % 3 ==0:
    print("Not a Prime number")
else:
    i = 5
    is_prime = True
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            is_prime = False
            break
        i += 6
    print("Prime number" if is_prime else "Not a Prime number")