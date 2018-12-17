import sys

flag = 0
g = 0
for line in sys.stdin:
    if flag != 0:
        ab = line.split()
        a = int(ab[0])
        b = int(ab[1])
        intervals.append((a, b))

    if flag == 0:
        ab = line.split()
        num = int(ab[0])
        intervals = []
        flag = 1

for i in range(num):
    a1, b1 = intervals[i]
    for u in range(i+1, num):
        a2, b2 = intervals[u]
        if a1 <= b2 and a2 <= b1:
            g = g + 1

if g == (num*(num-1))/2:
    print("gunilla has a point")
else:
    print("edward is right")
