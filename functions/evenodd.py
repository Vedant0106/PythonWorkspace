def check_even_odd(number):
    if number % 2 == 0:
        return "EVEN"
    return "ODD"


num = int(input("number: "))
result = check_even_odd(num)

print(result)
