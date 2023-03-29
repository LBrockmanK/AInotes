Converting FOL to CNF5. Eliminate existential quantifiers (Skolemize):
	 x P(x)	becomes   P(K)	(EE)K is some new constant (Skolem constant)
e.g. xy P(x,y)becomes  xP(x,F(x))F() must be a new function (Skolem function) with arguments that are all enclosing universally quantified variables 
Everyone has a name.x person(x)  y name(y)  has(x,y)
	wrong:x person(x)  name(K)has(x,K)Everyone has the same name K!!
	We want everyone to have a name based on who they are
	right:x person(x)  name(F(x))has(x,F(x))

The next step is to replace existential quantifiers with unique constants. We call this process skolemization.

Read the slide.