6. Drop universal quantifiers:
All variables are only universally quantified after step 5
e.g. xP(x)yQ(y) becomes P(x)Q(y)
All variables in KB will be assumed to be universally quantified

7. Distribute  over  :
	(PQ)R becomes (PR)(QR)

8. Group conjunctions/disjunctions together:
	(PQ)R becomes (PQR)
	(PQ)R becomes (PQR)


Once all the quantifiers are universal, we can drop them all.

The final steps are to create conjunctions of disjunctions (we do this by distributing V over ^

Then we group conjunctions and disjunctions together.
“Everyone who loves all animals is loved by someone.”
	x [y animal(y)  loves(x,y)]  [y loves(y,x)]

1&2. Eliminate biconditionals and implications
	x [y animal(y)  loves(x,y)]  [y loves(y,x)]

3. Reduce scope of  to single literals
	x [y {animal(y)  loves(x,y)}]  [y loves(y,x)]
	x [y animal(y)  loves(x,y)]  [y loves(y,x)]
	x [y animal(y)  loves(x,y)]  [y loves(y,x)]

Here is an example.

Read the slide.