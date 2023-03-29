Which one is the KBS?Example 1:
printColor(snow) :- !, write("It's white.").
printColor(grass) :- !, write("It's green.").
printColor(sky) :- !, write("It's yellow.").
printColor(X) :- write("Beats me.").
Example 2
printColor(X) :- colour(X,Y), !,
write("It's "), write(Y), write(".").
printColor(X) :- write("Beats me.").
color(snow,white).
color(sky,yellow).
color(X,Y) :- madeof(X,Z), colour(Z,Y).
madeof(grass,vegetation).
color(vegetation,green).
Thiese two programs are in Prolog, a language for logic programming – but not all logic programs would be considered examples of knowledge based systems.

Both programs take a query which would look like
the left side of some rule, such as printColor(sky) and try to prove it, which produces the output on the right of  A rule as a side effect.

So which one is knowledge based?