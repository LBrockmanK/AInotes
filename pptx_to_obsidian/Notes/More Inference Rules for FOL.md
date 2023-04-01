
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