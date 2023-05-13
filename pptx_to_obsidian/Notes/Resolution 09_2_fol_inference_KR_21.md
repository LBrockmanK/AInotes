- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_19.jpg]]
Resolution is a refutation technique.  We try to prove that a sentence alpha is entailed by a knowledge base by showing that the knowledge base and the negation of alpha is unsatisfiable.

To apply resolution both the knowledge base and the negation of alpha must be in conjunctive normal form (but this is always possible).

Entailment in first order logic is only semi-decidable.  What that means is that if alpha is derivable from the knowledge base then we can prove it, but if alpha is not derivable (like the last example) we cannot always prove it.  (This is an example of the halting problem.)

To show Q is entailed by KB use resolution refutation to show a finite subset of sentences is unsatisfiable.
To show Q isn't entailed by KB we could try to use resolution to generate all logical consequences and show Q isn't one of them. In general, it cannot be used to generate all logical consequences of KB. Thus entailment in FOL is only semidecidable.

![[09_2_fol_inference_KR_21_slide_20.jpg]]
This slide shows how we formulate the resolution rule for propositional logic into a generalized version we can use for first order logic.

The key is to apply a substitution that allows us to resolve two literals and to apply this substitution to the resolvent as well.



Prev: [[Ways to apply GMP 09_2_fol_inference_KR_21|Ways to apply GMP]]
Next: [[Resolution Refutation 09_2_fol_inference_KR_21|Resolution Refutation]]
Related Content:
[[Representing Quantities 09_1_FOL_21|Representing Quantities]]
[[First Order Inference 09_2_fol_inference_KR_21|First Order Inference]]
[[Inference Rules part 09_2_fol_inference_KR_21|Inference Rules part]]
[[Ways to apply GMP 09_2_fol_inference_KR_21|Ways to apply GMP]]
[[Resolution Refutation 09_2_fol_inference_KR_21|Resolution Refutation]]
[[Answer extraction 09_2_fol_inference_KR_21|Answer extraction]]
[[Conjunctive Normal Form 09_2_fol_inference_KR_21|Conjunctive Normal Form]]
[[Summary of 09_2_fol_inference_KR_21|Summary]]
[[Introduction to Knowledge Representation and Reasoning 09_KR_Intro21|Introduction to Knowledge Representation and Reasoning]]
[[Representation Languages 09_KR_Intro21|Representation Languages]]