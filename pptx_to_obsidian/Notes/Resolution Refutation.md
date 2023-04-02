SUBST(, happy(x))

pj	is  well-fed(Me)
	qk	is well-fed(x)

UNIFY(pj , qk) 		result in  = {x/Me}
	SUBST(x/Me, happy(x))	result in happy(Me)

	Inferred sentence: happy(Me)

GMP is a special case of generalized resolution (for KBs in HNF)
RESOLVENT

Here is an example.
We have two clauses that are a complementary. That is they use the same predicate but one of them is negated. Also one has a variable and the other a constant – so they can be unified.
Resolution performs the substitution followed by the cancellation – leaving the uncancelled part, which also has had the substitution applied to it.
We call the “leftover” part the “RESOLVENT”

american(x)  weapon(y)  sells (x,y,z)  hostile(z)  criminal(x)
missile(x)  owns(Nono,x)  sells(West,x,Nono)
missile(x)  weapon(x)
enemy(x,America)  hostile(x)
enemy(Nono,America)	owns(Nono,M)
missile(M)		american(West)
Recycling the “West is a criminal” example, let’s begin by making sure that all the facts and rules in our KB are in CNF. The following are already in CNF:
The remaining four need to be converted to CNF:
american(x)  weapon(y)  sells (x,y,z)  hostile(z)  criminal(x)
missile(x)  owns(Nono,x)  sells(West,x,Nono)
enemy(x,America)  hostile(x)
missile(x)  weapon(x)
And we also first need to negate our query:  criminal(West)

Lets consider our crime example, but use resolution refutation.

The black text shows the original form. The blue is what you get after converting to conjunctive normal form. Often these are horn (with only one positive literal) but they don’t have to be.

To begin the actual proof, we negate the clause we hope to prove and then try to show how this leads to a contradiction.

