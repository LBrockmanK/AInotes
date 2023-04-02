Logical symbols:
Punctuation: (, )
Variables:	x, y, x1…
Connectives:Ù Ú Ø Þ Û = " $
Non-Logical Symbols
Functions:	Income, Address, Sqrt, …
Constants:	Marvin, 2, Milwaukee, …
Predicates:	Teacher, Sisters, Even, Prime…

38

*
That completes our overview of the language of first order logic, including both the logical and the non-logical symbols.

As we look ahead to inference we may choose to exclude some of these to make reasoning more efficient.  In particular, functions (which make the domain infinite) and equality (which can add a large number of irrelevant relations) are often excluded.

Resolution is a refutation technique:
To prove KB╞  α  show that KB   α  is unsatisfiable
Resolution uses KB and  α  in CNF:
Conjunction of clauses that are disjunction of literals
Entailment in general FOL is only semi-decidable:
Can prove α if KB╞  α 
Cannot always prove that KB doesn’t╞  α 
Resolution repeatedly combines two clauses to make a new one until an empty clause is derived (a contradiction)


Resolution is a refutation technique.  We try to prove that a sentence alpha is entailed by a knowledge base by showing that the knowledge base and the negation of alpha is unsatisfiable.

To apply resolution both the knowledge base and the negation of alpha must be in conjunctive normal form (but this is always possible).

Entailment in first order logic is only semi-decidable.  What that means is that if alpha is derivable from the knowledge base then we can prove it, but if alpha is not derivable (like the last example) we cannot always prove it.  (This is an example of the halting problem.)

To show Q is entailed by KB use resolution refutation to show a finite subset of sentences is unsatisfiable.
To show Q isn't entailed by KB we could try to use resolution to generate all logical consequences and show Q isn't one of them. In general, it cannot be used to generate all logical consequences of KB. Thus entailment in FOL is only semidecidable.