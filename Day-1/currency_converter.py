amount_in_inr = int(input())
currency_name = input()

exchange_rates = {
    "Euro": 0.01417,
    "British Pound": 0.0100,
    "Australian Dollar": 0.02140,
    "Canadian Dollar": 0.02027
}
    
if currency_name in exchange_rates:
    required_amount = amount_in_inr * exchange_rates[currency_name]
    print(f"{required_amount:.2f}")
else:
    print("Invalid currency name")