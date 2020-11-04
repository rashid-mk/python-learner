# dictionary

shop={"pen":35,"books":65,"pencil":80}
print(shop)
print(shop.get("pen")) #simply shop["pen"]
print(shop.get("apple"))  # give none as output
for i in  range (3):
    print()


contacts={"mother":[9498714,"sf@gmail.com"],
    "rsd":{"phone":9539624958,"email":"rsd58@gmail.com"}}
print(contacts["rsd"]["email"])
for i in  range (3):
    print()

print(list(shop.items()))       # convert to list
for i in  range (3):
    print()

print(shop.keys())
for i in  range (3):
    print()

print(shop.values())
for i in  range (3):
    print()


shop.pop("pen")        # delete item from dictionary
print(shop)
for i in  range (3):
    print()


shop.popitem()         # delete last  item
print(shop)

shop["tomato"]=2        #add item to dictionary
print(shop)

#dict.clear()

from collections import OrderedDict
