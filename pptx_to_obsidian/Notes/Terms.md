A term is used to denote an object in the world
Variables:   x, y, z, …
Function(term1, …, termn):
Constants: (functions of arity 0): Max …
e.g. sqrt(9), distance(Milwaukee,x)
Use functions to express names or to refer to an unnamed object: e.g. leftLegOf(John)
A ground term is a term with no variables
5

*
In first order logic we use terms to denote objects in the world.  
We have variables, which we must define (typically a finite set of lower case letters). 
Also, given a sequence of n terms and a function symbol of arity n, f of term 1 to term n will also be a term.
	A special case will be the constants, which are functions of arity 0.
	More generally functions will have more than one argument.
	Use a function to express a name or to refer to an unnamed object. (Note that expressions may look like relations. We can tell them apart by using a separate set of symbols (which we specify like the variables) and also by looking at where they appear. If they appear as an argument of a relation symbol then they are expressions. 

A ground term (or a ground anything) is an expression without any variables, that is, all the terms are constants.
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