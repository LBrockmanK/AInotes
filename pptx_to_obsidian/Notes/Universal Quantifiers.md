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
x human(x)  mammal(x)

Equivalent to the conjunction of all the instantiations of variable x:
	(human(Rodgers)  mammal(Rodgers)) &(human(Cutler)  mammal(Cutler)) & (human(…)  mammal(…)) & …
28

*
Another way of thinking about universally quantified sentences is to replace the variable with all the ground terms that  it can refer to.

So a sentence like “all humans are mammals” is equivalent to a conjunction of all the sentences “If Rodgers is Human then Rodgers is a mammal” and so on,
 for all possible instantiations of the variables.

Note that not all possible instantiations will be useful. For example, “If MyHouse is human then MyHouse is a mammal” is a true sentence even if both of the embedded atomic propositions are false.

Also, if a conceptualization includes function symbols, then this will be an infinite conjunction, which is why we wouldn’t represent it this way in the first place. (Or we might just say “No functions”.)