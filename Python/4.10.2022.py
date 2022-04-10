#1.
#chinese = int(input("语文多少分？"))
#math = int(input("数学多少分？"))
#if chinese == 100 and math == 100:
#    print("迪士尼走起")
#elif chinese >= 95 and math >= 95:
#    print("方特走起")
#elif chinese >= 90 and math >=90:
#    print("去吃火锅")
#elif chinese >= 85 and math >= 85:
#    print("继续努力，争取考上90")
#else:
#    print("争取下次考到90分")






#2.
#knife = int(input("你这大刀多少米长？"))
#ticket = bool(input("买票没？"))

#if knife < 40:
#    print("请去检票")
#    if ticket:
#       print("可以进站")
#   else:
#        print("请先去买票")
#else:
#    print("安检未通过，禁止携带超过40米的刀具")




#3.
#import random
#a = random.randint(10,14)
#b = random.randint(13,14)
#c = random.randint(1,14)
#print(a,b,c)









#4.

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