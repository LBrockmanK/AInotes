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

Prev: [[Completeness of FOL Inference 09_2_fol_inference_KR_21|Completeness of FOL Inference]]
Next: [[Ways to apply GMP 09_2_fol_inference_KR_21|Ways to apply GMP]]

![[09_2_fol_inference_KR_21_slide_15.jpg]]
