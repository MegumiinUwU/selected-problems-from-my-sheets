def fib(n):
    jojo=[]
    a,b=1,1
    for i in range(0,n):
        jojo.append(a)
        a,b=b,b+a
    print(jojo)
luffy=int(input("please enter the lenght >>"))
fib(luffy)
