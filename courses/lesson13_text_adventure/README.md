# 课程13：实验课 - 文字冒险游戏

## 学习目标
- 综合运用循环、函数和条件判断。
- 学习如何构建一个简单的游戏循环。
- 激发逻辑思维和故事创作能力。

## 游戏设计
我们将制作一个简单的文字冒险游戏。玩家在一个神秘的城堡里醒来，需要找到钥匙才能逃脱。

- **场景**：城堡有三个房间：大厅、书房、宝箱室。
- **目标**：在大厅找到书房的线索，去书房找到钥匙，最后打开宝箱室的门逃脱。

## 游戏主循环
游戏的核心是一个`while`循环，它会一直运行，直到玩家获胜或失败。

```python
# 伪代码
当前位置 = "大厅"
while True:
    显示当前位置和选项()
    玩家输入 = 获取玩家选择()
    处理玩家输入(玩家输入)
    if 游戏结束:
        break
```

## 示例代码：`adventure_game.py`
这是完整的游戏代码，你可以直接运行它，也可以尝试修改它，创造你自己的冒险故事！

```python
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
                print_slow("纸条上写着：'知识就是力量，钥匙藏在智慧的海洋里。'")
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
```

## 如何运行和修改？
1.  将代码保存为`adventure_game.py`并运行。
2.  **挑战一下**：
    *   增加更多的房间，比如“厨房”或“花园”。
    *   在房间里添加更多可以互动的东西。
    *   设置一些谜题，比如需要回答问题才能拿到钥匙。

## 下一步
完成这个游戏后，你可以挑战下一个实验课，学习如何用代码制作动画！
