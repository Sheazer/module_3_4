def get_multiplied_digits(number):
    s = str(number)
    if len(s) > 0:
        first = int(s[0])
        s = s[1:]
        if first == 0:
            return get_multiplied_digits(s)
        else:
            return first * get_multiplied_digits(s)
    else:
        return 1


print(get_multiplied_digits(3030200402))
