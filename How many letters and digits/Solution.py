jojo=[]
t=input("please enter your string>> ")
digits = 0
letters= 0
for letter in t:
    if (letter.isdigit()):
        digits = digits+1
    elif(letter.isalpha()):
        letters=letters+1
print("Digits ={}".format(digits),end=" ")
print("letters ={}".format(letters),end="")