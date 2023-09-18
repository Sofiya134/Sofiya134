time = input('How many second?')
days = int(time)/86400
time = int(time) - (int(days)*86400)
hours = int(time)/3600
time = int(time) - (int(hours)*3600)
minuts = int(time)/60
seconds = int(time) - ((int(minuts)*60))
print(str(int(days)) + str(':') + str(int(hours)) + str(':') + str(int(minuts)) + str(':') + str(int(seconds)))