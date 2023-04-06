﻿criminal(West)

So on this slide we see the proof – starting from the negated query and stopping when we get to a contradiction (which corresponds to the empty clause, which we get when we try to conjoin A and not A )

At each step pick two clauses that contain complementary literals (such as not criminal and criminal). We only resolve one such pair at each step.
While you could pick any two clauses – it is most efficient to work depth first – using whatever is left over from the previous step if you can.

And then, as the proof proceeds what is “left over” gets shorter and shorter.  Occasionally we will have to start a new subtree – but  eventually – if there is a proof – we get down to where we have just one pair of complementary literals.

Prev: [[Resolution Refutation 09_2_fol_inference_KR_21|Resolution Refutation]]
Next: [[Answer extraction 09_2_fol_inference_KR_21|Answer extraction]]

![[09_2_fol_inference_KR_21_slide_23.jpg]]