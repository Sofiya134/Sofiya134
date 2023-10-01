from collections import Counter

def most_frequent_word(text: str) -> str:
    w = text.split()
    wc = Counter(w)
    mfw = max(wc, key = wc.get)
    return mfw

text = input('Enter text with english words and spaces')
mwf = most_frequent_word(text)
print(mwf)
