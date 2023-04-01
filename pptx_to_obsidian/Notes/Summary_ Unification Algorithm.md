The algorithm recursively explores the two expressions and simultaneously builds , which is shortest length substitution list to make a match 
It is also called the  “most general unifier”
The “occurs check” disallows replacing variables with terms that contains that variable (e.g. {x/F(x)})
This slows down the algorithm
Unification with this check has time complexity of O(n2), where n is the number of terms in the expressions