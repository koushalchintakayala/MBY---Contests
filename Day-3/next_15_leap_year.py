year = int(input())
leap_years = []
n = 0

while n < 15:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap_years.append(year)
        n += 1
    year += 1
    
for i in range(len(leap_years) - 1):
    print(leap_years[i], end=", ")
print(leap_years[-1])