def calculator(paid,price):
    change = paid - price
    return change

snack_price = 25
coins = 0
total_inserted = 0
print("Welcome to the SNACKS vending machine!")
print("These are the valid coins: 1, 5, 10, 25")
print("the amount of coins which is valid is 25")

while True:
    coin = int(input("Enter insert a coin: "))
    if coin not in [1,5,10,25]:
        print("Invalid coin. Please insert a valid coin.")
        continue
    total_inserted += coin
    print(f"Total inserted: {total_inserted} cents")

    if total_inserted >= snack_price:
        change = calculator(total_inserted, snack_price)
        break

print("Enough money has been inserted. Dispensing snack...")

if change == 0:
    pass
else:
    print(f"Your change is: {change} cents")


print("========Summary of your purchase========")
print(f"Total inserted: {total_inserted} cents")
print(f"Snack price : {snack_price}")
print(f"Change return back to you is {change}")
print("========Thank you for your vist========")