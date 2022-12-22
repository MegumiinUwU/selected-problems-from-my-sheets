Egypt = { "Cairo":"7,734,614",
"Alexandria":"3,811,516",
"Giza":"2,443,203",
"Port said" :"538,378",
"Suez":"488,125",
"Al mahallah al kubra":"431,052",
"Luxor":"422,407",
"Asyut":"420,585",
"Al mansurah":"420,195",
"Tanta":"404,901",
}

def listcities():
    print(Egypt.keys())

def choosecity():
    x=input("please enter the city name>>")
    x=x.capitalize()
    if x in Egypt:
        print(Egypt[x])
    else:
        print("This city doesn't exist")

def addnewcity():
    jojo = input("Please enter the city name>>")
    while jojo.isalpha()==False:
         jojo=input("Please enter the city name>>")
    eren=input("Please enter the city's population>>")
    while eren.isnumeric()==False:
        eren = input("Please enter the city's population>>")
    Egypt[jojo] = eren
    print(Egypt)

b= True
while b:
    joestar = int(input("Please enter a numper\n 1.View all cities\n 2.Add new city\n 3.Access city \n 4.End\n >>>>>"))
    while joestar<1 or joestar>4:
         joestar=int(input("Please enter a numper\n 1.View all cities\n 2.Add new city\n 3.Access city \n 4.End\n >>>>>"))

    if joestar==1:
        listcities()
    elif joestar==2:
        addnewcity()

    elif joestar==3:
        choosecity()
    elif joestar==4:
        break
print("Thanks for using our program")




