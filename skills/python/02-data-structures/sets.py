nums = {1, 2, 3, 4, 5}

# Add an element to the set
nums.add(6)
print(nums)

nums.remove(6)
print(nums)

print(nums)

nums.add(7)
nums.update([8, 9, 10])
print(nums)

nums.discard(8)
print(nums)

nums.difference_update({1, 2, 3})
print(nums)

#============ Set Math Operations ============
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
c = a.union(b)
print(c)
print(a is c)
d = a.intersection(b)
print(d)

e = a.difference(b)
print(e)

f = a.symmetric_difference(b)
print(f)