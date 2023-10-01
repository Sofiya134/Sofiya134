def generate_natural_cubes(n):
    n = n+1
    l = [i ** 3 for i in range(n)]
    print(l)
n = int(input('Enter the number'))
generate_natural_cubes(n)
