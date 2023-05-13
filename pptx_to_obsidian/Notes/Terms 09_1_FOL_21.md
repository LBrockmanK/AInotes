- [ ] TODO:
![[09_1_FOL_21_slide_4.jpg]]
5

*
In first order logic we use terms to denote objects in the world.  
We have variables, which we must define (typically a finite set of lower case letters). 
Also, given a sequence of n terms and a function symbol of arity n, f of term 1 to term n will also be a term.
	A special case will be the constants, which are functions of arity 0.
	More generally functions will have more than one argument.
	Use a function to express a name or to refer to an unnamed object. (Note that expressions may look like relations. We can tell them apart by using a separate set of symbols (which we specify like the variables) and also by looking at where they appear. If they appear as an argument of a relation symbol then they are expressions. 

A ground term (or a ground anything) is an expression without any variables, that is, all the terms are constants.

![[09_1_FOL_21_slide_5.jpg]]
6

An atomic sentence is the smallest expression to which a truth value may be assigned.
There are two types of atomic sentences: 
	one is a predicate symbol with zero or more terms as arguments. (A predicate symbol with zero argument is the same as in propositional logic.) These sentences represent user defined relations. To be meaningful, each such symbol needs a definition called an interpretation which says which tuples are in the relation (like documentation) .
	Another type of sentence is a sentence that asserts the equality of two terms. It is used to represent the relation when two terms refer to the same object.

![[09_1_FOL_21_slide_6.jpg]]
7


The sentences of FOL consist of the atomic sentences, along with complex sentences that are built using connectives (the same connectives as propositional logic) and complex sentences that contain quantified variables.

In first order logic there are two quantifiers; upside down A means “for all” and backwards, upside down E is “there exists” .



Prev: [[Syntax 09_1_FOL_21|Syntax]]
Next: [[Syntax The Connectives 09_1_FOL_21|Syntax The Connectives]]
Related Content:
[[Syntax The Connectives 09_1_FOL_21|Syntax The Connectives]]
[[What can we do with this 09_1_FOL_21|What can we do with this]]
[[Assigning Truth 09_1_FOL_21|Assigning Truth]]
[[What is Knowledge 09_KR_Intro21|What is Knowledge]]