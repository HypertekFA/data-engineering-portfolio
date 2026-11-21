numbers = (1, 2, 3, 4, 5)
print(numbers)
#numbers[0] = 10  # This will raise an error because tuples are immutable

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(months)

jan = months[0]
print(jan)

for month in months:
    print(month)

# tuple unpacking
x, y, z = (1, 2, 3)
print(x)
print(y)
print(z)

locations = {
    ("New York", "USA"),
    ("London", "UK"),
    ("Tokyo", "Japan"),
}
for city, country in locations:
    print(f"{city} is in {country}")