def is_leap(year):
    if year % 4 != 0:
        result = False
    elif year % 100 != 0:
        result = True
    elif year % 400 != 0:
        result = False
    else:
        result = True

    return result
