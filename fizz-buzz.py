def check_fizz_or_buzz(number):

    str = ""

    if number % 3 == 0:
        str = str + "Fizz"
    if number % 5 == 0:
        str = str + "Buzz"
    if number % 3 != 0 and number % 5 != 0:
        str = str + str(number)

    return str

print(check_fizz_or_buzz(5))