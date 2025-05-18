#  python shopping cart program 

food = []
prices =[]
total = 0

while True:
    food = input("enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter the price of a {food}: ₹"))
        food.append(food)
        prices.append(prices)

print("--------your cart-------")

for food in food:
    print(food,end=" ")

for price in prices:
    total += price

print(f"your total is : {total}")