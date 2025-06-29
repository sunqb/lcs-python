购物清单 = []
购物清单.append("牛奶")
购物清单.append("面包")
购物清单.append("鸡蛋")

print("=== 我的购物清单 ===")
for i, 商品 in enumerate(购物清单, 1):
    print(f"{i}. {商品}")
