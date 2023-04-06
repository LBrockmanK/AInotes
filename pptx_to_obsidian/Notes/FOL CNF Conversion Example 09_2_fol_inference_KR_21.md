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
4. Standardize variables apart
	x [y animal(y)  loves(x,y)]  [z loves(z,x)]

5. Eliminate Existentials by skolemizing
	x [animal(F(x))  loves(x,F(x))]  loves(G(x),x)

6. Drop universals
	[animal(F(x))  loves(x,F(x))]  loves(G(x),x)

7&8. Distribute  over  , group conjunctions/disjunctions:
	[animal(F(x))  loves(G(x),x)]  [loves(x,F(x))  loves(G(x),x)]

Read the slide

Prev: [[Converting FOL to CNF 09_2_fol_inference_KR_21|Converting FOL to CNF]]
Next: [[Summary of 09_2_fol_inference_KR_21|Summary]]

![[09_2_fol_inference_KR_21_slide_29.jpg]]
![[09_2_fol_inference_KR_21_slide_30.jpg]]
