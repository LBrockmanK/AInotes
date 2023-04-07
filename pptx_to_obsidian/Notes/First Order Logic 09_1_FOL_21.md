- [ ] TODO:
![[09_1_FOL_21_slide_0.jpg]]
1


In this lecture we will consider first-order logic (FOL), which is also known as predicate logic (FOPL).

First-order logic is the foundation for all successful forms of Knowledge Representation. It is a good language for describing the properties of individuals and static facts (that is, those that are true at a given moment in time).

There are automated reasoning procedures for FOL that will allow a system to accurately infer all and only what is entailed by those facts. However, these procedures are often too slow for real-time use when the set of facts is large.

To handle real problems in real-time, one solution has been to work with simplified logics, such as OWL, which we will consider later.

Also, FOL is not so good at capturing facts about how truth changes over time or how agents can form intentions to change what is currently true and act upon those intentions. It also does not address the uncertainty and incompleteness that we find in the real world. For all of these reasons, people have come up with extensions to FOL. Later in the semester we will consider these issues and the new logics, in detail.

![[09_1_FOL_21_slide_1.jpg]]
2

First order logic contains objects, relations and functions. It is thus a much more powerful language than propositional logic.

Specifically, FOL can express an infinite number of facts using a finite set of quantified propositions.


Next: [[Syntax 09_1_FOL_21|Syntax]]
Related Content: