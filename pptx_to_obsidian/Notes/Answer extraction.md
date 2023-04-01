Although resolution is good at answering yes-no queries, it does not tell us what entity makes the query true.
One solution, called answer extraction,  involves replacing a query y P(y) with by y P(y) & A(x)  where A is a new predicate symbol occurring nowhere else that we call the answer predicate. 
Since A occurs nowhere else, it will not be possible to derive the empty clause and we can terminate the derivation as soon as the resolvent contains only the answer predicate.
The binding for x in A(x) will be the answer we want.
