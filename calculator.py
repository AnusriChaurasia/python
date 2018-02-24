x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def prod(x,y):
    return x*y
def div(x,y):
    return x/y
def modu(x,y):
    return x%y
print("addition of ",x,"and",y,"is",add(x,y))
print("subtraction of ",x,"and",y,"is",sub(x,y))
print("multiplication of",x,"and",y,"is",prod(x,y))
print("division of ",x,"and",y,"is",div(x,y))
print("modulo of ",x,"and",y,"is",modu(x,y))
