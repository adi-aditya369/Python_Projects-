# while loop = execute some code while some condition remains 

# name = input("enter your name")
# age = int(input(" enter your age"))


# while age < 0:
#     print("age cant be negative")
#     age = int(input(" enter your age"))


# print(f"your age is {age}")

food = input("enter a food you like (q to quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("enter a food you like (q to quit): ")

print("bye")