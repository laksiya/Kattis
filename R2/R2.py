import sys

for line in sys.stdin:
    ab = line.split()
    r1 = int(ab[0])
    s = int(ab[1])
    print(s*2-r1)