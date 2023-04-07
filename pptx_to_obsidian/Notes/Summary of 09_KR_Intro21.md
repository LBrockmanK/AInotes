- [ ] TODO:
![[09_KR_Intro21_slide_19.jpg]]
To better model some of the reasoning that people do,  researchers have developed several non-deductive approaches to reasoning.
For example, abduction is based on a rule, similar to modus ponens that says, if you have a rule “if A then B”
And you observe B then you may abduce that A is true.  This is the sort of reasoning we do when diagnosing the cause based on a symptom. However the conclusions won’t always be valid: Not every cough is pneumonia.

![[09_KR_Intro21_slide_20.jpg]]
Thiese two programs are in Prolog, a language for logic programming – but not all logic programs would be considered examples of knowledge based systems.

Both programs take a query which would look like
the left side of some rule, such as printColor(sky) and try to prove it, which produces the output on the right of  A rule as a side effect.

So which one is knowledge based?

![[09_KR_Intro21_slide_21.jpg]]
Example 2. Note that both programs do the same thing, 
but the second one has a separate collection of knowledge structures.

![[09_KR_Intro21_slide_22.jpg]]
The facts at the bottom comprise a small knowledge base.

![[09_KR_Intro21_slide_23.jpg]]
A key feature of a KBS will be the ability to tell it facts and have it adjust its behavior accordingly

Philosophers call this cognitive penetrability --- which is simply the dependence of actions on explicit beliefs that we can introspect about.
Such actions are the ones we learn to do, rather than do because of some reflex. 
Learning also means that the actions may differ depending on the conditions. So, for example,
We might normally leave the room if we hear a fire alarm. But, we might not leave the room if we hear the alarm
And we believe the alarm is being tested.

![[09_KR_Intro21_slide_24.jpg]]
Explicit representations of knowledge give KR system many advantages over traditional procedural programs.

First, the knowledge is reusable. The same facts could be used to solve several different tasks.
Second, the knowledge is extendable. We can add new facts and the behavior will adapt immediately.
Third, we can look at the encoded facts and use them to debug faulty behavior.
Fourth, we can use the facts to explain and justify the behavior of the system.  
This is especially important for medical applications.

![[09_KR_Intro21_slide_25.jpg]]
This completes our introduction KRR.
In the next lecture we will review first order logic, focusing on the syntax of the language and its truth conditions and entailments.
FOL is the basis of nearly all other KR, including those subsets that have been applied to the Semantic Web.
Before considering various restrictions and extensions  of FOL,  we will also consider how to express useful concepts in FOL and how to use reasoning o derive implicit knowledge.



Content:
[[Introduction to Knowledge Representation and Reasoning 09_KR_Intro21|Introduction to Knowledge Representation and Reasoning]]
[[Three fundamental questions 09_KR_Intro21|Three fundamental questions]]
[[What is Knowledge 09_KR_Intro21|What is Knowledge]]
[[Representation Languages 09_KR_Intro21|Representation Languages]]
[[Disadvantages of using NL 09_KR_Intro21|Disadvantages of using NL]]
[[Deductive reasoning 09_KR_Intro21|Deductive reasoning]]
[[Generalized Modus Ponens GMP 09_2_fol_inference_KR_21|Generalized Modus Ponens GMP]]
[[Introduction to Knowledge Representation and Reasoning 09_KR_Intro21|Introduction to Knowledge Representation and Reasoning]]
[[Disadvantages of using NL 09_KR_Intro21|Disadvantages of using NL]]