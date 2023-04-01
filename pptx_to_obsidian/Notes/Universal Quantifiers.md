The universal quantifier: "
Sentence holds true for all values of x in the domain of variable x

This quantifier is often used with the connective  (the same as )  to form if-then rules
“All humans are mammals” in FOL becomes:
	"x human(x)  mammal(x)
Means “ if x is a human then x is a mammal”
27


Now we will consider how we determine the truth of sentences that contain quantifiers.

A universally quantified sentence like “for all x, S(x)” will be true if S is true for all values of x in the domain of variable x.

In untyped logics, that includes all the objects in the model, including those we specify using function symbols.

This quantifier is often used with the implication symbol to form if-then rules.
So, for_all(x) human(x) => mammal of x means that if x is human then x is a mammal.  But this is not really how we speak is it.  When we speak we say, “All humans are mammals”.  Just like with propositional logic this is equivalent to saying “Either something is not human or it is a mammal”.

The tricky thing to remember about universals is they can be true when the if-part is always false. So, a sentence like “All martians are green.” is trivially true.