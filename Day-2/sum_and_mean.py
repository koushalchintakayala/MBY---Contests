numbers = []

for num in map(int, input().split()):
    if num == -1:
        break
    numbers.append(num)

sum = sum(numbers)
count = len(numbers)
mean = sum / count

print(f"Sum of the given {count} numbers is : {sum}")
print(f"Mean of the given {count} numbers is : {mean:.2f}")