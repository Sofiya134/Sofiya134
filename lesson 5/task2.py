def generate_natural_cubes(n: int) -> list:
    return [i ** 3 for i in range(1, n+1)]

assert generate_natural_cubes(2) == [1, 8]
assert generate_natural_cubes(5) == [1, 8, 27, 64, 125]
