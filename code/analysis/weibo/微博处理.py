import pandas as pd
import jieba
import math

# 读取csv文件
df = pd.read_csv('微博数据/三阶段/三阶段-四川.csv')
ser = df["微博正文"]
zhuan = df["转发数"]
ping = df["评论数"]
zan = df["点赞数"]
myDict = dict()

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

# 逐行读取
for i in range(0, 2500):
    myList = jieba.cut(ser[i])  # jieba库分词
    factor = 1 + 0.2 * zhuan[i] + 0.05 * ping[i] + 0.01 * zan[i]  # 加权计算影响因子
    for word in myList:
        if word in mood:  # 心态词筛选
            if word in myDict:
                myDict[word] = myDict[word] + "/" + str(factor)  # 每个数据用/隔开
            else:
                myDict[word] = str(factor)

# 用正态分布排除极端值
for word in myDict.keys():
    nums = myDict[word].split("/")  # 把数据变成字符串数组
    ex = 0.0  # EX：平均值
    n = 0  # n：数据个数
    for i in nums:
        ex += float(i)
        n += 1
    ex /= n
    dx = 0.0  # DX：方差
    for i in nums:
        dx += (ex - float(i)) ** 2
    dx /= n
    low = ex - 3 * math.sqrt(dx)  # μ - 3*σ
    high = ex + 3 * math.sqrt(dx)  # μ + 3*σ
    value = 0.0  # 总影响因子
    for i in nums:
        if low < float(i) < high:  # 剔除极端值
            value += float(i)
    myDict[word] = round(value, 2)  # 精确到小数点后2位

# 从大到小排序
myDict = sorted(myDict.items(), key = lambda x:x[1], reverse = True)
print(myDict)

# 处理结果写入txt文件
f = open("微博结果/三阶段/三阶段-四川result.txt", 'w+')
for item in myDict:
    if float(item[1]) != 0.0:
        f.write(item[0] + ": \t" + str(item[1]) + "\n")
f.close()









