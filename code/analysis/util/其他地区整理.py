beijing = open("微博结果/一阶段/一阶段-北京result.txt", "r", encoding="gbk")
anhui = open("微博结果/一阶段/一阶段-安徽result.txt", "r", encoding='gbk')
guangxi = open("微博结果/一阶段/一阶段-广西result.txt", "r", encoding='gbk')
guangdong = open("微博结果/一阶段/一阶段-广东result.txt", "r", encoding='gbk')
gansu = open("微博结果/一阶段/一阶段-甘肃result.txt", "r", encoding='gbk')
fujian = open("微博结果/一阶段/一阶段-福建result.txt", "r", encoding='gbk')
chongqing = open("微博结果/一阶段/一阶段-重庆result.txt", "r", encoding='gbk')


myDict = dict()
mood = ["好", "怕", "无感", "关心", "提心吊胆", "担心", "不好", "痛苦", "激动", "可惜",
        "大不了", "喜欢", "乐观", "牛", "可怕", "窘迫", "恐惧", "痛", "燃", "鼓掌",
        "满足", "良好", "信心", "强", "平稳", "治愈", "放松", "松懈", "自觉", "温暖",
        "开心", "喜悦", "狂喜", "尽情", "快乐", "愉悦", "畅快", "欣喜", "幸福", "得意",
        "痛快", "满足", "欢乐", "快活", "陶醉", "甜美", "微笑", "兴奋", "自豪", "欣慰",
        "高兴", "满意", "心烦", "失落", "伤感", "忧伤", "委屈", "绝望", "哭泣", "伤心",
        "痛苦", "悲伤", "悲泣", "忧伤", "悲痛", "沮丧", "气馁", "郁闷", "烦躁", "低沉",
        "消沉", "悲观", "消极", "酸涩", "落魄", "绝望", "紧张", "呆滞", "郁闷", "安心",
        "祥和", "来之不易", "担忧", "自由", "保持良好", "休闲", "恐慌", "放心", "放弃"]

line = "\n"
while line != "":
    line = beijing.readline()
    data = line.split(":")
    if data[0] in mood:
        if data[0] in myDict:
            myDict[data[0]] += float(data[1])
        else:
            myDict[data[0]] = float(data[1])

line = "\n"
while line != "":
    line = anhui.readline()
    data = line.split(":")
    if data[0] in mood:
        if data[0] in myDict:
            myDict[data[0]] += float(data[1])
        else:
            myDict[data[0]] = float(data[1])

line = "\n"
while line != "":
    line = guangdong.readline()
    data = line.split(":")
    if data[0] in mood:
        if data[0] in myDict:
            myDict[data[0]] += float(data[1])
        else:
            myDict[data[0]] = float(data[1])

line = "\n"
while line != "":
    line = guangxi.readline()
    data = line.split(":")
    if data[0] in mood:
        if data[0] in myDict:
            myDict[data[0]] += float(data[1])
        else:
            myDict[data[0]] = float(data[1])

line = "\n"
while line != "":
    line = gansu.readline()
    data = line.split(":")
    if data[0] in mood:
        if data[0] in myDict:
            myDict[data[0]] += float(data[1])
        else:
            myDict[data[0]] = float(data[1])

line = "\n"
while line != "":
    line = fujian.readline()
    data = line.split(":")
    if data[0] in mood:
        if data[0] in myDict:
            myDict[data[0]] += float(data[1])
        else:
            myDict[data[0]] = float(data[1])

line = "\n"
while line != "":
    line = chongqing.readline()
    data = line.split(":")
    if data[0] in mood:
        if data[0] in myDict:
            myDict[data[0]] += float(data[1])
        else:
            myDict[data[0]] = float(data[1])

myDict = sorted(myDict.items(), key = lambda x:x[1], reverse = True)
print(myDict)

f = open("微博结果/一阶段/一阶段-其他result.txt", 'w+')
for item in myDict:
    if float(item[1]) != 0.0:
        f.write(item[0] + ": \t" + str(item[1]) + "\n")
f.close()

