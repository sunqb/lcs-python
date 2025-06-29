print("=== 小小计算器 ===")

# 加法练习
print("加法练习：")
for i in range(1, 6):
    结果 = i + i
    print(i, "+ ", i, " = ", 结果)

print("\n乘法练习：")
# 乘法练习
for i in range(1, 6):
    结果 = i * 2
    print(i, "× 2 = ", 结果)

print("\n数数练习：")
# 数数练习
for 数字 in range(10, 0, -1):
    print("还剩", 数字, "个")
print("全部数完了！")
