#You have x number of 1 rupee coins and y number of 5 rupee coins. You want to purchase an item for amount z rupees, and the shopkeeper requires exact change. Determine the number of 1 rupee and 5 rupee coins to use such that the exact amount is paid with the minimum number of coins. If it is not possible to pay the exact amount, output -1.

x = int(input())
y = int(input())
z = int(input())

max_fives = min(y, z // 5)
remaining = z - (max_fives * 5)

if remaining <= x:
    print(remaining)
    print(max_fives)
else:
    print(-1)