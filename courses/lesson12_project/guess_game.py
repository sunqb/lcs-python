import random

print("=== 猜数字游戏 ===")
print("我想了一个1到10的数字，你能猜到吗？")

神秘数字 = random.randint(1, 10)
猜测次数 = 0
最大次数 = 3

while 猜测次数 < 最大次数:
    try:
        玩家猜测 = int(input(f"第{猜测次数 + 1}次猜测，请输入数字："))
        猜测次数 += 1
        
        if 玩家猜测 == 神秘数字:
            print("🎉 恭喜你猜对了！")
            break
        elif 玩家猜测 > 神秘数字:
            print("太大了！")
        else:
            print("太小了！")
            
        if 猜测次数 == 最大次数:
            print(f"游戏结束！答案是 {神秘数字}")
    except:
        print("请输入有效数字！")
        猜测次数 -= 1

print("感谢游玩！")
