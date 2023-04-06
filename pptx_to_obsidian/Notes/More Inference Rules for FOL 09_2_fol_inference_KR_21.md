
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

Prev: [[Inference Rules part 09_2_fol_inference_KR_21|Inference Rules part]]
Next: [[Proofs for FOL 09_2_fol_inference_KR_21|Proofs for FOL]]

![[09_2_fol_inference_KR_21_slide_3.jpg]]
