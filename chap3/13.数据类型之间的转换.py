x = 10
y = 3
z = x/y  # 在执行除法运算，将运算的结果赋值给z
print(z, type(z))  # 隐式转换，通过运算隐式的转了结果的数据类型

# float类型转换成int类型，只保留整数部分
print('float类型转换成int类型', int(3.14))
print('float类型转换成int类型', int(3.9))
print('float类型转换成int类型', int(-3.14))
print('float类型转换成int类型', int(-3.9))

# 将int类型转换成float类型
print('将int类型转换成float类型', float(10))

