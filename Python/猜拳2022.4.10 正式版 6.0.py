#重复执行，添加扩展随机数，定义电脑和玩家的变量，电脑为随机数
while True:
    import random
    player = int(input("请输入数字来和电脑猜拳：1=石头，2=剪刀，3=布"))
    computer = random.randint(1,3)
    
#显示玩家出拳
    if player == 1:
        print("你出拳为：石头")
    if player == 2:
        print("你出拳为：剪刀")
    if player == 3:
        print("你出拳为：布")

#显示电脑出拳
    if computer == 1:
        print("电脑出拳为：石头")
    if computer == 2:  
        print("电脑出拳为：剪刀")
    if computer == 3: 
        print("电脑出拳为：布")

#判断输赢
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print("你赢了！")

    elif player == computer:
        print("平局！")

    else:
        print("你输了！")