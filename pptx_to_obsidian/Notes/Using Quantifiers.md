A common mistake is to use & as the main connective
Results in a blanket statement about everything
For example, don’t say:
x human(x) & mammal(x)
 which would be:
		(human(Rodgers) & mammal(Rodgers))& 	(human(Cutler) & mammal(Cutler)) & 	(human(LambeauField) & mammal(LambeauField)) & …
But this means everything is human and a mammal!
29


Deciding how to map an English sentence into logic can be tricky, especially with universals.  A common mistake is to use conjunction as the main connective (instead of using implication which is usually the correct way.)

If we mistranslate “All humans are mammals” as “For all x human(x) and mammal (x), what we get is equivalent to a conjunction of conjunctions. If we translate back to English, then what we have said is “Everything is both a human and a mammal”  (which would include my_house, my_shoes, my_street) which is false.
The existential quantifier: $

Sentence holds true for some value of x in the domain of variable x

Main connective typically  (same as “&”)
“Some humans are rich” in FOL becomes:
	x human(x)  rich(x)
Means x is some human and x is rich.
30


An existentially  quantified sentence like “There exists x, S(x)” will be true if S is true for some value of x in the domain of variable x.

We use it to express sentences such as “some humans are rich” or “there are some rich humans”.  Here the right connective to use is conjunction (not implication).
