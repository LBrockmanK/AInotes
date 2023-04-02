 = {x/West}


This slide illustrates a backward chaining deductive proof.

In BC, we start with something we want to prove, who is a criminal and try to find a rule whose conclusion would unify with it.  In this we try to show if West is a criminal.)

Here we wanted to show that it was a crime for Nono to sell the missile. So, we find a rule that has criminal in the conclusion and we replace the other variables with constants for Nono and missiles.
Then we try to prove each of the clauses of the premise either from a fact, or by starting another backward proof with this as a subgoal.
The proof ends at the bottom where each of the clauses has been proved with the substitution that was used.

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

