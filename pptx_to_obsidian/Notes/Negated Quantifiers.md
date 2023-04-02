Properties of quantifiers:
x P(x) when negated is x P(x)
x P(x) when negated is x P(x)

Why?
x sleeps(x)“Everybody sleeps.”
Negated:  (x sleeps(x))
x  sleeps(x)which says: “Somebody doesn’t sleep.”
36


Along these lines , when we have a universal “For all x P(x)” and we negate it to “not for all x P(x)”, then this is the same as saying “there exists x,  not P(x)”. In other words, the two negations on the outside can be eliminated. (But leave the one on the inside alone!)

So, an equivalent of “It is not the case that everybody sleeps.” is to say that there is somebody that doesn’t sleep.”
Truth table enumeration: incomplete for FOL(table may be infinite in size)
Natural Deduction: complete for FOL(but impractical… branching factor is too large)
GMP: incomplete for FOL(not all sentences can be converted to Horn form)
GMP: complete for FOL KB in HNF

Completeness, when talking about search, was whether it is able to find a solution. For inferences it is similar. An inference procedure is complete if it allows you to derive any sentence that would be true according to the semantics.
Inference is a search. It can be depth first, breadth first forward chaining or backward chaining. 
An inference procedure might fail to be complete if it can get lost on an infinitely deep branch (like DFS) or if a proof can be arbitrarily long – but the search is depth limited.

Truth tables are essentially depth limited searches because we decide ahead of time how many columns to use. Hence it is incomplete.
Natural deduction is complete – it is like breadth first search.
Generalized modus ponens is incomplete for first order logic – because not all sentences can put put in the correct format .
However, given sentences in the correct format it is complete.
