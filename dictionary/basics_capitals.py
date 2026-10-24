# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals={
    "INDIA":"NEW DELHI",
    "USA":"WASHINGTON D.C.",
    "CHINA":"BEIJING",
    "RUSSIA":"MOSCOW"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("USA"))
# print(capitals.get("JAPAN"))

# if capitals.get("RUSSIA"):
#     print("that capital exits")
# else:
#     print("That capital doesnt exits")
# capitals.update({"GERMANY":"BERLIN"})
# capitals.update({"USA":"NEW YORK"})
# capitals.pop("CHINA")
# capitals.popitem()clears out layest added value
# capitals.clear()
# keys=capitals.keys()
# for key in capitals.keys():
#     print(key)

# value = capitals.values
# print(value)
# for value in capitals.values():
#     print(value)

items=capitals.items()
for key,value in capitals.items():
    print(f"{key}:{value}")