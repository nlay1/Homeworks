translate = {}
f = open("dict.txt", 'r')

for line in f:
    (eng, arm) = line.split()
    translate[eng] = arm

print(translate)
