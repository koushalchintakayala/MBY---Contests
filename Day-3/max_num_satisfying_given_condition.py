num1 = int(input().strip())
num2 = int(input().strip())

if num1 >= num2:
    print(-1)
else:
    max_num = -1
    for num in range(num1, num2 + 1):
        if 10 <= num <= 99 and num % 5 == 0 and sum(map(int, str(num))) % 3 == 0:
            max_num = num
    
    print(max_num)
