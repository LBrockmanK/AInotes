Generalized Modus Ponens (GMP)All variables assumed to be universally quantified
Used with a KB in Horn normal form (HNF):Horn sentence: disjunction with one positive literal
single atomic sentence:      P(x)
 p1  p2 … atom:    P(x)  Q(x)  R(x)SUBST(,q)(where SUBST(pi') = SUBST(pi) for all i)

To use this rule, we must make some assumptions. (If our problem doesn’t initially meet these conditions, then we will try to transform it so that it does.)
 
  First, all variables are universally quantified.
 
  Second the KB must be in horn form.
  In HNF, we have one positive literal.

P(x) ^ Q(x) => R(x)   <=>   !P(x) v !Q(x) v R(x)