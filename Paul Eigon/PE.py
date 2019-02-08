import sys

for line in sys.stdin:
    ab = line.split()
    N = int(ab[0])
    P = int(ab[1])
    O = int(ab[2])
    l = int((P + O)/N)
if l % 2 == 0:
    print("paul")
else:
    print("opponent")