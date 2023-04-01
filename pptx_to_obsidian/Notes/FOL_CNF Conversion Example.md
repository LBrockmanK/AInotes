4. Standardize variables apart
	x [y animal(y)  loves(x,y)]  [z loves(z,x)]

5. Eliminate Existentials by skolemizing
	x [animal(F(x))  loves(x,F(x))]  loves(G(x),x)

6. Drop universals
	[animal(F(x))  loves(x,F(x))]  loves(G(x),x)

7&8. Distribute  over  , group conjunctions/disjunctions:
	[animal(F(x))  loves(G(x),x)]  [loves(x,F(x))  loves(G(x),x)]