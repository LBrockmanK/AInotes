- [ ] TODO:
![[09_1_FOL_21_slide_2.jpg]]
3

When we talk about a logic, or any language, we need to consider two things: the syntax and the semantics.

The syntax tells you what the symbols are and how you can put them together to form legal sequences.

First order logic has two types of symbols.
The first type are the logical symbols. These are like the reserved words of a programming language or the closed-class words in linguistics. In FOL, these are the punctuation, the connectives (including the quantifiers), and the variables. We allow an infinite number of variables, and typically use the lowercase letters x, y, and z, sometimes with subscripts, to name them.
The second type are the non logical symbols. These are like identifiers, or open-class words. In FOL, there are function symbols and predicate symbols. Both of these have an arity, which is the number of arguments that they take. For example, the proposition “OlderThan(Max, Tom)”  includes a predicate with arity 2. Note that in FOL, the constants, such as “Max”, are functions of arity zero. Also, the arity of a symbol never changes. Although in English, the same verb may take different numbers of arguments: “The cake baked” or “I baked the cake in the oven”, when we express these in logic, we will need to either use different symbols, or express the sentences as a conjunction of several simpler fixed-arity predicates, e.g.  event(e, bake1) & object(e, cake1) & agent(e, I1) & instrument(e,oven1).

![[09_1_FOL_21_slide_3.jpg]]
4


Now that we have defined the symbols (the vocabulary) for FOL,  we can consider the expressions.

There are two types of expressions.

There are  terms, which are like the nouns, in that they are symbols we will use to refer to entities in the world. 

There are also formulas, which will be used to express  propositions. A proposition is a statement that will have a truth value after all of the symbols have been given an interpretation.

In the next few slides we will consider each of these two types of expressions.



Prev: [[First Order Logic 09_1_FOL_21|First Order Logic]]
Next: [[Terms 09_1_FOL_21|Terms]]
Related Content:
[[Non logical symbols 09_1_FOL_21|Non logical symbols]]
[[Basic Facts 09_1_FOL_21|Basic Facts]]
[[Using Functions and Equality 09_1_FOL_21|Using Functions and Equality]]
[[Example of Reification 09_1_FOL_21|Example of Reification]]