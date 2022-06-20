import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)
password = ''
numUpper = 0
numLower = 0
numNum = 0
numSym = 0
print("Nate's Random Password Generator")
n = int(input("Length of password to be generated:"))
m=n
u = input("""Enter every associated number in a single string to include character subset: 
        \n1\tUppercase \n2\tLowercase \n3\tNumbers \n4\tSymbols\n:""")
u = u.strip()
y = len(u)

if '1' in u:
    numUpper = random.randint(1,n/y)
    y-=1
    n-=numUpper
    for x in range(numUpper):
        uppercaseLetter=chr(random.randint(65,90))
        password+=uppercaseLetter
if '2' in u:
    print(y)
    numLower = random.randint(1,n/y)
    y-=1
    n-=numLower
    for x in range(numLower):
        lowercaseLetter=chr(random.randint(97,122))
        password+=lowercaseLetter
if '3' in u:
    numNum = random.randint(1,n/y)
    y-=1
    n-=numNum
    for x in range(numNum):
        number=chr(random.randint(48,57))
        password+=number
if '4' in u:
    numSym = n+1
    for x in range(numSym):
        symbol=chr(random.randint(33,46))
        password+=symbol

print(numUpper,numLower,numNum,numSym)
print(numUpper+numLower+numNum+numSym)
password = shuffle(password)
passwordList = list(password)
while len(passwordList) > m:
    passwordList.pop()
password = "".join(map(str,passwordList))
# password = str(password)
print("Printing password of length",len(password),'...')
print(password)


