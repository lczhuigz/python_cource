# num = float(input("请输入要转换的数字（例如123456789.10）："))
digits = ("零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖")
units = ("", "拾", "佰", "仟", "万", "拾万", "佰万", "仟万", "亿")

number = 123456
num_str = str(number)
length = len(num_str)

if number == 0:
    result = "零"
else:
    result = ""
    for i in range(length):
        digit = int(num_str[i])
        if digit != 0:
            result += digits[digit] + units[length - i - 1]
        else:
            if len(result) > 0 and result[-1] != digits[0] and units[length - i - 1] != units[4]:
                result += digits[digit]

print(result)  # 输出：壹拾贰万叁仟肆佰伍拾陆