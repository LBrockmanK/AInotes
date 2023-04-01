american(x)  weapon(y)  sells (x,y,z)  hostile(z)  criminal(x)
missile(x)  owns(Nono,x)  sells(West,x,Nono)
missile(x)  weapon(x)
enemy(x,America)  hostile(x)
enemy(Nono,America)	owns(Nono,M)
missile(M)		american(West)
Recycling the “West is a criminal” example, let’s begin by making sure that all the facts and rules in our KB are in CNF. The following are already in CNF:
The remaining four need to be converted to CNF:
american(x)  weapon(y)  sells (x,y,z)  hostile(z)  criminal(x)
missile(x)  owns(Nono,x)  sells(West,x,Nono)
enemy(x,America)  hostile(x)
missile(x)  weapon(x)
And we also first need to negate our query:  criminal(West)