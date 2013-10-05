## lessons learned 
## 1 : no assignment withint conditional statement in python
evenlist=[]
x1=1
x2=2
x3=x1+x2
evenlist.append(x2)
while ( x3 < 4000000 ) : 
	if (x3 % 2 == 0 ): 
		evenlist.append(x3)
	x2,x1=x3,x2
	x3=x1+x2

print sum(evenlist)
