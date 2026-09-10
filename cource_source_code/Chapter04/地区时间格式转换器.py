# 用户输入的时间信息
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
hour = int(input("请输入小时："))
minute = int(input("请输入分钟："))
second = int(input("请输入秒钟："))

country = input("请输入要转换的国家（中国、美国、英国、德国、俄罗斯、澳大利亚、法国、加拿大）：")

# 转换为指定国家的时间格式
if country == '中国':
    formatted_time = f"{year:04d}年{month:02d}月{day:02d}日 {hour:02d}:{minute:02d}:{second:02d}"
elif country == '美国':
    formatted_time = f"{month:02d}/{day:02d}/{year:04d} {hour:02d}:{minute:02d}:{second:02d}"
elif country == '英国' or country == '澳大利亚' or country == '法国':
    formatted_time = f"{day:02d}/{month:02d}/{year:04d} {hour:02d}:{minute:02d}:{second:02d}"
elif country == '德国' or country == '俄罗斯':
    formatted_time = f"{day:02d}.{month:02d}.{year:04d} {hour:02d}:{minute:02d}:{second:02d}"
elif country == '加拿大':
    formatted_time = f"{year:04d}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
else:
    formatted_time = '不支持该国家的时间格式转换'
print(formatted_time)