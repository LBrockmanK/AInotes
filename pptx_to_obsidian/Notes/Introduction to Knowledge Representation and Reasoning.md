Susan McRoy

This lecture introduces the AI subarea of Knowledge Representation
Knowledge representation and reasoning is an area of AI that is concerned with how to use symbols to represent "a domain of discourse", along with functions that allow inference about the objects within the domain of discourse to occur. 
Adapted from the Wikipedia Article on KRR

A domain of discourse constitutes the entities in  a problem under consideration, including the objects,  their properties and capabilities, and any known facts about entities, events or states of the environment.
Inference is a procedure by which we can determine the truth of facts we have not been told explicitly (ie the implicitly known ones).

We will start with a definition that I adapted from the Wikipedia entry. The wiki is actually pretty good so I encourage you to read  the whole thing.

The essence of the definition is that knowledge representation and reasoning involves the use of symbols to represent some domain of discourse and the use of procedures that implement inference about the objects within the domain

A domain of discourse, or conceptualization, is simply the entities that comprise a problem including the objects, their properties and capabilities, and any explicitly known facts about them.

Inference  is a procedure to determine the truth of facts that are not explicit in the representation.
This definition captures  KR as a discipline, but doesn’t really explain KR or the underlying philosophical issues, such as  who is doing the knowing. 
To address the who question, we will use the term “agent” to refer to the entity that is doing the knowing (or doing an action of any sort).
Then we can distinguish facts that are true in the mind of some agent from those  taken to be universally true .
But  we won’t always mention this agent explicitly, for example, if all the represented knowledge corresponds to a single agent, such as “the system”.

Before we reflect on the meaning of the individual terms (knowledge, representation, and reasoning), we should
Consider one other philosophical point: normally when we think of knowledge, we assume there is some being that has the knowledge.
Whose knowledge are we talking about now?
Most of the time we will be considering some computer system that we are building, but sometimes we will consider other beings in the environment.
Here, I will use the term agent to refer to the entity that is doing the knowing (or doing an action of any sort).
Then we can distinguish facts that are true in the mind of some agent from facts that are taken to be universally true.
We will make this distinction when we define knowledge, but most of the time, the represented knowledge corresponds to a single agent, and so we can safely leave out the agent.
There are many formalisms for KR, nearly all based on some logic, because logics are very expressive and the semantics and reasoning systems for them are well-defined 
Approaches will vary significantly in how easy it is to say things and how long it takes, in real-time, to make the inferences that are needed by an application.
More expressive languages tend to allow us to say things more compactly, but reasoning with them take much longer.. 

The key problem is to thus to  find a KR approach that can make the inferences an application needs in time that is within the resource constraints of the problem at hand
 

When we talk about symbols, most of the time we will be talking about them as part of a logic.
Logics are expressive, have well-defined semantics, and support reasoning.
There are several variations of logic because in its full-expressiveness, logic is undecidable.
Different logics make it easier or harder to say things, and make it easier or harder to do automated reasoning.
Part of what you want to learn is how to select a logic and reasoner that is just powerful enough to do what is needed in time that meets the resource constraints of the problem
The Semantic Web initiative aims to make the meaning of web content machine accessible.
The different layers of the Semantic Web use logics with limited expressiveness that are easy to process.
At the lowest level is XML, which is not a logic at all.
RDF, is a basic data model, for writing simple statements about resources.  It is a subset of grounded FOL (no veariables) with only binary predicates.
RDF Schema adds a subclass and property hierarchy, with range restrictions on properties (e.g. anything that is eaten is food)
The Web Ontology language is a subset of FOL, that supports additional types of statements, such as disjointness of classes, cardinality restrictions on properties, transifivity of properties.
Above OWL  would be a proof layer which involves deduction and the representation of proofs.

One application of a very constrained form of logic is the so-called Semantic Web.

The Semantic Web aims to make the meaning of web content machine accessible. It involves the definition
Of objects and relations between them.

The different proposed layers of the Semantic Web all use languages that are limited in their expressiveness so they will be easy to process.

The lowest level is simply XML, which is not a logic at all, because there is no semantics, and no clear way to provide one.
The next level is RDF, which is a basic data model, that allows one to write simple statements about resources. It is a subset of grounded FOL (there are no variables only constants) and only binary predicates.
The next level is RDF schema, which adds a subclass and property hierarchy and range restrictions on properties.
Then we would get to the Web Ontology Language, abbreviated as OWL. OWL supports additional types of statements including disjointness of classes, cardinality restrictions on properties, and transitivity of properties. (There are actually several variants of OWL, each with varying degrees of expressiveness and decidability).

Above OWL would be a proof layer which involves deduction and the representation of proofs.