# 课程14：实验课 - 进阶海龟绘图

## 学习目标
- 学习更高级的`turtle`动画技巧。
- 掌握如何使用循环和函数创建动态效果。
- 创作一个旋转的风车动画。

## 动画原理
动画就是快速连续播放一系列静态图片。在`turtle`中，我们可以通过不断清空画布并重新绘制图形来实现动画效果。

## 关键函数
- `turtle.tracer(0)`: 关闭自动刷新，让我们手动控制画面更新。
- `turtle.update()`: 手动刷新画布，显示我们画好的内容。
- `while True`: 创建一个无限循环来持续播放动画。
- `turtle.clear()`: 清除画布上的所有内容，为下一帧做准备。

## 示例代码：`animated_windmill.py`
这个程序会画一个不断旋转的风车。

```python
import turtle
import time

# 设置画布
screen = turtle.Screen()
screen.title("旋转的风车")
screen.bgcolor("skyblue")

# 创建画笔
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

def draw_blade(color):
    """画一个风车叶片"""
    pen.color(color)
    pen.begin_fill()
    pen.forward(100)
    pen.left(90)
    pen.forward(20)
    pen.left(90)
    pen.forward(100)
    pen.end_fill()

def draw_windmill(angle):
    """画整个风车"""
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(angle)
    pen.pendown()

    # 画四个叶片
    draw_blade("red")
    pen.setheading(angle + 90)
    draw_blade("blue")
    pen.setheading(angle + 180)
    draw_blade("green")
    pen.setheading(angle + 270)
    draw_blade("yellow")

    # 画中心圆
    pen.penup()
    pen.goto(0, -5)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    pen.circle(5)
    pen.end_fill()

# 动画循环
screen.tracer(0)  # 关闭自动刷新
rotation_angle = 0

while True:
    pen.clear()  # 清除上一帧
    draw_windmill(rotation_angle) # 画新的一帧
    screen.update()  # 更新画布

    rotation_angle += 5  # 增加旋转角度
    time.sleep(0.05)  # 短暂延迟，控制动画速度

turtle.done()

```

## 如何运行？
1.  将代码保存为`animated_windmill.py`并运行。
2.  你会看到一个彩色的风车不停地旋转。

## 挑战一下
- 尝试改变风车的颜色或叶片形状。
- 增加一个背景，比如草地或房子。
- 让风车的旋转速度变化，比如越转越快。

## 下一步
挑战最后一个实验课，制作一个有趣的问答游戏！
