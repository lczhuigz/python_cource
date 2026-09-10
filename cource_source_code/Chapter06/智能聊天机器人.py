problem_dict = {
    "诗仙是谁": "李白",
    "中国第一个朝代": "夏朝",
    "三十六计的第一计是什么": "瞒天过海",
    "天府之国是中国的哪个地方": "四川",
    "中国第一长河": "长江"
}

work = True    # 工作标记，用于记录机器人是否回答了用户提出的问题，默认为是
flag = "c"     # 状态标记，默认为聊天状态

def train(arg_question, arg_answer):
    # 增加新问题及其答案
    problem_dict[arg_question] = arg_answer
    print(f"小智：训练成功，我现在会回答{len(problem_dict)}个问题了！")
    # 按照固定格式输出问题与答案
    print("--------------------")
    num = 1
    for key in problem_dict.keys():
        print(str(num) + "、" + key)
        num += 1
    print("--------------------")

def exchange(words):
    global work
    for key in problem_dict.keys():
        if words == key:   # 如果用户提出的问题存在问题库
            print(f"小智：{problem_dict[key]}")  # 输出答案
            work = True     # 更新工作标记
            break
        else:                # 如果用户提出的问题不在问题库
            work = False    # 更新工作标记
    if not work:            # 如果机器人没回答问题
        print("小智：抱歉，这个问题我还不会回答！")
        work = True         # 更新工作标记

print("小智：你好，我是小智！")
while flag == "c" or flag == "t":
    input_flag = input("你可以选择和我聊天（c）训练对话（t）让我离开（l）\n我：")
    if input_flag in ["c", "t", "l"]:
        flag = input_flag   # 修改机器人的状态标志
    if input_flag == "t":  # 训练机器人
        question = input("小智：请输入问题\n我：")
        answer = input("小智：请输入答案\n我：")
        train(question, answer)
        continue
    elif input_flag == "c":  # 跟机器人对话
        if len(problem_dict) == 0:
            print("小智：我现在还不会回答哦，请先训练我！")
            continue
        char_word = input("小智：很开心和你聊天，你想问我什么!\n我：")
        exchange(char_word)
    elif input_flag == "l":  # 退出
        print("小智：好的，下次再见！")
        break
    else:  # 输入不合法信息
        print("小智：请输入正确的指令！")
