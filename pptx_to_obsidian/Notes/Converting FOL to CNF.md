Replace  with equivalent: P  Q	 becomes  P  Q Q  P
Replace  with equivalent: P  Q	 becomes P  Q
Reduce scope of  to single literals:
	P		becomes P	   (DNE)
	(PQ)	becomes P  Q	   (de Morgan's)
	(PQ)	becomes P  Q	   (de Morgan's)
	xP		becomes xP
	xP		becomes xP
Standardize variables apart:
Each quantifier must have a unique variable name
Avoids confusion in steps 5 and 6
e.g. [xP]xQ]	becomes xPyQ


Here is an overview of the algorithm for converting FOL to conjunctive normal form.

Read the slide
5. Eliminate existential quantifiers (Skolemize):
	 x P(x)	becomes   P(K)	(EE)K is some new constant (Skolem constant)
e.g. xy P(x,y)becomes  xP(x,F(x))F() must be a new function (Skolem function) with arguments that are all enclosing universally quantified variables 
Everyone has a name.x person(x)  y name(y)  has(x,y)
	wrong:x person(x)  name(K)has(x,K)Everyone has the same name K!!
	We want everyone to have a name based on who they are
	right:x person(x)  name(F(x))has(x,F(x))


The next step is to replace existential quantifiers with unique constants. We call this process skolemization.

Read the slide.