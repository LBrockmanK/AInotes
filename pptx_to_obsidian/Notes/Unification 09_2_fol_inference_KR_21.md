- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_11.jpg]]
The process of matching clauses that contain variables and constants is called unification. The substitution is called the unifier. By convention we use the symbol theta to refer to it.

In these examples,  assume all variables universally quantified.
If we have two clauses that use the same variable we must first “standardize them apart” which means picking a new variable for one of them.

Lets consider the examples in the table

Read the slide.

![[09_2_fol_inference_KR_21_slide_12.jpg]]
Here is a simplified version of the algorithm in your textbook.
 (Read it)
Notice that after we check that R is a variable, we immediately check whether R is in S. This involves scanning inside the terms of function to make sure that the variable doesn’t occur there. This is called the occurs check and can be expensive to implement.

However, it is very important.
Here is an example:

Everyone that helps themselves is successful.		
Helps(x,x)      => Successful(x)
      Everyone helps their mother.				
Helps(y, Mother(y))
      unify without OC   {y/Mother(y)}				
Successful(Mother(y))		
Everyone's mother is successful!!!
									
or SUBST is infinite recursion
 Mother(Mother(Mother(Mother(…

![[09_2_fol_inference_KR_21_slide_13.jpg]]
The algorithm may seem complicated but it is not really.
The algorithm recursively explores the two expressions and simultaneously builds the substitution list “theta” which is shortest length substitution list to make a match. That is why it is called the “most general unifier”
The “occurs check” in the middle stops it from replacing variables with terms that contains that variable since we would not want to allow things like someone being their own mother.
T
The cost of this check is to make the time complexity O(n2), where n is the number of terms in the expressions, so it is sometimes removed for domains where it is unlikely to happen.



Prev: [[Generalized Modus Ponens GMP 09_2_fol_inference_KR_21|Generalized Modus Ponens GMP]]
Next: [[Completeness of FOL Inference 09_2_fol_inference_KR_21|Completeness of FOL Inference]]
Related Content: