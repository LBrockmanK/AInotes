Consider how we might say “John purchased a bike:
Purchases(john,sears,bike)     or
Purchases(john,sears,bike,feb14)   or
Purchases(john,sears,bike,feb14,$100)
Instead we add a purchase event:
Purchase(p)  agent(p)=john  obj(p)=bike  source(p)=sears  ..
Other Uses:  Define complex properties, such as marital status, in terms of  marriage and divorce events.
16

Events, which are represented by verbs in human languages, are one common use of abstract individuals.

For example, we might express the idea of John purchased a bike differently, depending on how much we know. We don’t really want to use a different predicate for each case, because the underlying transaction is the same. 

So, we add an abstract purchase event, here “p” and use it to state everything in terms of unary functions and the equality predicate.

Another good use is when a predicate depends on a sequence of events.
Substitution  is said to unify p and q if SUBST(,p) = SUBST(,q)


The process of matching clauses that contain variables and constants is called unification. The substitution is called the unifier. By convention we use the symbol theta to refer to it.

In these examples,  assume all variables universally quantified.
If we have two clauses that use the same variable we must first “standardize them apart” which means picking a new variable for one of them.

Lets consider the examples in the table

Read the slide.
