- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_7.jpg]]
We call this new rule generalized modus ponens.

In the proof we have been considering, we would unify X with Thom and  Y with Rob and consider no other substitutions.

We would then apply this unifier to the conclusion of the implication.

![[09_2_fol_inference_KR_21_slide_8.jpg]]
Formally Generalized modus ponens packages together in one step the introduction of conjunctions, the removal of the universal quantifiers and the application of the inference rule where we replace all the corresponding variables from the knowledge base so that they match.

![[09_2_fol_inference_KR_21_slide_9.jpg]]
To use this rule, we must make some assumptions. (If our problem doesn’t initially meet these conditions, then we will try to transform it so that it does.)
 
  First, all variables are universally quantified.
 
  Second the KB must be in horn form.
  In HNF, we have one positive literal.

P(x) ^ Q(x) => R(x)   <=>   !P(x) v !Q(x) v R(x)

![[09_2_fol_inference_KR_21_slide_10.jpg]]
Here is another example using GMP

We have two atomic sentences and a implication whose condition looks like it matches those sentences if only we could replace the variables.
What the sentence says is that the relation taller is transitive.
By replacing x with Larrry, y with Curly and z with Moe
The conclusion that is justtified is that “Larry is taller than Moe



Prev: [[Proofs for FOL 09_2_fol_inference_KR_21|Proofs for FOL]]
Next: [[Unification 09_2_fol_inference_KR_21|Unification]]
Related Content:
[[First Order Logic 09_1_FOL_21|First Order Logic]]
[[Proofs for FOL 09_2_fol_inference_KR_21|Proofs for FOL]]
[[Completeness of FOL Inference 09_2_fol_inference_KR_21|Completeness of FOL Inference]]
[[Inference Example 09_2_fol_inference_KR_21|Inference Example]]
[[Three fundamental questions 09_KR_Intro21|Three fundamental questions]]
[[Disadvantages of using NL 09_KR_Intro21|Disadvantages of using NL]]
[[Deductive reasoning 09_KR_Intro21|Deductive reasoning]]
[[Summary of 09_KR_Intro21|Other Forms of Reasoning]]