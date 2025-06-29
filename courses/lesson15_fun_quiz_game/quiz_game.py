import random

# 问题和答案
questions = {
    "中国的首都是哪里？": "北京",
    "世界上最大的动物是什么？": "蓝鲸",
    "一年有多少天？": "365"
}

# 游戏开始
print("欢迎来到问答游戏！")
score = 0

# 随机提问
for question in random.sample(list(questions.keys()), len(questions)):
    answer = input(question + " ")
    if answer == questions[question]:
        print("回答正确！")
        score += 1
    else:
        print("回答错误！正确答案是：" + questions[question])

# 游戏结束
print("游戏结束！你的得分是：" + str(score))
