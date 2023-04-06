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

Prev: [[Which one is the KBS 09_KR_Intro21|Which one is the KBS]]
Next: [[A KBS gives Cognitive Penetrability 09_KR_Intro21|A KBS gives Cognitive Penetrability]]

![[09_KR_Intro21_slide_22.jpg]]
