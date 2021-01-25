txt = open("微博结果/四阶段/四阶段-重庆result.txt", "r", encoding='gbk')
myDict = dict()

mood = ["无感", "不好", "痛苦", "激动", "可惜",
        "大不了", "喜欢", "乐观", "牛", "窘迫", "痛", "燃", "鼓掌",
        "信心", "强", "平稳", "治愈", "放松", "松懈", "自觉",
        "陶醉",
        "心烦", "绝望",
        "紧张", "呆滞", "安心",
        "来之不易", "自由", "保持良好", "休闲", ]
mood1 = ["幸福", "得意", "尽情", "满足", "自豪", "微笑", "满意", "祥和", "放心", "温暖",
         "好", "良好"]
mood2 = ["怕", "可怕", "恐惧", "恐慌", "提心吊胆"]
mood3 = ["关心", "担心", "担忧", ]
mood4 = ["开心", "喜悦", "狂喜", "快乐", "欢乐", "快活", "痛快", "愉悦", "畅快", "欣喜",
         "甜美", "欣慰", "兴奋", "高兴", ]
mood5 = ["哭泣", "伤心", "痛苦", "悲伤", "悲泣", "忧伤", "悲痛", "忧伤", "委屈", "伤感",
         "沮丧", "气馁", "郁闷", "烦躁", "低沉", "消沉", "悲观", "消极", "落魄", "酸涩",
         "失落", "放弃", ]

line = "\n"
while 1:
    line = txt.readline()
    if line == "":
        break
    data = line.split(":")
    if data[0] in mood1:
        data[0] = "满意"
    if data[0] in mood2:
        data[0] = "恐慌"
    if data[0] in mood3:
        data[0] = "担忧"
    if data[0] in mood4:
        data[0] = "喜悦"
    if data[0] in mood5:
        data[0] = "沮丧"
    if data[0] in myDict:
        myDict[data[0]] += float(data[1])
    else:
        myDict[data[0]] = float(data[1])

myDict = sorted(myDict.items(), key = lambda x:x[1], reverse = True)
print(myDict)

f = open("微博结果/四阶段/四阶段-重庆-合并后.txt", 'w+')
for item in myDict:
    if float(item[1]) != 0.0:
        f.write(item[0] + ": \t" + str(round(float(item[1]), 2)) + "\n")
f.close()
