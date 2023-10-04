l = list(input('Enter latin letters').split())
def map_to_tuples(l):
    return list(map(lambda x: (x.upper(), x.lower()), l))
print(map_to_tuples(l))