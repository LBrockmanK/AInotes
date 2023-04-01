These are general relationships among predicates, such as:
disjointness  x[Cat(x)  ¬Dog(x)]
subtype  x[Human(x)  Mammal(x)]
exhaustive  x[Being(x)  Alive(x)V Dead(x)
symmetry x y [Sibling(x,y)   Sibling(y,x)]
inverses  x  y [ChildOf(x,y)  ParentOf(y,x)]
type restrictions  x  y [MarriedTo(x,y)  
      Person(x)  Person(y)   x ≠ y ]
They are usually universally quantified conditionals or biconditionals

12

Terminological facts are those that define relationships among user-defined predicates and functions.

To people, these relationships seem obvious, but in a logic they must be made explicit.

For example, we might want to say that two types are disjoint, for example, cats and dogs, etc

Or, we might want to say that one type is a subtype of another. Such as all humans are mammals.

Or, we might want to say that a set of subtypes is exhaustive. For example, every being is either alive or dead (This will allow us to do proofs by elimination.)

Or we might want to say that a particular relation is symmetric. This allows us to represent these relationships more compactly, using only one of  the possible orderings.

Or We might want to say that a relation is an inverse of another. For example If x is the child of y then y is the parent of x.

Or we might want to represent restrictions, or constraints of the arguments of relations. For example, only people can get married and you can’t marry yourself.

These are just some possibilities. We might also want to define transitive predicates, or compound predicates that are defined in terms of simpler ones.

What is typical is that these facts are captured as universally quantified conditionals or biconditionals.