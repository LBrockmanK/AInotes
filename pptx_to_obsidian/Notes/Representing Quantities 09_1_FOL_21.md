Measurable quantities such as ages and times, distances and sizes are an interesting problem for KR. Do we add a predicate for each unit?
AgeInYears(suzy) =14
But this makes relating quantities expressed in different units hard.
For every property that might make use of time you would need an axiom to relate those given in years from those given in month.
The alternative is to introduce an abstract object for the measurable thing, such as a time duration.
For example, let age(suzy) denote an abstract quantity of time.
Then we can say years(age(suzy)) = 14 and months(x) = 12 * years(x)
17

One final use of abstract individuals is to help us represent measurable things, such as ages, sizes and times.

Measures are interesting because they involve a number and a unit of measure, such as years or inches.

Without an abstract individual we would represent these things by embedding the unit in the name of the function. But then representing relationships among quantities with different units is complex.

So, instead, what we do is introduce an abstract entity for the measurable thing and then define general functions that give us the quantity expressed in a given unit.

For example, the age(suzy) will be a time duration. years(age(suzy)) will convert that duration to a number.
With this approach, we can write expressions that map between the units, such as “the number of months will always be twelve times the number of years.

Prev: [[Example of Reification 09_1_FOL_21|Example of Reification]]
Next: [[FOL Semantics 09_1_FOL_21|FOL Semantics]]