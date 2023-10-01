def get_longest_word(text: str) -> str:
    text = text.lower().split(' ')
    big = ''
    for word in text:
        if len(word) > len(big):
            big = word
    return big
text = input('Enter text with english words and spaces')
lw = get_longest_word(text)
print(lw)