def return_day(day):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(day) if day in days else None
print(return_day(3))

def last_element(lst):
    if lst:
        return lst[-1]
    return None
print(last_element([1, 2, 3]))
print(last_element([]))

def single_letter_count(word, letter):
    return word.lower().count(letter.lower())
print(single_letter_count("Hello", "h"))

def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in set(word)}
print(multiple_letter_count("hello"))

