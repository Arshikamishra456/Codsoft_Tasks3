#WAP TO CREATE A SIMPLE CALCULATOR USING FUNCTION
def opr():
    x=int(input("enter a number:"))
    y=int(input("enter a number:"))
    return x,y
def calculator():
    print("enter your choise number:")
    print("enter 1 for addition")
    print("enter 2 for substraction")
    print("enter 3 for multiplication")
    print("enter 4 for division\n\n")
    a,b=opr()
    op=int(input("enter your choise of operation:"))
    if op in (1,2,3,4):
           if op==1:
              print("addition is:",(a+b))
           elif op==2:
              print("substraction is:",(a-b))
           elif op==3:
              print("multiplication is:",(a*b))
           elif op==4:
              print("division is:",(a//b))
           else:   
              print("invalid choise")
           calculator()
    else:
        exit(0)
calculator()
