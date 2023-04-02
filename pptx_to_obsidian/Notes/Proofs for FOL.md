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
States: the current KB
Actions: inference rules
Goal test: see if query is in KB

Problem: huge branching factor (especially for UE)
Idea: Find a substitution that makes the rule premise match known facts
Make new, powerful inference rule!


One problem with treating FOL proof as search is the branching factor (especially if we have to consider all possible instantiations of the variables (for UE)

We really only care about one possible substitution the one that makes modus ponens possible.

One way to reduce the search space would be to combine these AI, UE, and MP into one “macro” step
