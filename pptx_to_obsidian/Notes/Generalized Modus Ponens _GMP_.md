Unify rule premises with known facts and apply unifier to conclusion

Rule:  x,y turtle(x)  rabbit(y)  outlasts(x,y)
Known facts:	turtle(Thom), and rabbit(Rob)
Unifier:	{x/Thom, y/Rob}

Apply unifier to conclusion: outlasts(Thom,Rob)

We call this new rule generalized modus ponens.

In the proof we have been considering, we would unify X with Thom and  Y with Rob and consider no other substitutions.

We would then apply this unifier to the conclusion of the implication.
Combines AI, UE, and MP into a single rule
SUBST(,q)
(where SUBST(pi') = SUBST(pi) for all i)

SUBST (p) means apply substitutions in  to sentence p
Substitution list Ө = {v1/t1, v2/t2, …, vn/tn} means
Replace all occurrences of variable vi with term ti
Substitutions are made in left to right order

Formally Generalized modus ponens packages together in one step the introduction of conjunctions, the removal of the universal quantifiers and the application of the inference rule where we replace all the corresponding variables from the knowledge base so that they match.