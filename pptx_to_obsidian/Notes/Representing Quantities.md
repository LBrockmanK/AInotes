Measurable quantities such as ages and times, distances and sizes are an interesting problem for KR. Do we add a predicate for each unit?
AgeInYears(suzy) =14
But this makes relating quantities expressed in different units hard.
For every property that might make use of time you would need an axiom to relate those given in years from those given in month.
The alternative is to introduce an abstract object for the measurable thing, such as a time duration.
For example, let age(suzy) denote an abstract quantity of time.
Then we can say years(age(suzy)) = 14 and months(x) = 12 * years(x)