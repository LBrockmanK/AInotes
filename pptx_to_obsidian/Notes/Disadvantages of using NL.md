
Syntactic ambiguity
"I saw the man on the hill with the telescope"


First, NL is notoriously amibiguious.
The words are ambiguous, so bat can be a baseball thing or a furry flying mammal thing.
Also the grammars are ambiguous, leading to sentences that cannot be interpreted without more information.
This example is pretty well known in linguistics because of all the ways we might group the prepositional phrases.

Syntactic ambiguity
"I saw [the man on the hill] with the telescope“

This is probably the intended reading. But why?
Something to do with telescopes being used for seeing clearly.
Something about there being potentially many men and needing to pick one out.
Something about there not being very many hills with telescopes known to be on them 
   --- especially hills with telescopes that don’t have their own name
Syntactic ambiguity
"I saw [the man on the hill] with the telescope"
Context dependency
"John met Sam.  He gave him a shove."


A second big flaw from a reasoning point of view is the context dependency of NL.
For people this is good, because we can use fewer words to express things. 
But who are the referents for these pronouns?
Syntactic ambiguity
"I saw [the man on the hill] with the telescope"
Context dependency
"John met Sam.  HeJohn gave himSam a shove."


Really, either reading would work. 
But without actually seeing the assault, or knowing anything about their tendencies to violence,  
we might assume that He refers to John and Him refers to Sam, 
because it uses the same subject and object as the previous sentence.
Syntactic ambiguity
"I saw [the man on the hill] with the telescope"
Context dependency
"John met Sam.  HeJohn gave himSam a shove."
(Apparent) non-compositionality
"John kissed Mary." vs "John kissed [all the girls].“
Kiss(John, Mary) vs  x Forall x. girl(x) →  kiss(john,x)


The third fatal flaw for automated reasoning would be that NL appears to be non-compositional
What this means is that similar sentences might have very different representations and it wasn’t clear to logicians how to relate the two.
While this is a complaint, this non-compositionality can be addressed if one uses another construct from 
Mathematics, called the lambda calculus.
Reasoning makes implicit knowledge explicit.
[Reasoning is] the formal manipulation of the symbols representing a collection of believed propositions in order to produce representations of new ones.  Brachman and Levesque
However, the only manipulations that are justified are ones that respect the meanings of the symbols.


The third question is to explain what we mean by reasoning.
Reasoning is the process by which we make implicit knowledge explicit and …
We do that by manipulating symbols  ..
However any manipulations we use must respect the agreed upon meanings of the symbols.
We want our knowledge (and not just our explicitly encoded facts) to affect action
Example:
“Alice is allergic to medication m.”
“Anybody allergic to medication m is also allergic to m'.”
Is it OK to prescribe m' for Alice ?

Reasoning is going to be time consuming. A fair question is Why do we need reasoning?
And, the reason is that in most cases we will not be able to represent all our knowledge explicitly but
Instead will need to have some general rules that we can apply to new entities as they arise.
Consider this example: 

we may never have met Alice before, but we clearly want to put our facts together here
And not give her medication m-prime.
A set of sentences S logically entails a proposition p when the truth of p is implicit in the sentences of S
If the world is such that S is true (each proposition in S is true), then it must be case that p is also true.
Logic is the  study of entailment relations
To define a logic we define the syntax of the language (well-formedness)
The truth conditions for well-formed expressions
The rules of inference (that preserve entailment)



Earlier I said that we want reasoning because we want to know when: one set of facts constrains the world such that another fact just has to be true.

This is the essence of something called logical entailment.

In this description, we talk about a set of sentences S (which we will assume is true) and a sentence p,
Which must be true whenever every sentence in S is true.

How do we know when S constrains p in this way?  Well that is what a logic does: it  provides a set of entailment
Relations and also some procedures that preserve entailment.

We start by defining the well-formed sentences of the language. That is the synttax.
Then, for each well formed expression, we provide truth conditions. 
Then, we specify the rules of inference that preserve entailment. 
We want to choose rules that will be efficient to process and give us all  of what we need (which might be a subset of
What is actually entailed).
To verify that entailments are preserved, we  can check each rule by looking at the truth conditions of conclusions, given all possible interpretations  of the premises. 
However once an inference rule is trusted, such as modus ponens, we don’t need to validate it again.