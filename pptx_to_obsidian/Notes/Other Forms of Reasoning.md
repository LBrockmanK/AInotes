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
By explicitly representing knowledge, we can:
reuse knowledge to solve different tasks.
Returning a list of all white things, or painting pictures
extend existing behavior by adding new knowledge.
E.g. Canaries are yellow.
debug faulty behavior by locating erroneous beliefs.
E..g. “No the sky is not yellow. It is blue.”
explain and justify behavior of the system
E.g. “because grass is a form of vegetation

Explicit representations of knowledge give KR system many advantages over traditional procedural programs.

First, the knowledge is reusable. The same facts could be used to solve several different tasks.
Second, the knowledge is extendable. We can add new facts and the behavior will adapt immediately.
Third, we can look at the encoded facts and use them to debug faulty behavior.
Fourth, we can use the facts to explain and justify the behavior of the system.  
This is especially important for medical applications.
We will do a quick review of First Order Logic, focusing on the language and its entailments.
FOL was invented by Frege to formalize mathematics.
Later we will consider what we might want to represent, and what inference procedures we might want to apply.

This completes our introduction KRR.
In the next lecture we will review first order logic, focusing on the syntax of the language and its truth conditions and entailments.
FOL is the basis of nearly all other KR, including those subsets that have been applied to the Semantic Web.
Before considering various restrictions and extensions  of FOL,  we will also consider how to express useful concepts in FOL and how to use reasoning o derive implicit knowledge.