
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