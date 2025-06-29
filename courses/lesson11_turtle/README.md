# 课程11：绘图游戏 - 用代码画画

## 学习目标
- 学习turtle绘图模块
- 制作简单的图形
- 创作艺术作品

## 基本绘图
```python
import turtle

# 创建画笔
画笔 = turtle.Turtle()

# 画正方形
for _ in range(4):
    画笔.forward(100)  # 前进100像素
    画笔.right(90)     # 右转90度

turtle.done()  # 保持窗口打开
```

## 彩色图形
```python
import turtle

画笔 = turtle.Turtle()
画笔.color("red")  # 设置颜色

# 画彩色三角形
for _ in range(3):
    画笔.forward(100)
    画笔.left(120)

turtle.done()
```

## 练习项目：彩虹花朵
```python
import turtle

画笔 = turtle.Turtle()
画笔.speed(10)  # 设置速度

颜色列表 = ["red", "orange", "yellow", "green", "blue", "purple"]

for 颜色 in 颜色列表:
    画笔.color(颜色)
    画笔.circle(50)  # 画圆
    画笔.right(60)   # 旋转

turtle.done()
```
