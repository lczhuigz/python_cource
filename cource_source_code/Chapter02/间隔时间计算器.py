# 输入起始时间
start_hour = int(input("请输入起始时间的小时数："))
start_minute = int(input("请输入起始时间的分钟数："))

# 输入结束时间
end_hour = int(input("请输入结束时间的小时数："))
end_minute = int(input("请输入结束时间的分钟数："))

# 计算时间间隔
start_total_minutes = start_hour * 60 + start_minute  # 将起始时间转换为分钟数
end_total_minutes = end_hour * 60 + end_minute  # 将结束时间转换为分钟数

duration_minutes = end_total_minutes - start_total_minutes  # 计算时间段的总分钟数
duration_hour = duration_minutes // 60  # 将分钟数转换为小时数
duration_minute = duration_minutes % 60  # 计算剩余的分钟数

# 输出结果
print("时间间隔为：", duration_hour, "小时", duration_minute, "分钟")
