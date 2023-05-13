- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_4.jpg]]
Lets consider an example of applying natural deduction to prove a proposition. We begin with a knowledge base – which is the explicit set of facts that we are given as true..
Here there are that: Thom is a turtle, rob is a rabbit and that Turtles out last rabbits,  when, for example, they are racing. (Although we just have to assume that is what is meant since the semantics have not been provided.

Then we could use the knowledge base to answer questions whose answers might be implicit given the knowledge, such as whether it is true that Thom would outlast Rob?

![[09_2_fol_inference_KR_21_slide_5.jpg]]
We start by using And Introduction

Then we use Universal elimination

THen we use Modus Ponens

This combination of 3 steps: and-introduction, universal-elimination and modus-ponens is a very common pattern.

![[09_2_fol_inference_KR_21_slide_6.jpg]]
One problem with treating FOL proof as search is the branching factor (especially if we have to consider all possible instantiations of the variables (for UE)

We really only care about one possible substitution the one that makes modus ponens possible.

One way to reduce the search space would be to combine these AI, UE, and MP into one “macro” step



Prev: [[Inference Rules part 09_2_fol_inference_KR_21|Inference Rules part]]
Next: [[Generalized Modus Ponens GMP 09_2_fol_inference_KR_21|Generalized Modus Ponens GMP]]
Related Content:
[[Three fundamental questions 09_KR_Intro21|Three fundamental questions]]
[[Disadvantages of using NL 09_KR_Intro21|Disadvantages of using NL]]