# 课程10：文件操作 - 保存你的作品

## 学习目标
- 学习读写文件
- 保存和读取数据
- 制作日记程序

## 写入文件
```python
# 写入文件
with open("我的日记.txt", "w", encoding="utf-8") as 文件:
    文件.write("今天天气很好！\n")
    文件.write("我学会了Python编程。")
```

## 读取文件
```python
# 读取文件
with open("我的日记.txt", "r", encoding="utf-8") as 文件:
    内容 = 文件.read()
    print(内容)
```

## 练习项目：简单日记
```python
import datetime

今天 = datetime.date.today()
心情 = input("今天心情如何？")

with open("日记.txt", "a", encoding="utf-8") as 日记:
    日记.write(f"{今天}: {心情}\n")

print("日记已保存！")
```
