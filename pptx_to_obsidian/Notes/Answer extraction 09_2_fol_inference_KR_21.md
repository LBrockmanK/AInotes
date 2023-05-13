- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_24.jpg]]
In the example that we considered, we were asking if a known person (West) was a criminal. What if we wanted to ask the question, Who is a criminal around here?

This would be equivalent to the query There exists y, criminal(y).

Answer extraction is a technique that involves adding a new literal to the query (not A) where A is a new predicate symbol.  In the negated query this will show up as criminal(x) V A(x).  Note that we do not replace the existential variables in the query!

The algorithm will need to be changed to stop when only the answer predicate is left in the resolvent, and to return the arguments of the answer predicate.



Prev: [[Resolution Refutation 09_2_fol_inference_KR_21|Resolution Refutation]]
Next: [[Conjunctive Normal Form 09_2_fol_inference_KR_21|Conjunctive Normal Form]]
Related Content:
[[Ways to apply GMP 09_2_fol_inference_KR_21|Ways to apply GMP]]
[[Resolution Refutation 09_2_fol_inference_KR_21|Resolution Refutation]]
[[Conjunctive Normal Form 09_2_fol_inference_KR_21|Conjunctive Normal Form]]
[[Summary of 09_2_fol_inference_KR_21|Summary]]