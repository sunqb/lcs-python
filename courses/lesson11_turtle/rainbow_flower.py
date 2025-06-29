import turtle

画笔 = turtle.Turtle()
画笔.speed(10)  # 设置速度

颜色列表 = ["red", "orange", "yellow", "green", "blue", "purple"]

# 决策理由：使用循环和颜色列表，让孩子直观地看到代码如何创造出多彩的图案，激发兴趣。
for 颜色 in 颜色列表:
    画笔.color(颜色)
    画笔.circle(50)  # 画圆
    画笔.right(60)   # 旋转

画笔.hideturtle() # 隐藏画笔
turtle.done()  # 保持窗口打开
