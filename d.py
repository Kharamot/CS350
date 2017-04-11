from pyeda.boolalg.bdd import (
    bddvar,  expr2bdd, bdd2expr
)
     
from pyeda.boolalg.expr import exprvar

x1, x2, y1, y2, z1, z2 = map(exprvar, 'abcdef')
xx1, xx2, yy1, yy2, zz1, zz2 = map(bddvar, 'abcdef')

#translating edges to bool formulas and bdds

#first edge 0-->1, i.e., 00 --> 01
r= ~x1 & ~x2 & ~y1
r = r & y2
print(r)
rr= expr2bdd(r)
print(rr)

#second edge 1-->2; i.e., 01-->10
r= ( ~x1 & x2 & y1 & ~y2  )
print(r)
rr= rr | expr2bdd(r)

#third edge  2-->3; i.e., 10-->11
r= ( x1 & ~x2 & y1 & y2  )
print(r)
rr= rr | expr2bdd(r)

#fourth edge  3-->0; i.e., 11-->00
r= ( x1 & x2 & ~y1 & ~y2  )
print(r)
rr= rr | expr2bdd(r)


#two step reachability
hh = rr
hh=hh.compose({yy1:zz1, yy2:zz2}) & rr.compose({xx1:zz1, xx2:zz2}).smoothing({zz1,zz2}) | hh
#hh=hh.smoothing({zz1,zz2})

#test node 3 can reach node 0 in two steps, which must be false
print(hh.restrict({xx1:1, xx2:1, yy1:1, yy2:0}))
assert hh.restrict({xx1:1, xx2:1, yy1:0, yy2:1})




exit(0)