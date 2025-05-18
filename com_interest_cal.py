# python compound interst calculator 

principle = 0
rate = 0
time = 0 
while principle <= 0:
    principle=float(input("enter the priciple amount: "))
    if principle <= 0:
        print("principle can't be zero")


while rate <= 0:
    rate=float(input("enter the rate : "))
    if rate <= 0:
        print("rate can't be zero")

while time <= 0:
    time=int(input("enter the time amount: "))
    if time <= 0:
        print("time can't be zero")

total = principle* pow((1 + rate /100),time)
print(f"balance after {time} years/s: ₹{total:.2f}")
print(principle)
print(time)
print(rate)