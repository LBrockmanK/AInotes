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
Hallmark of knowledge-based system: the ability to be told facts about the world and adjust our behavior correspondingly
for example: read a book about canaries or rare coins
Cognitive penetrability: ability of our  actions to depend on our explicit beliefs.
These are conditioned responses, e.g. 
Normally, we leave the room if we hear a fire alarm
However, we do not leave the room if we hear  a fire alarm and we believe that it is being tested.
Counter example: blinking is not cognitively penetrable


A key feature of a KBS will be the ability to tell it facts and have it adjust its behavior accordingly

Philosophers call this cognitive penetrability --- which is simply the dependence of actions on explicit beliefs that we can introspect about.
Such actions are the ones we learn to do, rather than do because of some reflex. 
Learning also means that the actions may differ depending on the conditions. So, for example,
We might normally leave the room if we hear a fire alarm. But, we might not leave the room if we hear the alarm
And we believe the alarm is being tested.