fi = open('./input.txt', 'r')
num = int(fi.readline().split()[0])
problems = sorted(map(int, fi.readline().split()))

secs = 300.0*60.0
i = 0

while True:
    if secs - problems[i] >= 0 and i + 1 < num:
        i += 1
    else:
        break

fo = open('./output.txt', 'w')
fo.write(str(i))
