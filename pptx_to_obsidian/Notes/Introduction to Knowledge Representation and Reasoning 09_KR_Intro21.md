- [ ] TODO:
![[09_KR_Intro21_slide_0.jpg]]
This lecture introduces the AI subarea of Knowledge Representation

![[09_KR_Intro21_slide_1.jpg]]
We will start with a definition that I adapted from the Wikipedia entry. The wiki is actually pretty good so I encourage you to read  the whole thing.

The essence of the definition is that knowledge representation and reasoning involves the use of symbols to represent some domain of discourse and the use of procedures that implement inference about the objects within the domain

A domain of discourse, or conceptualization, is simply the entities that comprise a problem including the objects, their properties and capabilities, and any explicitly known facts about them.

Inference  is a procedure to determine the truth of facts that are not explicit in the representation.

![[09_KR_Intro21_slide_2.jpg]]
Before we reflect on the meaning of the individual terms (knowledge, representation, and reasoning), we should
Consider one other philosophical point: normally when we think of knowledge, we assume there is some being that has the knowledge.
Whose knowledge are we talking about now?
Most of the time we will be considering some computer system that we are building, but sometimes we will consider other beings in the environment.
Here, I will use the term agent to refer to the entity that is doing the knowing (or doing an action of any sort).
Then we can distinguish facts that are true in the mind of some agent from facts that are taken to be universally true.
We will make this distinction when we define knowledge, but most of the time, the represented knowledge corresponds to a single agent, and so we can safely leave out the agent.

![[09_KR_Intro21_slide_3.jpg]]
When we talk about symbols, most of the time we will be talking about them as part of a logic.
Logics are expressive, have well-defined semantics, and support reasoning.
There are several variations of logic because in its full-expressiveness, logic is undecidable.
Different logics make it easier or harder to say things, and make it easier or harder to do automated reasoning.
Part of what you want to learn is how to select a logic and reasoner that is just powerful enough to do what is needed in time that meets the resource constraints of the problem

![[09_KR_Intro21_slide_4.jpg]]
One application of a very constrained form of logic is the so-called Semantic Web.

The Semantic Web aims to make the meaning of web content machine accessible. It involves the definition
Of objects and relations between them.

The different proposed layers of the Semantic Web all use languages that are limited in their expressiveness so they will be easy to process.

The lowest level is simply XML, which is not a logic at all, because there is no semantics, and no clear way to provide one.
The next level is RDF, which is a basic data model, that allows one to write simple statements about resources. It is a subset of grounded FOL (there are no variables only constants) and only binary predicates.
The next level is RDF schema, which adds a subclass and property hierarchy and range restrictions on properties.
Then we would get to the Web Ontology Language, abbreviated as OWL. OWL supports additional types of statements including disjointness of classes, cardinality restrictions on properties, and transitivity of properties. (There are actually several variants of OWL, each with varying degrees of expressiveness and decidability).

Above OWL would be a proof layer which involves deduction and the representation of proofs.


[[Generalized Modus Ponens GMP 09_2_fol_inference_KR_21|Generalized Modus Ponens GMP]]

Prev: [[Summary of 09_2_fol_inference_KR_21|Summary]]
Next: [[Three fundamental questions 09_KR_Intro21|Three fundamental questions]]
Related Content:
[[Disadvantages of using NL 09_KR_Intro21|Disadvantages of using NL]]