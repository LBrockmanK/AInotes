32BC    Aristotle		Inference rules (syllogisms), quantifiers
1565     Cardano	PL + uncertainty (probability theory)
1847     Boole		PL (again)
1879     Frege		FOL
1922     Wittgenstein	proof using truth table
1930     Gödel		complete algo for FOL exists
1930     Herbrand	complete algo for FOL (reduce to PL)
1931     Gödel		no complete algo for number theory
1960     Davis/Putnam	practical algo for PL
1965     Robinson	practical algo for FOL (resolution)
1972	   Colmerauer	invention of Prolog, 1st logic programming language
1995     ISO                       ISO standard for Prolog

Logic has been around since the days of the Stoics and Aristotle  but practical inference methods for first order logic are relatively recent.  Logic programming originated in the 1960’s and early 70’s. 
The first ISO standard for a logic programming language was not completed until 1995.
Theorems are the true sentences that can be derived from a given set of  sentences.
There are many ways to show that a sentence in logic is true – the most basic is to use a truth table and show that by all possible truth assignments a sentence must be true. 
Other methods rely on search – this is what we mean by “deduction”.  There are rules that can be shown to be true – such as by using a truth table – which can be used the same way we use transitions in a state space search.

Today you can get free automated theorem provers, and specialized systems for “model checking” that are used in software verification – especially for concurrent systems.

On the next few slides we will consider examples of rules of inference and how they are used in proofs.