- [ ] TODO:
![[09_2_fol_inference_KR_21_slide_21.jpg]]
Here is an example.
We have two clauses that are a complementary. That is they use the same predicate but one of them is negated. Also one has a variable and the other a constant – so they can be unified.
Resolution performs the substitution followed by the cancellation – leaving the uncancelled part, which also has had the substitution applied to it.
We call the “leftover” part the “RESOLVENT”

![[09_2_fol_inference_KR_21_slide_22.jpg]]
Lets consider our crime example, but use resolution refutation.

The black text shows the original form. The blue is what you get after converting to conjunctive normal form. Often these are horn (with only one positive literal) but they don’t have to be.

To begin the actual proof, we negate the clause we hope to prove and then try to show how this leads to a contradiction.

![[09_2_fol_inference_KR_21_slide_23.jpg]]
So on this slide we see the proof – starting from the negated query and stopping when we get to a contradiction (which corresponds to the empty clause, which we get when we try to conjoin A and not A )

At each step pick two clauses that contain complementary literals (such as not criminal and criminal). We only resolve one such pair at each step.
While you could pick any two clauses – it is most efficient to work depth first – using whatever is left over from the previous step if you can.

And then, as the proof proceeds what is “left over” gets shorter and shorter.  Occasionally we will have to start a new subtree – but  eventually – if there is a proof – we get down to where we have just one pair of complementary literals.



Prev: [[Resolution 09_2_fol_inference_KR_21|Resolution]]
Next: [[Answer extraction 09_2_fol_inference_KR_21|Answer extraction]]
Related Content: