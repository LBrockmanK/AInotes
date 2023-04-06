
unify (P, Q, THETA) {
  if no differences then return THETA
  else {
    R = mismatch term in P      // where R  S
    S = mismatch term in Q
  }
  if R is a variable then {
    if R is in S then return FAILURE
    add {R/S} to THETA
    return unify(P-sub-THETA, Q-sub-THETA, THETA)
  }
  else if S is a variable {
    if S is in R then return FAILURE
    add {S/R} to THETA
    return unify(P-sub-THETA, Q-sub-THETA, THETA)
  }
  else return FAILURE           // no unifier found
}

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
The algorithm recursively explores the two expressions and simultaneously builds , which is shortest length substitution list to make a match 
It is also called the  “most general unifier”
The “occurs check” disallows replacing variables with terms that contains that variable (e.g. {x/F(x)})
This slows down the algorithm
Unification with this check has time complexity of O(n2), where n is the number of terms in the expressions

The algorithm may seem complicated but it is not really.
The algorithm recursively explores the two expressions and simultaneously builds the substitution list “theta” which is shortest length substitution list to make a match. That is why it is called the “most general unifier”
The “occurs check” in the middle stops it from replacing variables with terms that contains that variable since we would not want to allow things like someone being their own mother.
T
The cost of this check is to make the time complexity O(n2), where n is the number of terms in the expressions, so it is sometimes removed for domains where it is unlikely to happen.



Prev: [[Unification 09_2_fol_inference_KR_21|Unification]]
Next: [[Completeness of FOL Inference 09_2_fol_inference_KR_21|Completeness of FOL Inference]]

![[09_2_fol_inference_KR_21_slide_12.jpg]]
![[09_2_fol_inference_KR_21_slide_13.jpg]]
