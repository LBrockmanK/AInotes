Existential Quantifiers (3)Common mistake is to use  as main connective.
Results in a weak statement

For example: x human(x)  rock(x)
	(human(Rodgers)  rock(Rodgers))  (human(Cutler)  rock(Cutler))  (human(my_house)  rock(my_house))  …
Can be true if there is something not human!
Just like with universals, translating sentences from English into logic can be tricky for existential expressions.

A common mistake is to use implication as the main connective instead of conjunction.

If you use implication then what you get is a very weak sentence. Suppose that we mistranslate “There is a human rock.” which is false into a logical expression that includes implication. We get a disjunction of implications which will be true if any of the subparts is true.
However remember that an implication is equivalent to not(premise) or conclusion which here would include “not(human(my_house)) or rock(my_house)”. Well since my_house is not human, this part would be true and hence the whole existentially quantified thing would be true.  What we defined is actually “there is something that is either not human or  a rock”, which is true but irrelevant.