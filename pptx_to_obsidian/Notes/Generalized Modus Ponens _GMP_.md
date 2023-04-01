
Example:
p1'                 = taller(Larry,Curly)
p2' 	   = taller(Curly,Moe)
p1  p2  q    = taller(x,y)  taller(y,z)  taller(x,z)
 = {x/Larry, y/Curly, z/Moe}
SUBST(,q) = taller(Larry,Moe)
SUBST(,q)
(where SUBST(pi') = SUBST(pi) for all i)


Here is another example using GMP

We have two atomic sentences and a implication whose condition looks like it matches those sentences if only we could replace the variables.
What the sentence says is that the relation taller is transitive.
By replacing x with Larrry, y with Curly and z with Moe
The conclusion that is justtified is that “Larry is taller than Moe