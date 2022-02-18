import math
n=int(input())
x=math.trunc((n/500))
y=math.trunc(((n-500*x)/200))
z=math.trunc(((n-(500*x+200*y))/100))
b=math.trunc(((n-(500*x+200*y+100*z))/50))
d=math.trunc(((n-(500*x+200*y+100*z+50*b))/20))
e=math.trunc(((n-(500*x+200*y+100*z+50*b+20*d))/10))
sum=0
if n%10!=0:
    print(-1)
elif x>=1:
    print(x)
elif y>=1:
    print(y)
elif z>=1:
    print(z)
elif b>=1:
    print(b)
elif d>=1:
    print(d)
elif e>=1:
    print(e)

sum=x+y+z+b+d+e
print(sum)


    

        
    
    

    