The existential quantifier: $

Sentence holds true for some value of x in the domain of variable x

Main connective typically  (same as “&”)
“Some humans are rich” in FOL becomes:
	x human(x)  rich(x)
Means x is some human and x is rich.
30

An existentially  quantified sentence like “There exists x, S(x)” will be true if S is true for some value of x in the domain of variable x.

We use it to express sentences such as “some humans are rich” or “there are some rich humans”.  Here the right connective to use is conjunction (not implication).

x human(x)  rich(x)

Equivalent to the disjunction of all the  instantiations of variable x:
	(human(Rodgers)  rich(Rodgers))  (human(Cutler)  rich(Cutler))  (human(my_cat)  rich(my_cat))  …
31

An existentially quantified sentence is equivalent to a disjunction of all the instantiations of the variable x. As long as at least one of these disjuncts is true, then the entire sentence is true.
Common mistake is to use  as main connective.
Results in a weak statement

For example: x human(x)  rock(x)
	(human(Rodgers)  rock(Rodgers))  (human(Cutler)  rock(Cutler))  (human(my_house)  rock(my_house))  …
Can be true if there is something not human!
32

Just like with universals, translating sentences from English into logic can be tricky for existential expressions.

A common mistake is to use implication as the main connective instead of conjunction.

If you use implication then what you get is a very weak sentence. Suppose that we mistranslate “There is a human rock.” which is false into a logical expression that includes implication. We get a disjunction of implications which will be true if any of the subparts is true.
However remember that an implication is equivalent to not(premise) or conclusion which here would include “not(human(my_house)) or rock(my_house)”. Well since my_house is not human, this part would be true and hence the whole existentially quantified thing would be true.  What we defined is actually “there is something that is either not human or  a rock”, which is true but irrelevant.

Prev: [[Using Quantifiers]]
Next: [[Using Multiple Quantifiers]]