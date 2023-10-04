def remove_vowels():
    return list(input('Enter latin letters').split())
l = remove_vowels()
vowels = 'euioaEUIOA'
notvowels = list(filter(lambda x: x not in vowels, l))
print(f'no vowels: {notvowels}')