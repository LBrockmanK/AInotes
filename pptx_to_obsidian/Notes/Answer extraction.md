Although resolution is good at answering yes-no queries, it does not tell us what entity makes the query true.
One solution, called answer extraction,  involves replacing a query y P(y) with by y P(y) & A(x)  where A is a new predicate symbol occurring nowhere else that we call the answer predicate. 
Since A occurs nowhere else, it will not be possible to derive the empty clause and we can terminate the derivation as soon as the resolvent contains only the answer predicate.
The binding for x in A(x) will be the answer we want.

In the example that we considered, we were asking if a known person (West) was a criminal. What if we wanted to ask the question, Who is a criminal around here?

This would be equivalent to the query There exists y, criminal(y).

Answer extraction is a technique that involves adding a new literal to the query (not A) where A is a new predicate symbol.  In the negated query this will show up as criminal(x) V A(x).  Note that we do not replace the existential variables in the query!

The algorithm will need to be changed to stop when only the answer predicate is left in the resolvent, and to return the arguments of the answer predicate.

Prev: [[Completed Refutation Example]]
Next: [[Conjunctive Normal Form]]