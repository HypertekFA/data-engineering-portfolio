x = 5
y = 'Hello, World!'
print(x)
print(y)

x = str(5)    # x will be '5'
y = int(5)    # y will be 5
z = float(5)  # z will be 5.0
print(x)
print(y)
print(z)

x = 5
y = 'John'
print(x)
print(y)

x = 'John'

print(x)

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x)
print(y)
print(z)

nums = [1,2,3,4,5,6,7]
target = 9
result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result = [i, j]
            break
    if result:
        break

print(result)  # [0, 1]

def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(group_anagrams(words))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

list1 = ['a','b','c']
list2 = [1,2,3]
dict = {}
for i in range(len(list1)):
    dict[list1[i]] = list2[i]
print(dict)
