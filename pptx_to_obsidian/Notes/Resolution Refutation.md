SUBST(, happy(x))

pj	is  well-fed(Me)
	qk	is well-fed(x)

UNIFY(pj , qk) 		result in  = {x/Me}
	SUBST(x/Me, happy(x))	result in happy(Me)

	Inferred sentence: happy(Me)

GMP is a special case of generalized resolution (for KBs in HNF)
RESOLVENT