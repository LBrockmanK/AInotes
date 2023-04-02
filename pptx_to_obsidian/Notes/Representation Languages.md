Formal language, such as logics and rules, are  often used for representation.
The alternative would be to use the languages that we learn for human to human communication: Natural language 
Some advantages of using NL would be that they are expressive and well-known.
However, they have some big disadvantages for automated reasoning.

We have different choices for representation languages.
In KR, logics or some variation are most often used.
Logics have been used since the time of Aristotle; but the use of modern logics began with Frege and Russell
Natural languages, such as English, are also representation languages.
Using NL might be appealing because it is very expressive and is well-known.
However, it didn’t suit mathematicians in creating precise theories ---  for at least three reasons.
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