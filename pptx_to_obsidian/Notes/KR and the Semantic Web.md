The Semantic Web initiative aims to make the meaning of web content machine accessible.
The different layers of the Semantic Web use logics with limited expressiveness that are easy to process.
At the lowest level is XML, which is not a logic at all.
RDF, is a basic data model, for writing simple statements about resources.  It is a subset of grounded FOL (no veariables) with only binary predicates.
RDF Schema adds a subclass and property hierarchy, with range restrictions on properties (e.g. anything that is eaten is food)
The Web Ontology language is a subset of FOL, that supports additional types of statements, such as disjointness of classes, cardinality restrictions on properties, transifivity of properties.
Above OWL  would be a proof layer which involves deduction and the representation of proofs.