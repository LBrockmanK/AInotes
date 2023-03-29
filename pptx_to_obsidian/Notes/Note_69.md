FOL-CNF Conversion Example“Everyone who loves all animals is loved by someone.”
	x [y animal(y)  loves(x,y)]  [y loves(y,x)]

1&2. Eliminate biconditionals and implications
	x [y animal(y)  loves(x,y)]  [y loves(y,x)]

3. Reduce scope of  to single literals
	x [y {animal(y)  loves(x,y)}]  [y loves(y,x)]
	x [y animal(y)  loves(x,y)]  [y loves(y,x)]
	x [y animal(y)  loves(x,y)]  [y loves(y,x)]
Here is an example.

Read the slide.