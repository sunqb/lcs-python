import time

def print_slow(text):
    """一个让文字慢慢打印的函数，增加神秘感"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def show_intro():
    """显示游戏介绍"""
    print_slow("你在一座古老的城堡里醒来，头有点晕...")
    print_slow("你发现大门被锁住了，必须找到钥匙才能离开。")
    print_slow("祝你好运，冒险家！")
    print("-" * 30)

def play_game():
    """游戏主函数"""
    current_room = "大厅"
    has_key = False
    show_intro()

    while True:
        print_slow(f"\n你现在在【{current_room}】。")

        if current_room == "大厅":
            print_slow("你看到一个通往“书房”的门，还有一个紧锁的“宝箱室”。")
            print_slow("桌上有一张纸条。")
            choice = input("你要做什么？(1.去书房, 2.查看纸条, 3.去宝箱室) > ")
            if choice == "1":
                current_room = "书房"
            elif choice == "2":
                print_slow("纸条上写着：\'知识就是力量，钥匙藏在智慧的海洋里。\'")
            elif choice == "3":
                if has_key:
                    print_slow("你用钥匙打开了宝箱室的门...")
                    current_room = "宝箱室"
                else:
                    print_slow("门锁着，你需要钥匙。")
            else:
                print_slow("无效的选择。")

        elif current_room == "书房":
            print_slow("书房里有很多书架，充满了古老的书籍。")
            print_slow("一个书架上有一个闪闪发光的东西。")
            choice = input("你要做什么？(1.检查闪光的东西, 2.返回大厅) > ")
            if choice == "1":
                if not has_key:
                    print_slow("你找到了钥匙！现在可以去打开宝箱室的门了。")
                    has_key = True
                else:
                    print_slow("你已经有钥匙了。")
            elif choice == "2":
                current_room = "大厅"
            else:
                print_slow("无效的选择。")

        elif current_room == "宝箱室":
            print_slow("你打开了宝箱，里面没有金银财宝，只有一条通往外面的密道！")
            print_slow("恭喜你，成功逃离了城堡！🎉")
            break  # 游戏结束

# 开始游戏
play_game()
