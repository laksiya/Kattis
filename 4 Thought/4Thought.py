import sys
import operator
linenr = -1

N = 4
op = {'+':operator.add, '-': operator.sub , '/': operator.div, '*': operator.mul}
equations = {}


def generateAll():
    first = 4
    second = 4
    f = 1
    s = 1
    whole = 0
    for i in op.keys:
        for j in op.keys:
            for k in op.keys:
                string = "4 " + i + " 4 " + j + " 4 " + k + " 4"
                ops = [i, j, k]
                values = [4,4,4,4]

                if '+' in ops:
                    first, second = string.partition('+')

                while '*' in ops:
                    i = string.index('*')
                    a = int(string[i-2])
                    b = int(string[i + 2])
                    res = a*b
                    string.replace('*', res, 1)

                while '/' in ops:
                    i = string.index('/')
                    a = int(string[i - 2])
                    b = int(string[i + 2])
                    res = a/b
                    string.replace('*', res, 1)

                while '+' in ops:
                    i = string.index('+')
                    a = int(string[i-2])
                    b = int(string[i + 2])
                    res = a+b
                    string.replace('+', res, 1)

                while '*' in ops:
                    i = string.index('-')
                    a = int(string[i-2])
                    b = int(string[i + 2])
                    res = a-b
                    string.replace('-', res, 1)

                print(string)


    F = 0
    if linenr == 0:
        ab = line.split()
        NUM = int(ab[0])
    else:
        ab = line.split()
        input = int(ab[0])
        N = int(ab[0])
        if N > 256 or N < -60:
            print("no solution")

        if N = 256:
            string = "4 * 4 * 4 * 4"

        if N = 0:
            string = "4 * 4 - 4 * 4"

        if N - 4*4*4 > 0:
            string = "4 * 4 * 4 "




        print("rest:", N)
        print(string,)


