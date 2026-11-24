
if __name__ == '__main__':
    print('Hello World')
    numbers = [10,20,35,45]
    for num in numbers:
        if num % 2 != 0 :
            print(num)

    numbers.append(45)
    print(numbers)

    numbers.extend([34,65,78,43,6])
    print(numbers)

    numbers.pop(3)
    print(numbers)
    numbers.remove(65)
    print(numbers)

    anotherlist = numbers.copy()
    print(anotherlist)
    anotherlist.remove(45)
    print(numbers)
    print(anotherlist)

    departments=[
        {"name": "John", "age": 34, "country":"Norway"},
        {"name": "Smith", "age": 32, "country": "Germany"}
    ]

    for department in departments:
        for name in department:
            print(name, department[name])