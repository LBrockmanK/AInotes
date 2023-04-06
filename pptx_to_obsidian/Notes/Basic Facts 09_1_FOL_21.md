The basic facts of a problem can usually be expressed as atomic sentences.
Type facts
Person(John), Person(Jane), Company(Aurora)
Property facts
Married(John,Jane), WorksFor(John,Aurora)
Equality facts
Jane = WifeOf(John)
10

Many facts can be expressed as atomic sentences.

These include basic type facts, property facts, and equality facts.
Complex facts will use connectives.
These would include universals:
 x ManagerOf(x,Aurora)  Rich(x)
 x Rich(x) & WorksFor(x,Aurora)  Lives(x,RiverHills) 
And uncertain facts
LivesIn(John, Milwaukee)V LivesIn(John, RiverHills)
And closure axioms
 x Person(x)  x=John V x=Jane
Jane ≠ John
11

Some facts are more complex because they state generalizations over members of a class.

Or, we may only have partial information about a fact. For example, there are a fixed set of possible alternatives but we don’t know which one of them is true.  If you have ever played the game Clue, you know this idea well.  As we learn more, we narrow down these possibilities, until we have something like “The murder was committed by Colonel Mustard with a knife in the living room.”

Closure facts are used to define all the members of a type (or to specify that two constants cannot denote the same individual.

There are also several types of terminological facts that we will consider on the next slide.

Prev: [[Non logical symbols 09_1_FOL_21|Non logical symbols]]
Next: [[Terminological Facts 09_1_FOL_21|Terminological Facts]]