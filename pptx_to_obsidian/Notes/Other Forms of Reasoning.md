Abduction
Probabilistic
Default
Analogical

These reasoning methods that are not deductive and the reasoning is not always sound, but they provide a way of dealing with  incomplete or uncertain information.


To better model some of the reasoning that people do,  researchers have developed several non-deductive approaches to reasoning.
For example, abduction is based on a rule, similar to modus ponens that says, if you have a rule “if A then B”
And you observe B then you may abduce that A is true.  This is the sort of reasoning we do when diagnosing the cause based on a symptom. However the conclusions won’t always be valid: Not every cough is pneumonia.
Example 1:
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
Example 1:
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
Example 1:
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
color(X,Y) :- madeof(X,Z), color(Z,Y).
madeof(grass,vegetation).
color(vegetation,green).

The facts at the bottom comprise a small knowledge base.