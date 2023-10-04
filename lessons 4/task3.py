for i in range(101):
    print(i)
    while True:
        answer = input('Should we break?').lower()
        if answer == 'yes':
            break
        elif answer == 'no':
            break
        else:
            print("Don't understand you. Please enter 'yes' or 'no'")
    if answer == 'yes':
        break
