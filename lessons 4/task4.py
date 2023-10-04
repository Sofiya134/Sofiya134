import random
random_int = random.randint(0, 100)
while True:
    user = int(input('Try to guess a number frim 1 to 100 '))
    if user == random_int:
        print('Congratulations!')
        break
    elif user < random_int:
        print('You missed, the number should be higher')
    elif user > random_int:
        print('You missed, the number should be lower')
