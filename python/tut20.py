def greter(a,b):
    if(a>b):
        print("a is greter ")
    else:
        print("b is greter")

def lessthen(a,b):
    if(a<b):
        print("a is lesser")
    else:
        print("b is lesser")

a=int (input("Enter the first Number"))
b=int (input ("Enter the Second Number"))

greter(a,b)
print("and")
lessthen(a,b)