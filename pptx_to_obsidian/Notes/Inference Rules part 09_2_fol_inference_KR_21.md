- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_2.jpg]]
This slide lists the basic inference rules of all logics – including those without quantifiers (which are called “propositional” logics).

**

On the right side we see how we might use these inference rules to prove that a sentence S is true.  We can start with what is given (a knowledge base of facts) and then search forward, applying one inference rule at each step until we reach S. (This approach is called natural deduction.)

** ** ** ** ** ** ** ** **

The key difficulty in natural deduction is the branching factor which is determined by the number of sentences and the number of inference rules that we might use.

In automated theorem provers we often restrict ourselves to a subset of the rules (which decreases the branching factor). For example, if the knowledge base can be expressed in horn normal form, then it sufficient to use resolution.

![[09_2_fol_inference_KR_21_slide_3.jpg]]
All inference rules for PL also apply to FOL(MP, AE, AI, OI, DNE, UR, R, DML)

Now we add 3 new ones:

UE: ground term can be any constant symbol or function symbol applied to only ground terms
EE: constant symbol must not exist in the KB or else accidental inferences may be drawn
      Ex Mother(x,Joy)    infer with EE   Mother(Joy,Joy)   leads to an illogical inference
EI: All instances of the ground term must be replaced with a new variable for the sentence



Prev: [[Brief History of Reasoning 09_2_fol_inference_KR_21|Brief History of Reasoning]]
Next: [[Proofs for FOL 09_2_fol_inference_KR_21|Proofs for FOL]]
Related Content:
[[Representing Quantities 09_1_FOL_21|Representing Quantities]]
[[First Order Inference 09_2_fol_inference_KR_21|First Order Inference]]
[[Ways to apply GMP 09_2_fol_inference_KR_21|Ways to apply GMP]]
[[Resolution 09_2_fol_inference_KR_21|Resolution]]
[[Resolution Refutation 09_2_fol_inference_KR_21|Resolution Refutation]]
[[Answer extraction 09_2_fol_inference_KR_21|Answer extraction]]
[[Conjunctive Normal Form 09_2_fol_inference_KR_21|Conjunctive Normal Form]]
[[Summary of 09_2_fol_inference_KR_21|Summary]]
[[Introduction to Knowledge Representation and Reasoning 09_KR_Intro21|Introduction to Knowledge Representation and Reasoning]]
[[Representation Languages 09_KR_Intro21|Representation Languages]]