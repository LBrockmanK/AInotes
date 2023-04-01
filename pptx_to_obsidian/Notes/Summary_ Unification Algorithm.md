The algorithm recursively explores the two expressions and simultaneously builds , which is shortest length substitution list to make a match 
It is also called the  “most general unifier”
The “occurs check” disallows replacing variables with terms that contains that variable (e.g. {x/F(x)})
This slows down the algorithm
Unification with this check has time complexity of O(n2), where n is the number of terms in the expressions

The algorithm may seem complicated but it is not really.
The algorithm recursively explores the two expressions and simultaneously builds the substitution list “theta” which is shortest length substitution list to make a match. That is why it is called the “most general unifier”
The “occurs check” in the middle stops it from replacing variables with terms that contains that variable since we would not want to allow things like someone being their own mother.
T
The cost of this check is to make the time complexity O(n2), where n is the number of terms in the expressions, so it is sometimes removed for domains where it is unlikely to happen.

