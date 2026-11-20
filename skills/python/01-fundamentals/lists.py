names = ["apple", "banana", "cherry"]
print(names)

shopping_carts = [["apple", "banana", "cherry"], ["orange", "kiwi", "mango"]]
for shopping_cart in shopping_carts:
    for fruit in shopping_cart:
        print(fruit)

names = ["apple", "banana", "cherry"]
other_fruits = ["orange", "kiwi", "mango"]

names.extend(other_fruits)
print(names)

other_fruits.remove("kiwi")
print(other_fruits)

names.pop()

names.insert(1, "blueberry")
print(names)

