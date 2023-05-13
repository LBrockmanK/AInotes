- [ ] TODO:
![[09_1_FOL_21_slide_17.jpg]]
18

*
Semantics tells us what the meaning of a given formula is, which in FOL will be either true or false.  FOL does not let us say “maybe”.

To have a semantics, we first need to specify the “backend”, which is our representation of the “real-world”. A domain, sometimes called a model, contains the objects and the relations among them. In a computer we might capture these statically,  using other stored expressions, or we might define them procedurally, as function calls to read the value of some sensor or to query an external resource.

The interpretation mapping is our mapping from the syntax to the domain. To assign a truth value, (1) we  need to map the terms to objects and (2) we need to know what relations (or executed functions) the predicates correspond to and what the connectives do. 

Together the domain and the mapping comprise the interpretation in FOL.

![[09_1_FOL_21_slide_18.jpg]]
19

Given the domain and an interpretation mapping, we can specify which elements of the domain denoted by any variable free (ground) term of FOL.
For example, to interpret bestFriend(Max)  we use the mapping to the function denoted by “bestFriend” and then apply that function to the element denoted by “Max”.
To interpret terms with variables, we will also need to have a variable assignment, which is a mapping from the variables to the elements in the domain.

![[09_1_FOL_21_slide_19.jpg]]
20

*
Domains tell us the truth value for each propositional symbol.

They also allow us to figure out when two functional expressions refer to the same object.

We use rules (like documentation) to define how to interpret sentences with operators in them.

For example, the upside down V is conjunction.  It is true when (and only when) both conjuncts are true.

The V is disjunction. A disjoined sentence is true whenever one of the disjuncts is true.

An implication is true either if the premise (S1) is false or the conclusion is true. Thus an implication is only false when both the premise is true and the conclusion is false.

An equivalence is true when both of the implications (s1 => s2 and s2=> s1) are true.

The precedence of operators is given on the slide.

For now, we will defer our discussion of quantifiers.



Prev: [[Representing Quantities 09_1_FOL_21|Representing Quantities]]
Next: [[An Example 09_1_FOL_21|An Example]]
Related Content:
[[Terms 09_1_FOL_21|Terms]]
[[What can we do with this 09_1_FOL_21|What can we do with this]]
[[An Example 09_1_FOL_21|An Example]]
[[Assigning Truth 09_1_FOL_21|Assigning Truth]]
[[Models and Satisfaction 09_1_FOL_21|Models and Satisfaction]]
[[Entailment 09_1_FOL_21|Entailment]]
[[Truth Tables 09_1_FOL_21|Truth Tables]]
[[Universal Quantifiers 09_1_FOL_21|Universal Quantifiers]]