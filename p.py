from pyeda.boolalg.bdd import (
    bddvar,  expr2bdd, bdd2expr
)
import pickle
from pyeda.boolalg.expr import exprvar

def fivestep(node1, node2):
    x = []
    y = []
    z = []
    x1, x2, x3, x4 = map(exprvar, 'abcd') # x5, x6, x7, x8, x9, x10 = map(exprvar, 'abcdefghij')
    x.append(x1)
    x.append(x2)
    x.append(x3)
    x.append(x4)
    y1, y2, y3, y4 = map(exprvar, 'efgh') # y5, y6, y7, y8, y9, y10 = map(exprvar, 'abcdefghij')
    y.append(y1)
    y.append(y2)
    y.append(y3)
    y.append(y4)
    z1, z2, z3, z4 = map(exprvar, 'ijkl') #z5, z6, z7, z8, z9, z10 = map(exprvar, 'abcdefghij')
    xx1, xx2, xx3, xx4 = map(bddvar, 'abcd') #xx5, xx6, xx7, xx8, xx9, xx10 = map(bddvar, 'abcdefghij')
    yy1, yy2, yy3, yy4 = map(bddvar, 'efgh') #yy5, yy6, yy7, yy8, yy9, yy10 = map(bddvar, 'abcdefghij')
    zz1, zz2, zz3, zz4 = map(bddvar, 'ijkl') #zz5, zz6, zz7, zz8, zz9, zz10 = map(bddvar, 'abcdefghij')

    # file = open("translate.txt", "r")
    # contents = file.read()
    # file.close()

    # nums = contents.split()
    nums = ['000', '001', '001', '100', '010', '011', '100', '101', '101', '010', '011', '110']

    print (nums)
    i = 0
    j = 0
    # r = x1 & y1
    rr = None #expr2bdd(r)
    a = []
    #translating edges to bool formulas and bdds
    for node in nums:
        if i%2 == 0:
            j = 0
            for c in node:
                if c == '0':
                    #if j == 0:
                     #   a.append(~x[j])
                    #else:
                 	a.append(~x[j])
                else:
                    a.append(x[j])
                j+=1
        else:
            j = 0
            for c in node:
                if c == '0':
                    #if j == 0:
                     #   a.append(~y[j])
                    #else:
                    a.append(~y[j])
                else: #if c == '1':
                    a.append(y[j])
                j+=1
            #if i == 1:# & j == 3:
             #   r = a[0] & a[1] & a[2] & a[3] & a[4] & a[5] #& a[6] & a[7]
              #  print(r)
               # rr = expr2bdd(r)
            #else: #if j == 3:
            r = a[0] & a[1] & a[2] & a[3] & a[4] & a[5] #& a[6] & a[7]
            print(r)
            rr = rr | expr2bdd(r)
            a = []
        j=0
        i+=1
    i = 0
    hh = rr
    while i < 4:
        hh = (rr.compose({yy1:zz1, yy2:zz2, yy3:zz3, yy4:zz4}) & hh.compose({xx1:zz1, xx2:zz2, xx3:zz3, xx4:zz4})).smoothing({zz1, zz2, zz3, zz4}) | hh
        i += 1

    #print(hh.restrict({xx1:0, xx2:0, xx3:0, xx4:0, yy1:0, yy2:0, yy3:1, yy4:0}))
    #assert hh.restrict({xx1:0, xx2:0, xx3:0, xx4:0, yy1:1, yy2:0, yy3:0, yy4:0})

    return hh.restrict({xx1:0, xx2:0, xx3:0, yy1:1, yy2:1, yy3:0})

def main():
    print(bool(fivestep(0, 2)))

main()