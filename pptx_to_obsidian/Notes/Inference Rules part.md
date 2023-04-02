﻿Modus Ponens
And-Elimination (AE):
And-Introduction (AI):
Or-Introduction (OI):
Double-Negation 
Elimination (DNE):
    Unit Resolution (UR):
Resolution (R):
Prove S using natural deduction with these rules.
deMorgan’s Law (DML):
6. R		(MP: 1,2)
7. W		(MP: 3,6)
8. P  R	(AI: 1,6)
9. S  W	(MP: 5,8)
10. S		(UR: 7,9)


This slide lists the basic inference rules of all logics – including those without quantifiers (which are called “propositional” logics).

**

On the right side we see how we might use these inference rules to prove that a sentence S is true.  We can start with what is given (a knowledge base of facts) and then search forward, applying one inference rule at each step until we reach S. (This approach is called natural deduction.)

** ** ** ** ** ** ** ** **

The key difficulty in natural deduction is the branching factor which is determined by the number of sentences and the number of inference rules that we might use.

In automated theorem provers we often restrict ourselves to a subset of the rules (which decreases the branching factor). For example, if the knowledge base can be expressed in horn normal form, then it sufficient to use resolution.

Universal Elimination, UE
	variable substituted with ground term
	x Eats(Jim, x) infer Eats(Jim, Cake)

Existential Elimination, EE
	variable substituted with new constant
	x Eats(Jim, x) infer Eats(Jim, NewFood)

Existential Introduction, EI
	ground term substituted with variable
	Eats(Jim, Cake) infer x Eats(x, Cake)
SUBST({v/g}, α)
SUBST({v/k}, α)
v SUBST({g/v}, α)

All inference rules for PL also apply to FOL(MP, AE, AI, OI, DNE, UR, R, DML)

Now we add 3 new ones:

UE: ground term can be any constant symbol or function symbol applied to only ground terms
EE: constant symbol must not exist in the KB or else accidental inferences may be drawn
      Ex Mother(x,Joy)    infer with EE   Mother(Joy,Joy)   leads to an illogical inference
EI: All instances of the ground term must be replaced with a new variable for the sentence