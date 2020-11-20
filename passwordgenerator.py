alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alpharep = alpha.copy()

num = ['1','2','3','4','5','6','7','8','9','0']

numrep = num.copy()

spechar=['@','@','#','#','&','&','$','$','_','_','!','!','?','?','/','/','*','*',':',':','%','%','[',']','{','}','(',')','<','>','+','+']

specharep = spechar.copy()

import random as r
print("Password Strength:","-"*53)
print("WEAKER: Password contains only Alphabets")
print("WEAK: Password contains both Alphabets and Numbers")
print("STRONG: Password contains both Alphabets and Specialcharacters")
print("STRONGER: Password contains Alphabets, Numbers andSpecial characters")
print("-"*72)


q = False
while q!=True:
    ch = input("Enter your option: ")
    ch = ch.lower()
    if (ch=="weaker" or ch=="weak" or ch=="strong" or ch=="stronger"):
        q = True

print("-"*72)
print("Password Length:","-"*55)
print("1 to 50: Password containing only Alphabets")
print("1 to 60: Password containing both Alphabets and Numbers")
print("1 to 70: Password containing both Alphabets and Special characters")
print("1 to 80: Password containing Alphabets, Numbers and Special characters")
print("-"*72)


p = False
while (p!=True):
    try:
        length = int(input("Enter a number: "))
    except ValueError:
        continue
    if (ch=="weaker"):
        if (length<=50 and length>0):
            p = True
    elif (ch=="weak"):

        if(length<=60 and length>0):
            p = True
    elif (ch=="strong"):
        if(length<=70 and length>0):
            p = True
    elif (ch=="stronger"):
        if(length<=80 and length>0):
            p = True

print("-"*72)


l = len(alpha + alpharep + num + spechar)
pwd =[]
r.shuffle(alpha)
r.shuffle(alpharep)
r.shuffle(num)
r.shuffle(numrep)
r.shuffle(spechar)
r.shuffle(specharep)


if ch=="weaker":
    pwd = alpha + alpharep
elif ch=="weak":
    pwd = alpha + alpharep + num + numrep
elif ch=="strong":
    pwd = alpha + alpharep + spechar + specharep
elif ch=="stronger":
    pwd = alpha + alpharep + num + numrep + spechar + specharep
r.shuffle(pwd)

z = False
while(z!=True):
    pwd.pop()
    l2 = len(pwd)
    if (l2==length):
        z =True
    else:
        continue
pwd = ''.join(pwd)
pwd = pwd.upper()
pwd = pwd.replace('',' ')
pwd = pwd.strip()
print("Password: ",pwd)
print("-"*72)