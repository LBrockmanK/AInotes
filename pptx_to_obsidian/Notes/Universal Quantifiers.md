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
Properties of quantifiers:
x y is the same as y x
x y is the same as y x

Why?
 "x "y likes(x,y) the active voice: “Everyone likes everyone.”
 "y "x likes(x,y) the passive voice: “Everyone is liked by everyone.”
33

These next few slides contain several interesting properties of quantifiers and their orderings.  I will mention these things briefly, but you should take a minute before moving on.

First, when you have two nested quantifiers that are the same, it doesn’t matter what order they come in. (It is like you are picking two elements from a set but immediately putting the first element back before you pick the second one, so there is no dependence between the two.)

In English this is like saying “Everyone likes everybody” is the same as “Everyone is liked by everybody”.
Properties of quantifiers:
x y is not the same as y x
x y is not the same as y x

Why?
x y likes(x,y) “Everyone has someone they like.”
y x likes(x,y)  “There is someone who is liked by everyone.”
34

However, when the quantifiers are different then the order is VERY important.

So to express “Everyone has someone that they like” we use for all x, there exists y. which means that each x can have a different y that they like. (Or they can like the same y; there is no restriction).

However to express “There is someone who is liked by everyone”, we have to put the existential on the outside (exists x for_all y likes(x,y)) .
Properties of quantifiers:
x P(x) is the same as x P(x)
x P(x) is the same as x P(x)

Why?
x sleep(x)“Everybody sleeps.”
x  sleep(x)double negative: “Nobody doesn’t sleep.”
35


Another interesting property is that we can rewrite each of the quantifiers in terms of the other one. You just negate both the new quantifier and the sentence inside the expression.

This is akin to saying that we can reduce a double negation.

For example in English, “everybody sleeps” means the same as “nobody doesn’t sleep.”
Properties of quantifiers:
x P(x) when negated is x P(x)
x P(x) when negated is x P(x)

Why?
x sleeps(x)“Everybody sleeps.”
Negated:  (x sleeps(x))
x  sleeps(x)which says: “Somebody doesn’t sleep.”
36


Along these lines , when we have a universal “For all x P(x)” and we negate it to “not for all x P(x)”, then this is the same as saying “there exists x,  not P(x)”. In other words, the two negations on the outside can be eliminated. (But leave the one on the inside alone!)

So, an equivalent of “It is not the case that everybody sleeps.” is to say that there is somebody that doesn’t sleep.”