
bizzarelist=[1,4,9,16,25,36]
x=91
print("coins left",x)
josuke = True
while x!=0:
    print("pick a number from the list (1,4,9,16,25,36)")
    jojo1 = int(input("player1 play>> "))
    while jojo1 not in bizzarelist or ((x-jojo1) < 0):
        jojo1 = int(input("player1 play again>> "))
    x-=jojo1
    if x == 0:
        print("player1 wins ")
        break
    print("coins left", x)
    print("pick a number from the list (1,4,9,16,25,36)")
    jojo2 = int(input("player2 play>> "))
    while jojo2 not in bizzarelist or ((x - jojo2) < 0):
        jojo2 = int(input("player2 play again>> "))
    x -= jojo2
    if x == 0:
        print("player2 wins ")
        break
    print("coins left", x)

















