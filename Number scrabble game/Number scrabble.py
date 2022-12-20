def display_score(player1,player2,player3):
    print("PLAYER1 : ",player1)
    print("PLAYER2 : ",player2)
    print("PLAYER3 : ",player3)


jojo_bizzare_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1,player2,player3=0,0,0
for i in range(1,4):
    print(jojo_bizzare_list)
    x = int(input("please pick a number player 1 >>"))
    while x < 1 or x > 9 or x not in jojo_bizzare_list:
        x = int(input("please pick a number player 1 >>"))
    jojo_bizzare_list.remove(x)
    print(jojo_bizzare_list)
    y = int(input("please pick a number player 2 >>"))
    while y < 1 or y > 9 or y not in jojo_bizzare_list:
        y = int(input("please pick a number player 2 >>"))
    jojo_bizzare_list.remove(y)
    print(jojo_bizzare_list)
    z = int(input("please pick a number player 3 >>"))
    while z < 1 or z > 9 or z not in jojo_bizzare_list:
        z = int(input("please pick a number player 3 >>"))
    jojo_bizzare_list.remove(z)
    print(jojo_bizzare_list)
    player1 += x
    player2 += y
    player3 += z
    display_score(player1, player2, player3)
    if player1 == 15:
        print("player 1 wins")
        break
    elif player2 == 15:
        print("player 2 wins")
        break
    elif player3 == 15:
        print("player 3 wins")
        break
if player1!=15 and player2!=15 and player3!=15:
    print("DRAW")
#jojo is the best anime
#this game was made by youssef 













