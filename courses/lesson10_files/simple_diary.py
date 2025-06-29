import datetime

今天 = datetime.date.today()
心情 = input("今天心情如何？")

# 决策理由：使用 'a' 模式来追加内容，而不是 'w' 覆盖，这样可以保留历史日记。
with open("日记.txt", "a", encoding="utf-8") as 日记:
    日记.write(f"{今天}: {心情}\n")

print("日记已保存！")
