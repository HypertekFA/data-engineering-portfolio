instructor ={
    "name": "John Doe",
    "owns_dog": True,
    "age": 30,
    "email": "john.doe@example.com"
}
print(instructor)
print(instructor["name"])
print(instructor["owns_dog"])
print(instructor.items())

for key, value in instructor.items():
    print(f"{key}: {value}")

carts = {
    "cart1": ["apple", "banana", "cherry"],
    "cart2": ["orange", "kiwi", "mango"]
}
for cart, fruits in carts.items():
    print(f"{cart}: {fruits}")

for value in carts.values():
    for fruit in value:
        print(fruit)

for key in carts.keys():
    for fruit in carts[key]:
        print(fruit)

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
total_donations = sum(donations.values())
print(total_donations)

#================ dictionary methods ================
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
donations_copy = donations.copy()
print(donations_copy)

fromkeys = ['a', 'b', 'c']
new_dict = dict.fromkeys(fromkeys, "default_value")
print(new_dict)

print(donations.get("sam"))

donations.pop("sam")
print(donations)
donations.popitem()
print(donations)
donations.update({"sam": 25.0, "lena": 88.99})
print(donations)
