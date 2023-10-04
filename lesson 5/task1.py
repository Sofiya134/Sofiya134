def is_year_leap(a: int) -> bool:
    if a % 400 == 0:
        return True
    elif a % 100 == 0 and a % 400 != 0:
        return False
    elif a % 4 == 0 and a % 100 != 0:
        return True
    else:
        return False
assert is_year_leap(2400) is True
assert is_year_leap(2004) is True
assert is_year_leap(2100) is False
assert is_year_leap(2001) is False