num = int(input('Enter the number '))
sum = 0
while num != 0:
    last = num % 10
    sum += last
    num //= 10
print('Sum of digits ', sum)
