import jieba

# 读取txt文件
txt = open("lizhinews.txt", "r", encoding='utf-8')
myDict1 = dict()
myDict2 = dict()
myDict3 = dict()
myDict4 = dict()

# 心态词词典
mood = ["好", "怕", "无感", "关心", "提心吊胆", "担心", "不好", "痛苦", "激动", "可惜",
        "大不了", "喜欢", "乐观", "牛", "可怕", "窘迫", "恐惧", "痛", "燃", "鼓掌",
        "满足", "良好", "信心", "强", "平稳", "治愈", "放松", "松懈", "自觉", "温暖",
        "开心", "喜悦", "狂喜", "尽情", "快乐", "愉悦", "畅快", "欣喜", "幸福", "得意",
        "痛快", "满足", "欢乐", "快活", "陶醉", "甜美", "微笑", "兴奋", "自豪", "欣慰",
        "高兴", "满意", "心烦", "失落", "伤感", "忧伤", "委屈", "绝望", "哭泣", "伤心",
        "痛苦", "悲伤", "悲泣", "忧伤", "悲痛", "沮丧", "气馁", "郁闷", "烦躁", "低沉",
        "消沉", "悲观", "消极", "酸涩", "落魄", "绝望", "紧张", "呆滞", "郁闷", "安心",
        "祥和", "来之不易", "担忧", "自由", "保持良好", "休闲", "恐慌", "放心", "放弃"]

# 逐条读取
line = txt.readline()
count = 0  # 记录循环次数
newLine = ""  # 临时储存字符串
flag = 0  # 记录状态

while line != "":
    while newLine != "\n":  # 读取一整条新闻
        newLine = txt.readline()
        line = line + newLine
    newLine = ""
    myList = jieba.cut(line)  # jieba库分词

    # 第一阶段
    if flag == 1:
        if "2019年12月08日" in line:  # 返回默认状态
            flag = 0
        for word in myList:
            if word in mood:
                if word in myDict1:
                    myDict1[word] += 1
                else:
                    myDict1[word] = 1

    # 第二阶段
    elif flag == 2:
        if "2020年01月23日" in line:  # 返回默认状态
            flag = 0
        for word in myList:
            if word in mood:
                if word in myDict2:
                    myDict2[word] += 1
                else:
                    myDict2[word] = 1

    # 第三阶段
    elif flag == 3:
        if "2020年02月10日" in line:  # 返回默认状态
            flag = 0
        for word in myList:
            if word in mood:
                if word in myDict3:
                    myDict3[word] += 1
                else:
                    myDict3[word] = 1

    # 第四阶段
    elif flag == 4:
        if "2020年03月10日" in line:  # 返回默认状态
            flag = 0
        for word in myList:
            if word in mood:
                if word in myDict4:
                    myDict4[word] += 1
                else:
                    myDict4[word] = 1

    # 不属于任何一个阶段（默认状态）
    else:
        if "2020年06月" in line:  # 跳转到第四阶段
            flag = 4
        if "2020年02月13日" in line:  # 跳转到第三阶段
            flag = 3
        if "2020年02月07日" in line:  # 跳转到第二阶段
            flag = 2
        if "2020年01月22日" in line:  # 跳转到第一阶段
            flag = 1
    count += 1
    line = txt.readline()
    print(count)

# 从大到小排序
myDict1 = sorted(myDict1.items(), key = lambda x:x[1], reverse = True)
print(myDict1)

myDict2 = sorted(myDict2.items(), key = lambda x:x[1], reverse = True)
print(myDict2)

myDict3 = sorted(myDict3.items(), key = lambda x:x[1], reverse = True)
print(myDict3)

myDict4 = sorted(myDict4.items(), key = lambda x:x[1], reverse = True)
print(myDict4)

# 处理结果写入txt文件
f = open("新闻1.txt", 'w+')
for item in myDict1:
    if float(item[1]) != 0.0:
        f.write(item[0] + ": \t" + str(item[1]) + "\n")
f.close()

f = open("新闻2.txt", 'w+')
for item in myDict2:
    if float(item[1]) != 0.0:
        f.write(item[0] + ": \t" + str(item[1]) + "\n")
f.close()

f = open("新闻3.txt", 'w+')
for item in myDict3:
    if float(item[1]) != 0.0:
        f.write(item[0] + ": \t" + str(item[1]) + "\n")
f.close()

f = open("新闻4.txt", 'w+')
for item in myDict4:
    if float(item[1]) != 0.0:
        f.write(item[0] + ": \t" + str(item[1]) + "\n")
f.close()









