Consider how we might say “John purchased a bike:
Purchases(john,sears,bike)     or
Purchases(john,sears,bike,feb14)   or
Purchases(john,sears,bike,feb14,$100)
Instead we add a purchase event:
Purchase(p)  agent(p)=john  obj(p)=bike  source(p)=sears  ..
Other Uses:  Define complex properties, such as marital status, in terms of  marriage and divorce events.