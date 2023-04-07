- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_14.jpg]]
Completeness, when talking about search, was whether it is able to find a solution. For inferences it is similar. An inference procedure is complete if it allows you to derive any sentence that would be true according to the semantics.
Inference is a search. It can be depth first, breadth first forward chaining or backward chaining. 
An inference procedure might fail to be complete if it can get lost on an infinitely deep branch (like DFS) or if a proof can be arbitrarily long – but the search is depth limited.

Truth tables are essentially depth limited searches because we decide ahead of time how many columns to use. Hence it is incomplete.
Natural deduction is complete – it is like breadth first search.
Generalized modus ponens is incomplete for first order logic – because not all sentences can put put in the correct format .
However, given sentences in the correct format it is complete.


[[What can we do with this 09_1_FOL_21|What can we do with this]]
[[Models and Satisfaction 09_1_FOL_21|Models and Satisfaction]]
[[Generalized Modus Ponens GMP 09_2_fol_inference_KR_21|Generalized Modus Ponens GMP]]

Prev: [[Unification 09_2_fol_inference_KR_21|Unification]]
Next: [[Inference Example 09_2_fol_inference_KR_21|Inference Example]]
Related Content:
[[Ways to apply GMP 09_2_fol_inference_KR_21|Ways to apply GMP]]
[[Resolution Refutation 09_2_fol_inference_KR_21|Resolution Refutation]]
[[Converting FOL to CNF 09_2_fol_inference_KR_21|Converting FOL to CNF]]
[[Introduction to Knowledge Representation and Reasoning 09_KR_Intro21|Introduction to Knowledge Representation and Reasoning]]
[[Disadvantages of using NL 09_KR_Intro21|Disadvantages of using NL]]