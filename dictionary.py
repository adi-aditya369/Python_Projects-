# dictionary = a collection of {key:value} pairs
#               ordered and changeable.no duplicates

capitals = {"India":"Delhi",
            "USA":"Washington D.C",
            "China":"Beijing",
            "Russia":"moscow"}
# if capitals.get("Russia"):
#     print("that capital exists")
# else:
#     print("that capital doesn't not exist")   

# capitals.update({"germany": "berlin"}) 
# capitals.pop("China")
# capitals.popitem()   remove latest keys values pair
# capitals.clear()
# keys = capitals.keys()
# values = ca pitals.values()   print values
# items = capitals.items()
# print(items)
for key,value in capitals.items():
    print(f"{key}:{value}")
# print(capitals)