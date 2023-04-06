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

All variables assumed to be universally quantified
Used with a KB in Horn normal form (HNF):Horn sentence: disjunction with one positive literal
single atomic sentence:      P(x)
 p1  p2 … atom:    P(x)  Q(x)  R(x)
SUBST(,q)
(where SUBST(pi') = SUBST(pi) for all i)

To use this rule, we must make some assumptions. (If our problem doesn’t initially meet these conditions, then we will try to transform it so that it does.)

  First, all variables are universally quantified.

  Second the KB must be in horn form.
  In HNF, we have one positive literal.

P(x) ^ Q(x) => R(x)   <=>   !P(x) v !Q(x) v R(x)

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

Prev: [[FOL Proof as Search 09_2_fol_inference_KR_21|FOL Proof as Search]]
Next: [[Unification 09_2_fol_inference_KR_21|Unification]]