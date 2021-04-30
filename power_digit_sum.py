def get_powered_number(number, exponent):
    numbers_current_power = 1 # = 2
    i = 0
    while i < exponent:  # i = 0 exponent = 2
        numbers_current_power = number * numbers_current_power
        i += 1
    return numbers_current_power


number = 2
exponent = 65
real = get_powered_number(number, exponent)


def is_it_correct(expectation, real):
    if expectation == real:
        return True
    else:
        return False


print(is_it_correct(real, number ** exponent))
print(real)
