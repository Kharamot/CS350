from pyeda.boolalg.bdd import (
    bddvar,  expr2bdd, bdd2expr
)
from pyeda.boolalg.expr import exprvar

def fivestep(node1, node2):
	n1 = str(bin(int(node1))[2:].zfill(10))
	n2 = str(bin(int(node2))[2:].zfill(10))
	a = [] #to store the binary ints of node1
	b = [] #to store the binary ints of node2

	i=0
	for c in n1:
		a.append(int(c))
		i+=1
	i=0
	for c in n2:
		b.append(int(c))
		i+=1

	x = [] #to store the static x expvars
	y = [] #to store the static y expvars
	z = []
	x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = map(exprvar, 'abcdefghij')
	x.append(x1)
	x.append(x2)
	x.append(x3)
	x.append(x4)
	x.append(x5)
	x.append(x6)
	x.append(x7)
	x.append(x8)
	x.append(x9)
	x.append(x10)
	y1, y2, y3, y4, y5, y6, y7, y8, y9, y10 = map(exprvar, 'klmnopqrst')
	y.append(y1)
	y.append(y2)
	y.append(y3)
	y.append(y4)
	y.append(y5)
	y.append(y6)
	y.append(y7)
	y.append(y8)
	y.append(y9)
	y.append(y10)
	z1, z2, z3, z4, z5, z6, z7, z8, z9, z10 = map(exprvar, 'ABCDEFGHIJ')
	xx1, xx2, xx3, xx4, xx5, xx6, xx7, xx8, xx9, xx10 = map(bddvar, 'klmnopqrst')
	yy1, yy2, yy3, yy4, yy5, yy6, yy7, yy8, yy9, yy10 = map(bddvar, 'abcdefghij')
	zz1, zz2, zz3, zz4, zz5, zz6, zz7, zz8, zz9, zz10 = map(bddvar, 'ABCDEFGHIJ')

	file = open("translate.txt", "r")
	contents = file.read()
	file.close()

	nums = contents.split()
	i = 0
	j = 0
	#r = x1 & y1
	rr = None #expr2bdd(r)
	exp = []
	#translating edges to bool formulas and bdds
	print("Building BDD")
	for node in nums:
		if i%2 == 0:
			j = 0
			for c in node:
				if c == '0':
					exp.append(~x[j])
				else:
					exp.append(x[j])
				j+=1
		else:
			j = 0
			for c in node:
				if c == '0':
					exp.append(~y[j])
				else:
					exp.append(y[j])
				j+=1
			r = exp[0] & exp[1] & exp[2] & exp[3] & exp[4] & exp[5] & exp[6] & exp[7] & exp[8] & exp[9] & exp[10] & exp[11] & exp[12] & exp[13] & exp[14] & exp[15] & exp[16] & exp[17] & exp[18] & exp[19]
			rr = rr | expr2bdd(r)
			exp = []
		#print(j)
		j=0
		i+=1

	#Start searching for 5 step.
	i = 0
	hh = rr
	print("Finding 5 step.")
	while i < 4:
		hh = (rr.compose({yy1:zz1, yy2:zz2, yy3:zz3, yy4:zz4, yy5:zz5, yy6:zz6, yy7:zz7, yy8:zz8, yy9:zz9, yy10:zz10}) & hh.compose({xx1:zz1, xx2:zz2, xx3:zz3, xx4:zz4, xx5:zz5, xx6:zz6, xx7:zz7, xx8:zz8, xx9:zz9, xx10:zz10})).smoothing({zz1, zz2, zz3, zz4, zz5, zz6, zz7, zz8, zz9, zz10}) | hh
		i += 1
	if(hh.restrict({xx1:a[0], xx2:a[1], xx3:a[2], xx4:a[3], xx5:a[4], xx6:a[5], xx7:a[6], xx8:a[7], xx9:a[8], xx10:a[9], yy1:b[0], yy2:b[1], yy3:b[2], yy4:b[3], yy5:b[4], yy6:b[5], yy7:b[6], yy8:b[7], yy9:b[8], yy10:b[9]}) == 1):
		return True
	else:
		return False

def main():
	print(bool(fivestep(0, 940)))


main()