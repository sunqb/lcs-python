# 课程4：文字处理 - 和计算机聊天

## 学习目标

- 学习如何处理文字（字符串）。
- 了解文字的连接和操作。
- 制作一个简单的聊天程序。

## 什么是字符串？

字符串就是文字，可以是一个字母、一个词，或者一整句话。在Python中，我们用引号把文字包起来。

```python
问候语 = "你好"
名字 = "小明"
句子 = "今天天气真好！"
```

## 连接文字

你可以把不同的文字连接在一起，就像拼积木一样。

```python
名字 = "小红"
问候 = "你好，" + 名字 + "！"
print(问候)
# 输出：你好，小红！
```

## 互动游戏：名字介绍

让我们制作一个程序，询问用户的名字，然后打招呼。

```python
# 简单版本（不需要用户输入）
用户名字 = "小明"  # 你可以改成自己的名字
问候语 = "你好，" + 用户名字 + "！欢迎来到编程世界！"
print(问候语)

# 更多信息
最喜欢的颜色 = "蓝色"  # 改成你最喜欢的颜色
介绍 = 用户名字 + "最喜欢" + 最喜欢的颜色 + "！"
print(介绍)
```

## 文字的长度

你可以数一数文字有多少个字符。

```python
我的名字 = "小明"
名字长度 = len(我的名字)
print("我的名字有", 名字长度, "个字")
# 输出：我的名字有 2 个字
```

## 练习项目：制作自我介绍卡片

创建一个文件`my_card.py`，制作你的专属介绍卡片：

```python
# 个人信息
姓名 = "小明"  # 改成你的名字
年龄 = 8      # 改成你的年龄
爱好 = "画画"  # 改成你的爱好

# 制作介绍卡片
print("=" * 20)  # 打印20个等号作为边框
print("   个人介绍卡片")
print("=" * 20)
print("姓名：" + 姓名)
print("年龄：" + str(年龄) + "岁")  # str()把数字变成文字
print("爱好：" + 爱好)
print("=" * 20)
```

### 如何运行这个程序？

1. 将代码保存为`my_card.py`。
2. 在终端中输入`python my_card.py`。
3. 看看你的专属介绍卡片！

## 练习

1. 修改上面的程序，添加你最喜欢的食物和颜色。
2. 尝试制作一个程序，显示"我叫[姓名]，我[年龄]岁，我最喜欢[爱好]！"

## 下一步

完成这个课程后，你将学习如何让计算机做选择（条件判断）。
