Sentences are assigned a truth value with respect to a domain and an interpretation mapping

The domain contains the objects and the relations among them .
The interpretation mapping specifies what symbols refer to:
Predicate symbols refer to relations
Functional symbols refer to functional relations on terms, where constants  refer to objects

18

*
Semantics tells us what the meaning of a given formula is, which in FOL will be either true or false.  FOL does not let us say “maybe”.

To have a semantics, we first need to specify the “backend”, which is our representation of the “real-world”. A domain, sometimes called a model, contains the objects and the relations among them. In a computer we might capture these statically,  using other stored expressions, or we might define them procedurally, as function calls to read the value of some sensor or to query an external resource.

The interpretation mapping is our mapping from the syntax to the domain. To assign a truth value, (1) we  need to map the terms to objects and (2) we need to know what relations (or executed functions) the predicates correspond to and what the connectives do. 

Together the domain and the mapping comprise the interpretation in FOL.


Prev: [[Representing Quantities]]
Next: [[Semantics of Terms Denotations]]