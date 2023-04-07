- [ ] TODO:
![[09_1_FOL_21_slide_9.jpg]]
10

Many facts can be expressed as atomic sentences.

These include basic type facts, property facts, and equality facts.

![[09_1_FOL_21_slide_10.jpg]]
11

Some facts are more complex because they state generalizations over members of a class.

Or, we may only have partial information about a fact. For example, there are a fixed set of possible alternatives but we don’t know which one of them is true.  If you have ever played the game Clue, you know this idea well.  As we learn more, we narrow down these possibilities, until we have something like “The murder was committed by Colonel Mustard with a knife in the living room.”

Closure facts are used to define all the members of a type (or to specify that two constants cannot denote the same individual.

There are also several types of terminological facts that we will consider on the next slide.

![[09_1_FOL_21_slide_11.jpg]]
12

Terminological facts are those that define relationships among user-defined predicates and functions.

To people, these relationships seem obvious, but in a logic they must be made explicit.

For example, we might want to say that two types are disjoint, for example, cats and dogs, etc

Or, we might want to say that one type is a subtype of another. Such as all humans are mammals.

Or, we might want to say that a set of subtypes is exhaustive. For example, every being is either alive or dead (This will allow us to do proofs by elimination.)

Or we might want to say that a particular relation is symmetric. This allows us to represent these relationships more compactly, using only one of  the possible orderings.

Or We might want to say that a relation is an inverse of another. For example If x is the child of y then y is the parent of x.

Or we might want to represent restrictions, or constraints of the arguments of relations. For example, only people can get married and you can’t marry yourself.

These are just some possibilities. We might also want to define transitive predicates, or compound predicates that are defined in terms of simpler ones.

What is typical is that these facts are captured as universally quantified conditionals or biconditionals.



Prev: [[Non logical symbols 09_1_FOL_21|Non logical symbols]]
Next: [[Using Functions and Equality 09_1_FOL_21|Using Functions and Equality]]
Related Content:
[[What can we do with this 09_1_FOL_21|What can we do with this]]
[[Models and Satisfaction 09_1_FOL_21|Models and Satisfaction]]
[[Generalized Modus Ponens GMP 09_2_fol_inference_KR_21|Generalized Modus Ponens GMP]]
[[Completeness of FOL Inference 09_2_fol_inference_KR_21|Completeness of FOL Inference]]
[[Converting FOL to CNF 09_2_fol_inference_KR_21|Converting FOL to CNF]]
[[Introduction to Knowledge Representation and Reasoning 09_KR_Intro21|Introduction to Knowledge Representation and Reasoning]]
[[Disadvantages of using NL 09_KR_Intro21|Disadvantages of using NL]]