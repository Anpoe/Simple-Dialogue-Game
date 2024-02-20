import os
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 5
        self.atk = 2
        self.defs = 3
        self.san = 5
    def dead_to_me(self):
        if self.hp < 0:
            while True:
                print("你死了。哦，这句话和你本人一样毫无意义。你的葬礼也在我说完这句话后结束了，但说实话，除了我，谁会在意呢？")
                end2 = input("重新寻找吗？(Y/N)\n")
                if end2 in ['Y','y']:
                    print("好吧。那么再来一次。")
                    input()
                    break
                if end2 in ['N','n']:
                    exit(0)
        if self.san < 0:
            print("或许知道自己是谁并不重要，最重要的是你体验了这个过程，不是吗？\n等等，老天，你真的这么想？一辈子呆在这里，没有人，没有手机，没有电视，和你的'墓碑'一起消亡，变成这个白色房间的食物，你甘心吗？")
            end1 = input("你还是去死吧。\n A.好吧。 \n B.去你的！\n")
            if end1 in ['A','a']:
                while True:
                    print("那么就结束了，与你相处的这段时间可以排上我职业生涯'无聊到想去死'排行榜前三名。")
                    end2 = input("重新寻找吗？(Y/N)\n")
                    if end2 in ['Y','y']:
                        print("好吧。那么再来一次。")
                        input()
                        break
                    if end2 in ['N','n']:
                        exit(0)
            else:
                while True:
                    print("你不会以为这个选项真的能改变什么吧？说真的，你的崩溃简直无聊透顶。")
                    end2 = input("重新寻找吗？(Y/N)\n")
                    if end2 in ['Y','y']:
                        print("好吧。那么再来一次。")
                        input()
                        break
                    if end2 in ['N','n']:
                        exit(0)
    def to_win(self):
        if self.san > 10:
            print("赞美你！你已经完全掌握了这个游戏的玩法，只要大搞破坏就够了！毁灭一切，你就是超新星，核弹，燃烧着的太阳，把这种美好的态度带到现实中去吧！ \n ——THE END——")
            input()
            exit(0)
        if self.hp >= 10:
            print("真有你的，在这个空空荡荡的地方大搞行为艺术，你要知道我放你出去并不是因为你有多出色，只是我可受够你了！")
            input()
            print("好了，快滚吧！你就是你，千千万万个普通人中的一个罢了，我已经对你感到十分无趣了，就像是在澡堂里搓澡，前面十分钟是享受，但后面嘛... \n 总之别多想，好吗，也不用对自己产生什么怀疑，这只是一个无聊的人创造的一个无聊的游戏罢了，无聊到明知道你并不在意，但还是絮絮叨叨。\n ——THE END——") 
            input()
            exit(0)              
def main(player: Player):
    count = 0
    try:
        while True:
            count += 1
            print(f"第{count}次，你看见了。")
            name = input("请输入玩家名字：")
            print("\n ————读取数据中————")
            input()
            print(f"SAN={player.san} \nHP={player.hp}")
            input()
            print("初始化...")
            input()
            print("模拟开始。")
            input()
            print(f"{name}从房间里醒来，陌生的天花板，白色的，从中心开始慢慢延伸出裂痕，像一张覆盖住整个房间的蜘蛛网。")
            print("你感到无所适从，凉意像蝌蚪一样从你的背脊爬上脖子，失去意识前的记忆早已模糊不清，你是谁？有着什么样的过去？希冀与什么样的未来？没有人关心。在一个空荡荡的房间里，你本人一文不值，如果想要得到你曾经拥有的，现在的当务之急就是逃出去。")
            print("你环顾四周，白色，白色，白色。像是关押精神病人的牢房，唯一的不同就是这里没有任何东西可以阻止你自寻死路。")
            input()
            action1 = input("你的行动是？\n A.睡一觉吧。\n B.打开床头柜看看 \n C.试图开门\n")
            if action1 in ['A', 'a']:
                while True:
                    print("\n 既然你不在意，那么这个世界也不会给你回答，你再也没有醒来这个事实，你也不会知道了。\n ——THE END——")
                    input()
                    end2 = input("重新寻找吗？(Y/N)")
                    if end2 in ['Y','y']:
                        print("好吧。那么再来一次。")
                        input()
                        break
                    if end2 in ['N','n']:
                        exit(0)
                        
            elif action1 in ['B', 'b']:
                print("床头柜里放着一把锤子，你拿起来挥了挥，沉甸甸的感觉让你在这个世界中找到了那么一点实感。")
                player.atk += 1
                input()
                action2 = input("原谅我的好奇心，你要用这把锤子干些什么呢？ \n A.向窗玻璃丢去 \n B.还能干什么？当然是砸自己的头啦！ \n C.向着门把手轮一锤子\n")
                if action2 in ['A', 'a']:
                    print("锤子自由飞行，飞呀飞，然后它出去了！冲破了牢笼！你的手再也握不住它了，它已经从人类的禁锢中自由了。")
                    input()
                    print("你向窗外看去（别担心，这不需要选择，更不会消耗你的行动点，你只是做了每个人看见飞出去的锤子时本能想干的事情——它落在哪了？）。")
                    input()
                    print("很可惜，你已经永远失去它了，就像理查三世从马上掉下来时绝望地意识到的那样。下面是郁郁葱葱的树叶，生锈的水管，散碎的纸屑，唯独没有你可爱的锤子。")
                    print("你可算是完蛋了，把唯一一件能排上用场的工具丢掉？真有你的。")
                    player.san -= 10
                    player.atk -= 1
                    player.dead_to_me()
                elif action2 in ['B', 'b']:
                    print("好主意！这可真是你人生的高光时刻，到头来总算是为社会干了件好事。")
                    player.hp -= 7
                    player.dead_to_me()
                else:
                    print("门纹丝不动，它高大而沉默，你站在它面前，想象那是你的墓碑。")
                    player.san -= 1
                    action3 = input("别想了，这东西暂时派不上用场，干点什么别的吧。\n A. 把所有的一切都砸烂。\n B. 祈祷吧，用这个锤子，它看起来像是一个断掉的十字架。\n C. 你可以用它在地板上挖一个洞，彻头彻尾的《肖申克的救赎》。\n")
                    if action3 in ['A', 'a']:
                        print("好主意！我是认真的，毁灭才是人生的真谛，什么思考，谋略，统统都不需要———")
                        player.san += 10
                        player.to_win()
                    elif action3 in ['B', 'b']:
                        print("很有想象力...但你要向谁祈祷呢？我吗？好吧，算你赢了，相信一个存在又不存在的事物已经够让人感到悲哀了。")
                        player.hp += 10
                        player.to_win()
                    else:
                        print("人类果然是神奇的生物，告诉我，你是不是那种社交恐惧，只会用电影里的情节来模拟代入真实的社交，真实的生活。如果没有了电影，你是不是连该怎么和一个人说爱你都不知道？")
                        player.san -= 10
                        player.dead_to_me()                       
            else:
                print("就在那一瞬间，你感到一切都脱离了你的控制，你像是漂浮在太空中的垃圾，无人问津但又惹人生厌。这可太悲哀了，沉默着，飞行着，然后渐渐变冷...")
                player.san -= 10
                player.dead_to_me()
    except Exception:
        print("实验遇到了无法逆转的问题...强制抽离...")
        
if __name__ == '__main__':
    player = Player('')
    main(player)

os.system("pause")