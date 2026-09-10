user_points = 7500
user_purchases = 800
if user_points >= 10000 and user_purchases >= 1000:
    print("钻石会员")
elif user_points >= 5000 and user_purchases >= 500:
    print("白金会员")
elif user_points >= 2000 and user_purchases >= 200:
    print("黄金会员")
elif user_points >= 1000 and user_purchases >= 100:
    print("白银会员")
elif user_points >= 500:
    print("青铜会员")
else:
    print("普通会员")

