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
