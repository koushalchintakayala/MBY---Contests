sal = int(input())
job_level = int(input())

if job_level == 3:
    hike = 15
elif job_level == 4:
    hike = 7
elif job_level == 5:
    hike = 5
else:
    hike = 0
    
new_sal = sal + (sal * hike // 100)

print(new_sal)