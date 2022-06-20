num1=0
num2=0
def parse(expression,operator):
    x = expression.split(operator)
    
    n1 = x[0].strip()
    n2 = x[1].strip()
    
    global num1 
    num1 = int(n1)
    global num2
    num2 = int(n2)
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mult(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
#main
print("Welcome to Nate's Super Awesome Calculator!!")
expression = input("Please enter a simple expression:")
if '+' in expression:
    parse(expression,'+')
    print(add(num1,num2))
elif '-' in expression:
    parse(expression,'-')
    print(sub(num1,num2))
elif '*' in expression:
    parse(expression,'*')
    print(mult(num1,num2))
elif '/' in expression:
    parse(expression,'/')
    print(div(num1,num2))
else:
    print("Invalid Input...\nExiting...")
    exit