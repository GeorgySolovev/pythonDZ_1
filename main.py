#1
n=int(input())
print(n*(n+1)/2)
#2
import math
a= int(input())
b = int(input())

print(a+b,a-b,a*b,round(a/b,2),a//b,a%b,a**b,' log10(a): ',round(math.log10(a),2))
print( a < b, a <= b, a > b,a >= b, a !=b , a==b)

#3
import math
x= int(input())
y=int(input())
z= int(input())
print(round(math.sqrt((x**5+7)/(math.fabs(-6)*y))/(7-z)),3)

#4

#5
a=int(input('введите а:'))
b = int(input('введите b:'))
x=-b/a
m=int(input('введите m:'))
n=int(input('введите n:'))
print(m<=x<=n)

#6
v=int(input('введите v(км/час):'))
t = int(input('введите t(часов):'))
print(v*t,'км')

#7
n = int(input())
k=1
print(n*(n+1)/2)
for i in range (1,n+1):
    k=k*i
print(k)

#8
a=int(input())
b=int(input())
c=int(input())
minn=min(a,b,c)
maxx=max(a,b,c)
print(minn,a+b+c-minn-maxx,maxx)