﻿- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_14.jpg]]
Completeness, when talking about search, was whether it is able to find a solution. For inferences it is similar. An inference procedure is complete if it allows you to derive any sentence that would be true according to the semantics.
Inference is a search. It can be depth first, breadth first forward chaining or backward chaining. 
An inference procedure might fail to be complete if it can get lost on an infinitely deep branch (like DFS) or if a proof can be arbitrarily long – but the search is depth limited.

Truth tables are essentially depth limited searches because we decide ahead of time how many columns to use. Hence it is incomplete.
Natural deduction is complete – it is like breadth first search.
Generalized modus ponens is incomplete for first order logic – because not all sentences can put put in the correct format .
However, given sentences in the correct format it is complete.



Prev: [[Unification 09_2_fol_inference_KR_21|Unification]]
Next: [[Inference Example 09_2_fol_inference_KR_21|Inference Example]]
Related Content:
[[Syntax 09_1_FOL_21|Syntax]]
[[Resolution 09_2_fol_inference_KR_21|Resolution]]