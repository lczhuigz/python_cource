first_idiom = '万事如意'  		# 首个成语
end_str = first_idiom[-1]  		# 获取首个成语的末尾文字
new_li = [first_idiom]  		# 保存拼接后的成语，第一个元
li = ['发愤图强', '笑容满面', '意气风发', '强颜欢笑']  # 保存待接龙的成语
for index in range(len(li)):
    for i in li:
        if end_str == i[0]:  		# 判断前面成语的末尾文字与后续成语的开头文字是否相同
            new_li.append(i)     	# 将成语添加到new_li列表中
            li.remove(i)            # 删除已经完成接龙的成语
            end_str = i[-1]   		# 重新记录末尾文字
            break
print(new_li)
