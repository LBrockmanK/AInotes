- [ ] TODO:
![[09_KR_Intro21_slide_10.jpg]]
First, NL is notoriously amibiguious.
The words are ambiguous, so bat can be a baseball thing or a furry flying mammal thing.
Also the grammars are ambiguous, leading to sentences that cannot be interpreted without more information.
This example is pretty well known in linguistics because of all the ways we might group the prepositional phrases.

![[09_KR_Intro21_slide_11.jpg]]
This is probably the intended reading. But why?
Something to do with telescopes being used for seeing clearly.
Something about there being potentially many men and needing to pick one out.
Something about there not being very many hills with telescopes known to be on them 
   --- especially hills with telescopes that don’t have their own name

![[09_KR_Intro21_slide_12.jpg]]
A second big flaw from a reasoning point of view is the context dependency of NL.
For people this is good, because we can use fewer words to express things. 
But who are the referents for these pronouns?

![[09_KR_Intro21_slide_13.jpg]]
Really, either reading would work. 
But without actually seeing the assault, or knowing anything about their tendencies to violence,  
we might assume that He refers to John and Him refers to Sam, 
because it uses the same subject and object as the previous sentence.

![[09_KR_Intro21_slide_14.jpg]]
The third fatal flaw for automated reasoning would be that NL appears to be non-compositional
What this means is that similar sentences might have very different representations and it wasn’t clear to logicians how to relate the two.
While this is a complaint, this non-compositionality can be addressed if one uses another construct from 
Mathematics, called the lambda calculus.

![[09_KR_Intro21_slide_15.jpg]]
The third question is to explain what we mean by reasoning.
Reasoning is the process by which we make implicit knowledge explicit and …
We do that by manipulating symbols  ..
However any manipulations we use must respect the agreed upon meanings of the symbols.

![[09_KR_Intro21_slide_16.jpg]]
Reasoning is going to be time consuming. A fair question is Why do we need reasoning?
And, the reason is that in most cases we will not be able to represent all our knowledge explicitly but
Instead will need to have some general rules that we can apply to new entities as they arise.
Consider this example: 

we may never have met Alice before, but we clearly want to put our facts together here
And not give her medication m-prime.

![[09_KR_Intro21_slide_17.jpg]]
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



Prev: [[Representation Languages 09_KR_Intro21|Representation Languages]]
Next: [[Deductive reasoning 09_KR_Intro21|Deductive reasoning]]
Related Content:
[[First Order Logic 09_1_FOL_21|First Order Logic]]
[[Proofs for FOL 09_2_fol_inference_KR_21|Proofs for FOL]]
[[Generalized Modus Ponens GMP 09_2_fol_inference_KR_21|Generalized Modus Ponens GMP]]
[[Completeness of FOL Inference 09_2_fol_inference_KR_21|Completeness of FOL Inference]]
[[Inference Example 09_2_fol_inference_KR_21|Inference Example]]
[[Three fundamental questions 09_KR_Intro21|Three fundamental questions]]
[[Deductive reasoning 09_KR_Intro21|Deductive reasoning]]
[[Summary of 09_KR_Intro21|Other Forms of Reasoning]]