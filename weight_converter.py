# python weight conventer 

weight = float(input("enter your weight: "))
unit = input("kilograms or pound ? (k or l): ")
if unit == "k":
    weight =weight*2.205
    ubit = "lbs"
elif unit == "l":
    wweight = weight / 2.205
    unit = "kgs"
else:
    print(f"{unit} was ot valid")

print(f"your weight is : {round(weight,1)}{unit}")    
