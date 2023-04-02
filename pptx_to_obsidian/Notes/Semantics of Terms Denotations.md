﻿Given the domain and an interpretation mapping for all symbols,we can get the denotation of each ground term in FOL compositionally:
		Suppose   |bestFriend| = f, |Max| = max1
                  Then |bestFriend(Max)| = f(max1)
   
To interpret terms with variables, we will also need to have a variable assignment, which is a mapping from the variables to the elements in the domain.
19

Given the domain and an interpretation mapping, we can specify which elements of the domain denoted by any variable free (ground) term of FOL.
For example, to interpret bestFriend(Max)  we use the mapping to the function denoted by “bestFriend” and then apply that function to the element denoted by “Max”.
To interpret terms with variables, we will also need to have a variable assignment, which is a mapping from the variables to the elements in the domain.

The domain will allow us to compute the  truth value for each proposition:
e.g. P1= true,  P2= false
We also use models to interpret expressions of equality, ex f(a) = f(b) iff I(f(a)) and I(f(b)) are the same in the model.
To define connectives, we have rules for evaluating truth with respect to some model m:
S		is true  iff S	is false
S1S2	is true  iff S1	is true	and	S2 is true
S1S2	is true  iff S1	is true	  or	S2 is true
S1S2 	is true  iff S1 is false      or	S2 is true		is false iff S1 is true	and	S2 is false
S1S2 	is true iff S1S2 	is true 	and 	S2S1 is true

Operator Precedence: (highest)      (lowest)
20

*
Domains tell us the truth value for each propositional symbol.

They also allow us to figure out when two functional expressions refer to the same object.

We use rules (like documentation) to define how to interpret sentences with operators in them.

For example, the upside down V is conjunction.  It is true when (and only when) both conjuncts are true.

The V is disjunction. A disjoined sentence is true whenever one of the disjuncts is true.

An implication is true either if the premise (S1) is false or the conclusion is true. Thus an implication is only false when both the premise is true and the conclusion is false.

An equivalence is true when both of the implications (s1 => s2 and s2=> s1) are true.

The precedence of operators is given on the slide.

For now, we will defer our discussion of quantifiers.