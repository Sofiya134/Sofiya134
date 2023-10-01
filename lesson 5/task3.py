def generate_squares(*args: int) -> list:
    return [i ** 2 for i in args]

print(generate_squares(1, 2, 3))
