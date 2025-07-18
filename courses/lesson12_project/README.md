# 课程12：综合项目 - 制作你的游戏

## 学习目标
- 综合运用所有知识
- 制作完整的小游戏
- 展示你的编程技能

## 项目：猜数字游戏
```python
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
```

## 扩展项目：个人信息管理器
```python
学生信息 = []

def 添加学生():
    姓名 = input("学生姓名：")
    年龄 = int(input("学生年龄："))
    爱好 = input("学生爱好：")
    
    学生 = {
        "姓名": 姓名,
        "年龄": 年龄,
        "爱好": 爱好
    }
    
    学生信息.append(学生)
    print("学生信息已添加！")

def 显示所有学生():
    print("\n=== 所有学生信息 ===")
    for i, 学生 in enumerate(学生信息, 1):
        print(f"{i}. 姓名：{学生['姓名']}, 年龄：{学生['年龄']}, 爱好：{学生['爱好']}")

# 简单菜单
while True:
    print("\n1. 添加学生")
    print("2. 显示所有学生")
    print("3. 退出")
    
    选择 = input("请选择操作：")
    
    if 选择 == "1":
        添加学生()
    elif 选择 == "2":
        显示所有学生()
    elif 选择 == "3":
        print("再见！")
        break
    else:
        print("无效选择，请重新输入。")
```

## 恭喜完成课程！
你已经学会了：
- 基本的Python语法
- 变量和数据类型
- 条件判断和循环
- 函数和文件操作
- 用户交互和绘图

继续练习，你会成为优秀的程序员！
