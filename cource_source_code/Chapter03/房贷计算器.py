while True:
    loan_type = input("请选择贷款类型（商业贷款/公积金贷款）(输入exit退出程序): ")
    if loan_type == "exit":    # 退出房贷计算器
        break

    loan_years = int(input("请选择贷款期限（年）："))
    if loan_type == "商业贷款":
        if loan_years <= 5:         # 商业贷款的贷款期限小于或等于5年
            interest_rate = 0.0475
        else:      # 商业贷款的贷款期限大于5年
            interest_rate = 0.049
    elif loan_type == "公积金贷款":
        if loan_years <= 5:         # 公积金贷款的贷款期限小于或等于5年
            interest_rate = 0.026
        else:   # 公积金贷款的贷款期限大于5年
            interest_rate = 0.031
    else:     # 无效的贷款类型
        print("无效的贷款类型，请重新输入！")
        continue

    loan_amount = float(input("请输入贷款金额（元）: "))
    # 贷款期限的总月数
    loan_term = loan_years * 12
    # 计算月利率
    monthly_interest_rate = interest_rate / 12
    total_payments = loan_term
    # 计算每月月供参考
    monthly_payment = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) \
                      / ((1 + monthly_interest_rate) ** total_payments - 1)
    # 计算还款总额
    total_payments_amount = monthly_payment * total_payments
    # 计算支付利息
    total_interest = total_payments_amount - loan_amount

    print("----------------------------------------")
    print("每月月供参考:", monthly_payment, "元")
    print("支付利息:", total_interest, "元")
    print("还款总额:", total_payments_amount, "元")
