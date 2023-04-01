
Example:
p1'                 = taller(Larry,Curly)
p2' 	   = taller(Curly,Moe)
p1  p2  q    = taller(x,y)  taller(y,z)  taller(x,z)
 = {x/Larry, y/Curly, z/Moe}
SUBST(,q) = taller(Larry,Moe)
SUBST(,q)
(where SUBST(pi') = SUBST(pi) for all i)