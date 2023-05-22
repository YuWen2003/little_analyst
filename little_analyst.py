def answer(c,d):
    if c>d:
        print("LEFT")
    else:
        print("RIGHT")
 
a=int(input())
b=int(input())
 
c=(a+b)
d=abs(a-b)
result=answer(c,d)