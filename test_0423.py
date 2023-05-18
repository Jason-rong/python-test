# 常见数据类型
# 整型-int类型
# 浮点型-小数类型
# 布尔类型-True,False
# str 字符串类型
# 列表-数组[1,2,3]
# 元组-集合{1,2,3}
# 字典-map{key:value}
age = 18
print(type(age))
print(f"我的年龄是：{age}")
st = True
print(type(st))

# 编写一个程序，查找所有此类数字，它们可以被7整除，但不能是5的倍数（在2000和3200之间（均包括在内））。获得的数字应以逗号分隔的顺序打印在一行上
numList = []
for i in range(2000,3201):
    if(i % 7 == 0) and (i % 5 != 0):
        numList.append(str(i))
print(','.join(numList))