min_number = int(input())

for _ in range(9):
    num = int(input())
    if num < min_number:
        min_number = num

print(f"Thank you! {min_number} is the smallest number.")
