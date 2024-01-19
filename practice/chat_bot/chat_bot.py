import random

# ___________ 模拟机器人聊天软件___________
print("欢迎使用机器人聊天1.0")
print("使用指南: 你可以问我任何问题, 我会知无不言言无不尽! 输入再见 '886' 对话.")
print("_______________________________________________")
print("你好, 请问有什么需要帮助的吗?")

ipt = input()
while input != 886:
    num = random.randint(0, 33)
    if num == 1:
        ipt = input("谢谢你的提问, 你喜欢吃辣吗?\n")
    elif num == 2:
        ipt = input("哦, 这都不知道是吗? 真了不起! 你觉得呢?\n")
    elif num == 3:
        ipt = input("啊? 我不太清楚, 真的不知道吗?\n")
    elif num == 4:
        ipt = input("真不错! 为你高兴呢? 还有什么问题?\n")
    elif num == 5:
        ipt = input("呵呵, 真喜欢跟你聊天! \n")
    elif num == 6:
        ipt = input("啊? 我不知道耶, 换个话题吧?\n")
    elif num == 7:
        ipt = input("真有你的, 我也不知道, 还有吗?\n")
    elif num == 8:
        ipt = input("真好玩啊, 你来告诉我一些吧!\n")
    elif num == 9:
        ipt = input("哈哈, 太棒了! 然后呢?\n")
    elif num == 10:
        ipt = input("啊? 为什么呢?\n")
    elif num == 11:
        ipt = input("So? 你想表达什么?\n")
    elif num == 12:
        ipt = input("快说些别的把! \n")
    elif num == 13:
        ipt = input("哎呀! 可真有你的! 这都不懂?\n")
    elif num == 14:
        ipt = input("不然呢! 你还能怎样?\n")
    elif num == 15:
        ipt = input("真是恐怖! 还有什么?\n")
    elif num == 16:
        ipt = input("啊? 这个话题....不太好吧?\n")
    elif num == 17:
        ipt = input("哈哈? 可说呢? 真是的! \n")
    elif num == 18:
        ipt = input("Really? 简直了! 继续. \n")
    elif num == 19:
        ipt = input("是吗? 快讲讲, 快讲讲!\n")
    elif num == 20:
        ipt = input("哎! 那有什么办法啊?\n")
    elif num == 21:
        ipt = input("去去去, 小孩子懂得什么?\n")
    elif num == 22:
        ipt = input("这个事情可不好说.\n")
    elif num == 23:
        ipt = input("哎, 连爱因斯坦恐怖也搞不清楚! \n")
    elif num == 24:
        ipt = input("不能比这个问题还有趣了吧? \n")
    elif num == 25:
        ipt = input("那个...啊?  你在说什么?\n")
    elif num == 26:
        ipt = input("我去, 不是吧, 这也问? 太夸张了啊!\n")
    elif num == 27:
        ipt = input("那是! 你也不想想, 怎么可能?\n")
    elif num == 28:
        ipt = input("你不要这样说好不好?\n")
    elif num == 29:
        ipt = input("话可不能这么说.\n")
    elif num == 30:
        ipt = input("诶? 何出此言啊? \n")
    elif num == 31:
        ipt = input("自古有云: 云什么来着? \n")
    elif num == 32:
        ipt = input("你再好好想想吧?\n")
    elif num == 33:
        ipt = input("要说对吧, 也不完全对, 不对吧? 又似乎有道理! \n")
    else:
        ipt = input("你这句话说的, 我都不知道怎么反驳! \n")

print("跟你聊天真开心, 再见!")
# -------------------------------
