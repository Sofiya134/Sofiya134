def is_year_leap(a):
    if a % 400 == 0:
        print('True')
    elif a % 100 == 0 and a % 400 != 0:
        print('False')
    elif a % 4 == 0 and a % 100 != 0:
        print('True')
    else:
        print('False')
a = int(input('Enter the year'))
is_year_leap(a)
