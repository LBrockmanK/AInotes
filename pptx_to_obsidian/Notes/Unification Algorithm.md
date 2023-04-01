
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