- [ ] TODO:
![[09_1_FOL_21_slide_26.jpg]]
27


Now we will consider how we determine the truth of sentences that contain quantifiers.

A universally quantified sentence like “for all x, S(x)” will be true if S is true for all values of x in the domain of variable x.

In untyped logics, that includes all the objects in the model, including those we specify using function symbols.

This quantifier is often used with the implication symbol to form if-then rules.
So, for_all(x) human(x) => mammal of x means that if x is human then x is a mammal.  But this is not really how we speak is it.  When we speak we say, “All humans are mammals”.  Just like with propositional logic this is equivalent to saying “Either something is not human or it is a mammal”.

The tricky thing to remember about universals is they can be true when the if-part is always false. So, a sentence like “All martians are green.” is trivially true.

![[09_1_FOL_21_slide_27.jpg]]
28

*
Another way of thinking about universally quantified sentences is to replace the variable with all the ground terms that  it can refer to.

So a sentence like “all humans are mammals” is equivalent to a conjunction of all the sentences “If Rodgers is Human then Rodgers is a mammal” and so on,
 for all possible instantiations of the variables.

Note that not all possible instantiations will be useful. For example, “If MyHouse is human then MyHouse is a mammal” is a true sentence even if both of the embedded atomic propositions are false.

Also, if a conceptualization includes function symbols, then this will be an infinite conjunction, which is why we wouldn’t represent it this way in the first place. (Or we might just say “No functions”.)

![[09_1_FOL_21_slide_28.jpg]]
29


Deciding how to map an English sentence into logic can be tricky, especially with universals.  A common mistake is to use conjunction as the main connective (instead of using implication which is usually the correct way.)

If we mistranslate “All humans are mammals” as “For all x human(x) and mammal (x), what we get is equivalent to a conjunction of conjunctions. If we translate back to English, then what we have said is “Everything is both a human and a mammal”  (which would include my_house, my_shoes, my_street) which is false.

![[09_1_FOL_21_slide_29.jpg]]
30


An existentially  quantified sentence like “There exists x, S(x)” will be true if S is true for some value of x in the domain of variable x.

We use it to express sentences such as “some humans are rich” or “there are some rich humans”.  Here the right connective to use is conjunction (not implication).

![[09_1_FOL_21_slide_30.jpg]]
31


An existentially quantified sentence is equivalent to a disjunction of all the instantiations of the variable x. As long as at least one of these disjuncts is true, then the entire sentence is true.

![[09_1_FOL_21_slide_31.jpg]]
32

Just like with universals, translating sentences from English into logic can be tricky for existential expressions.

A common mistake is to use implication as the main connective instead of conjunction.

If you use implication then what you get is a very weak sentence. Suppose that we mistranslate “There is a human rock.” which is false into a logical expression that includes implication. We get a disjunction of implications which will be true if any of the subparts is true.
However remember that an implication is equivalent to not(premise) or conclusion which here would include “not(human(my_house)) or rock(my_house)”. Well since my_house is not human, this part would be true and hence the whole existentially quantified thing would be true.  What we defined is actually “there is something that is either not human or  a rock”, which is true but irrelevant.

![[09_1_FOL_21_slide_32.jpg]]
33

These next few slides contain several interesting properties of quantifiers and their orderings.  I will mention these things briefly, but you should take a minute before moving on.

First, when you have two nested quantifiers that are the same, it doesn’t matter what order they come in. (It is like you are picking two elements from a set but immediately putting the first element back before you pick the second one, so there is no dependence between the two.)

In English this is like saying “Everyone likes everybody” is the same as “Everyone is liked by everybody”.

![[09_1_FOL_21_slide_33.jpg]]
34

However, when the quantifiers are different then the order is VERY important.

So to express “Everyone has someone that they like” we use for all x, there exists y. which means that each x can have a different y that they like. (Or they can like the same y; there is no restriction).

However to express “There is someone who is liked by everyone”, we have to put the existential on the outside (exists x for_all y likes(x,y)) .

![[09_1_FOL_21_slide_34.jpg]]
35


Another interesting property is that we can rewrite each of the quantifiers in terms of the other one. You just negate both the new quantifier and the sentence inside the expression.

This is akin to saying that we can reduce a double negation.

For example in English, “everybody sleeps” means the same as “nobody doesn’t sleep.”

![[09_1_FOL_21_slide_35.jpg]]
36


Along these lines , when we have a universal “For all x P(x)” and we negate it to “not for all x P(x)”, then this is the same as saying “there exists x,  not P(x)”. In other words, the two negations on the outside can be eliminated. (But leave the one on the inside alone!)

So, an equivalent of “It is not the case that everybody sleeps.” is to say that there is somebody that doesn’t sleep.”



Prev: [[Truth Tables 09_1_FOL_21|Truth Tables]]
Next: [[Some Terminology 09_1_FOL_21|Some Terminology]]
Related Content:
[[Terms 09_1_FOL_21|Terms]]
[[What can we do with this 09_1_FOL_21|What can we do with this]]
[[FOL Semantics 09_1_FOL_21|FOL Semantics]]
[[An Example 09_1_FOL_21|An Example]]
[[Assigning Truth 09_1_FOL_21|Assigning Truth]]
[[Models and Satisfaction 09_1_FOL_21|Models and Satisfaction]]
[[Entailment 09_1_FOL_21|Entailment]]
[[Truth Tables 09_1_FOL_21|Truth Tables]]