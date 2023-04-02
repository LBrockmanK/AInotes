The syntax of a logic tells you the well-formed sequences of symbols
FOL has 2 types of symbols:
Logical symbols have a fixed meaning in the language. There are 3 types:
Punctuation (such as parentheses)
Connectives and quantifiers
Variables  (x, y, z, x1, x2, …)
Non-logical symbols are those whose meanings depend on the application  (there are an infinite supply of these)
Function symbols (bestFriend, a, b, c, d,…, h)
Predicate symbols (OlderThan, P, Q, R, P1,…)

3

When we talk about a logic, or any language, we need to consider two things: the syntax and the semantics.

The syntax tells you what the symbols are and how you can put them together to form legal sequences.

First order logic has two types of symbols.
The first type are the logical symbols. These are like the reserved words of a programming language or the closed-class words in linguistics. In FOL, these are the punctuation, the connectives (including the quantifiers), and the variables. We allow an infinite number of variables, and typically use the lowercase letters x, y, and z, sometimes with subscripts, to name them.
The second type are the non logical symbols. These are like identifiers, or open-class words. In FOL, there are function symbols and predicate symbols. Both of these have an arity, which is the number of arguments that they take. For example, the proposition “OlderThan(Max, Tom)”  includes a predicate with arity 2. Note that in FOL, the constants, such as “Max”, are functions of arity zero. Also, the arity of a symbol never changes. Although in English, the same verb may take different numbers of arguments: “The cake baked” or “I baked the cake in the oven”, when we express these in logic, we will need to either use different symbols, or express the sentences as a conjunction of several simpler fixed-arity predicates, e.g.  event(e, bake1) & object(e, cake1) & agent(e, I1) & instrument(e,oven1).