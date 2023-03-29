Which one is the KBS?Example 1:
printColor(snow) :- !, write("It's white.").
printColor(grass) :- !, write("It's green.").
printColor(sky) :- !, write("It's yellow.").
printColour(X) :- write("Beats me.").
Example 2
printColor(X) :- colour(X,Y), !,
write("It's "), write(Y), write(".").
printColor(X) :- write("Beats me.").
color(snow,white).
color(sky,yellow).
color(X,Y) :- madeof(X,Z), colour(Z,Y).
madeof(grass,vegetation).
color(vegetation,green).
Example 2. Note that both programs do the same thing, 
but the second one has a separate collection of knowledge structures.