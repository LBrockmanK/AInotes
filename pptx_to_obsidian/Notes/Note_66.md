Converting FOL to CNFReplace  with equivalent: P  Q	 becomes  P  Q Q  P
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