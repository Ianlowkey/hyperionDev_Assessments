def say_the_number(num):
    num_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
                19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
                50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
                90: "ninety"}

    # if statement for numbers under 21
    if num < 21:
        return num_dict[num].capitalize()

    # if statement for numbers under 100
    if num < 100:
        if num % 10 == 0:
            return num_dict[num]
        else:
            return num_dict[num // 10 * 10] + " " + num_dict[num % 10]

    # if statement for numbers under a thousand
    if num < 1000:
        if num % 100 == 0:
            return num_dict[num // 100] + ' hundred '.capitalize()
        else:
            return num_dict[num // 100] + ' hundred and ' + say_the_number(num % 100).capitalize()

    # if statement for numbers under a million
    if num < 1000000:
        if num % 1000 == 0:
            return say_the_number(num // 1000) + ' thousand, '.capitalize()
        else:
            return say_the_number(num // 1000) + ' thousand and ' + say_the_number(num % 1000).capitalize()

    # if statement for numbers under a billion
    if num < 1000000000:
        if num % 1000000 == 0:
            return say_the_number(num // 1000000) + ' million '.capitalize()
        else:
            return say_the_number(num // 1000000) + ' million, ' + say_the_number(num % 1000000).capitalize() + '.'

    # if statement for numbers under a trillion
    if num < 1000000000000:
        if num % 1000000000 == 0:
            return say_the_number(num // 1000000000) + ' billion '.capitalize()
        else:
            return say_the_number(num // 1000000000) + ' billion, ' + say_the_number(num % 1000000000).capitalize()

    # if statement for numbers that are a trillion
    if num > 1000000000000:
        if num % 1000000000000 == 0:
            return say_the_number(num // 1000000000000) + ' trillion '.capitalize()
        else:
            return say_the_number(num // 1000000000000) + ' trillion, ' + say_the_number(
                num % 1000000000000).capitalize() + "."


print(say_the_number(0))
print(say_the_number(11))
print(say_the_number(1043283))
print(say_the_number(90376000010012))
