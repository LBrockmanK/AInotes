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

