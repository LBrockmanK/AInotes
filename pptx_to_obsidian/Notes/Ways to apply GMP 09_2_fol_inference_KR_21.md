Deduction as forward chaining adds all sentences that can be inferred – it is both sound and complete (but slow) & has been used for some databases.
Deduction as backward chaining starts with a goal and tries to search backward, trying to prove the premises of rules as subgoals; it is faster but incomplete.
Resolution is an alternative strategy where the negation of a goal is added to (a CNF version of) a KB and then to prove the KB+ is unsatisfiable we find & remove complementary literals, one at a time.

There are three main options for automated theorem provers.

Forward chaining  deduction is like breadth first search; it is  sound and complete for first order definite clauses but his NP-hard (because it searches ALL paths. For practical applications, a system will allow the developer to list which predicates can be solved by forward chaining.

Otherwise some systems, such as those implemented in Prolog, use backward chaining, which means starting with the goal and working towards explicitly known facts.  This is faster if it works – but is incomplete because one can get into loops or repeated subgoals.

A third approach is called resolution because we iteratively try to resolve clauses  to remove complementary expressions.

The next two slides show you examples of forward and backward proofs and then a resolution proof.



Prev: [[Inference Example 09_2_fol_inference_KR_21|Inference Example]]
Next: [[Forward Chaining with GMP 09_2_fol_inference_KR_21|Forward Chaining with GMP]]

![[09_2_fol_inference_KR_21_slide_16.jpg]]
