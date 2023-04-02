
21

*
Lets consider an example.  First we decide on a set of objects and relations that we think are relevant to describing some situation.

Here, the objects comprise  two people, named R and J, a crown, a sword, a bag of cash, and two legs. To name the stuff, we may invent symbols such as sword1, or we might use a function like swordOf(R).

The relations are shown as labels on ovals or on links between ovals.  For each relation, there is a set of tuples that are in the relation.
For example,
   On_head contains {<crown1,R>}
   Brother contains {<R,J>, <J,R>}
   Person contains {<R>, <J>}
   King contains {<J>}
“The law says that it is a crime for an American to sell weapons to hostile nations. The country Nono, and enemy of America, has some missiles, and all of its missiles were sold to it by Colonel West, who is an American.”
1. american(x)  weapon(y)  sells (x,y,z)  hostile(z)  criminal(x)
x owns(Nono,x)  missile(x)
5. missile(x)  owns(Nono,x)  sells(West,x,Nono)
8. missile(x)  weapon(x)
7. enemy(x,America)  hostile(x)
6. american(West)
2. enemy(Nono,America)

Now we will consider a proof using GMP.

Here we consider an English description of a situation and its translation into logic.

This is our knowledge base.
We need to make sure it is in horn form.

![[slide_20_image_Picture 2054.png]]
