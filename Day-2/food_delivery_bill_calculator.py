food_type = input().strip()
quantity = int(input().strip())
distance = int(input().strip())

if food_type not in ('V', 'N') or quantity < 1 or distance <= 0:
    print(-1)
else:
    food_cost = 120 if food_type == 'V' else 150
    total_food_cost = food_cost * quantity
    
    if distance <= 3:
        delivery_charge = 0
    elif distance <= 6:
        delivery_charge = (distance - 3) * 3
    else:
        delivery_charge = (3 * 3) + ((distance - 6) * 6)
    
    total_bill = total_food_cost + delivery_charge
    print(total_bill)
