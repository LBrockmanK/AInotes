﻿- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_16.jpg]]
There are three main options for automated theorem provers.

Forward chaining  deduction is like breadth first search; it is  sound and complete for first order definite clauses but his NP-hard (because it searches ALL paths. For practical applications, a system will allow the developer to list which predicates can be solved by forward chaining.

Otherwise some systems, such as those implemented in Prolog, use backward chaining, which means starting with the goal and working towards explicitly known facts.  This is faster if it works – but is incomplete because one can get into loops or repeated subgoals.

A third approach is called resolution because we iteratively try to resolve clauses  to remove complementary expressions.

The next two slides show you examples of forward and backward proofs and then a resolution proof.

![[09_2_fol_inference_KR_21_slide_17.jpg]]
This slide illustrates a forward chaining proof, where we only use GMP.
The facts along the top are sentences 6, 4, 3 and 2 respectively

The result of applying GMP to these sentences is shown in the second row.

The third row, shows that we can prove West is a criminal by applying GMP to the results given in the second row.  The trick is deciding how to apply generalized modus ponens to get the goal we want.
So, that is why it is often easier to work backwards.

![[09_2_fol_inference_KR_21_slide_18.jpg]]
This slide illustrates a backward chaining deductive proof.

In BC, we start with something we want to prove, who is a criminal and try to find a rule whose conclusion would unify with it.  In this we try to show if West is a criminal.)

Here we wanted to show that it was a crime for Nono to sell the missile. So, we find a rule that has criminal in the conclusion and we replace the other variables with constants for Nono and missiles.
Then we try to prove each of the clauses of the premise either from a fact, or by starting another backward proof with this as a subgoal.
The proof ends at the bottom where each of the clauses has been proved with the substitution that was used.



Prev: [[Inference Example 09_2_fol_inference_KR_21|Inference Example]]
Next: [[Resolution 09_2_fol_inference_KR_21|Resolution]]
Related Content:
[[Resolution Refutation 09_2_fol_inference_KR_21|Resolution Refutation]]
[[Answer extraction 09_2_fol_inference_KR_21|Answer extraction]]
[[Conjunctive Normal Form 09_2_fol_inference_KR_21|Conjunctive Normal Form]]
[[Summary of 09_2_fol_inference_KR_21|Summary]]