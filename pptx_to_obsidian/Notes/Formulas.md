An atomic sentence is the smallest expression to which a truth value can be assigned
Predicate(term1, …, termn):
e.g. teacher(McRoy,You), lte(sqrt(2),sqrt(7))
Maps one or more objects to a truth value
Represents a user defined relation
Term1 = Term2:
e.g. height(McRoy) = 66,  1 = 2
Represents when two terms refer to the same object
6

An atomic sentence is the smallest expression to which a truth value may be assigned.
There are two types of atomic sentences: 
	one is a predicate symbol with zero or more terms as arguments. (A predicate symbol with zero argument is the same as in propositional logic.) These sentences represent user defined relations. To be meaningful, each such symbol needs a definition called an interpretation which says which tuples are in the relation (like documentation) .
	Another type of sentence is a sentence that asserts the equality of two terms. It is used to represent the relation when two terms refer to the same object.
A sentence represents a fact in the world that is assigned a truth value; It is:
Atomic sentence
Complex sentence using connectives: 
e.g. spouse(George,Laura) spouse(Laura,George)
Complex sentence using quantified variables: " $ sentence 
e.g. " x " y (spouse(x,y)  spouse(y,x))
7

The sentences of FOL consist of the atomic sentences, along with complex sentences that are built using connectives (the same connectives as propositional logic) and complex sentences that contain quantified variables.

In first order logic there are two quantifiers; upside down A means “for all” and backwards, upside down E is “there exists” .