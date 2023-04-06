“Thom is a turtle.”
1. turtle(Thom)
“Rob is a rabbit.”
2. rabbit(Rob)
“Turtles outlast rabbits.”
3. x,y turtle(x)  rabbit(y)  outlasts(x,y)
Prove: Does Thom outlast Rob?
? outlasts(Thom,Rob)

Lets consider an example of applying natural deduction to prove a proposition. We begin with a knowledge base – which is the explicit set of facts that we are given as true..
Here there are that: Thom is a turtle, rob is a rabbit and that Turtles out last rabbits,  when, for example, they are racing. (Although we just have to assume that is what is meant since the semantics have not been provided.

Then we could use the knowledge base to answer questions whose answers might be implicit given the knowledge, such as whether it is true that Thom would outlast Rob?

And Introduction: 1, 2
4. turtle(Thom)  rabbit(Rob)
Universal Elimination: 3 {x/Thom, y/Rob}
5. turtle(Thom)  rabbit(Rob)  outlasts(Thom,Rob)
Modus Ponens: 4, 5
6. outlasts(Thom,Rob)

AI, UE, MP is a common inference pattern

We start by using And Introduction

Then we use Universal elimination

THen we use Modus Ponens

This combination of 3 steps: and-introduction, universal-elimination and modus-ponens is a very common pattern. 

Prev: [[More Inference Rules for FOL 09_2_fol_inference_KR_21|More Inference Rules for FOL]]
Next: [[FOL Proof as Search 09_2_fol_inference_KR_21|FOL Proof as Search]]

![[09_2_fol_inference_KR_21_slide_4.jpg]]
![[09_2_fol_inference_KR_21_slide_5.jpg]]
