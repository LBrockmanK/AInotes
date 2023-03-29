KR and the Semantic WebThe Semantic Web initiative aims to make the meaning of web content machine accessible.
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