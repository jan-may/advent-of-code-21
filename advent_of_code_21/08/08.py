def readFile(fileName):
    with open('input.txt') as f:
        out = [x.strip().split('|') for x in f.readlines()]
    signal_pattern = []
    output_value = []
    for x,y in out:
        signal_pattern.append(x.split())
        output_value.append(y.split())
    return signal_patterns, output_values

def check(s, val):
    return all(x in s for x in val)

def diff(s, val):
    return ''.join(x for x in s if x not in val)
         
signal_patterns = readFile('input.txt')[0]
output_values = readFile('input.txt')[1]

sum = ""
erg = 0

#task 2
for i in range(len(signal_patterns)):
    val1 = ""
    val4 = ""
    val7 = ""
    val8 = ""
    sum = "0"
    for value in signal_patterns[i]:
        if len(value) == 2:
            val1 = value
        elif len(value) == 3:
            val7 = value
        elif len(value) == 4:
            val4 = value
        elif len(value) == 7:
            val8 = value
    for value in output_values[i]:
        fourdiff = diff(val4, val1)
        print(value, fourdiff)
        if len(value) == 2:
            sum += "1"
        elif len(value) == 3:
            sum += "7"
        elif len(value) == 4:
            sum += "4"
        elif len(value) == 5 and check(value, val1):
            sum += "3"
        elif len(value) == 5 and check(value, fourdiff):
            sum += "5"
        elif len(value) == 5:
            sum += "2"
        elif len(value) == 6 and check(value, val4):
            sum += "9"
        elif len(value) == 6 and check(value, fourdiff):
            sum += "6"
        elif len(value) == 6:
            sum += "0"
        elif len(value) == 7:
            sum += "8"
    erg += int(sum)

print(erg)





        


