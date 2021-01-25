from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
import numpy as np


x1 = np.loadtxt('一阶段-湖北-合并后.txt', delimiter=':', usecols=(1), unpack=True)
x2 = np.loadtxt('二阶段-湖北-合并后.txt', delimiter=':', usecols=(1), unpack=True)
x3 = np.loadtxt('三阶段-湖北-合并后.txt', delimiter=':', usecols=(1), unpack=True)
x4 = np.loadtxt('四阶段-湖北-合并后.txt', delimiter=':', usecols=(1), unpack=True)
a1 = x1.shape
a2 = x2.shape
a3 = x3.shape
a4 = x4.shape
b = a1[0]
f1 = open('一阶段-湖北-合并后.txt', encoding="GB2312")
line = f1.readline()
lista1 = [0 for x in range(0, b)]
i = 0
while line:
    line = line.replace(" ", "").replace("\n", "").split(":")
    if(line[0] != ''):
        lista1[i] = line[0]
    line = f1.readline()
    i = i + 1
f1.close()

f2 = open('二阶段-湖北-合并后.txt', encoding="GB2312")
line = f2.readline()
b = a2[0]
lista2 = [0 for x in range(0, b)]
i = 0
while line:
    line = line.replace(" ", "").replace("\n", "").split(":")
    if (line[0] != ''):
        lista2[i] = line[0]
    line = f2.readline()
    i = i + 1
f2.close()

f3 = open('三阶段-湖北-合并后.txt', encoding="GB2312")
line = f3.readline()
b = a3[0]
lista3 = [0 for x in range(0, b)]
i = 0
while line:
    line = line.replace(" ", "").replace("\n", "").split(":")
    if (line[0] != ''):
        lista3[i] = line[0]
    line = f3.readline()
    i = i + 1
f3.close()

f4 = open('四阶段-湖北-合并后.txt', encoding="GB2312")
line = f4.readline()
b = a4[0]
lista4 = [0 for x in range(0, b)]
i = 0
while line:
    line = line.replace(" ", "").replace("\n", "").split(":")
    if (line[0] != ''):
        lista4[i] = line[0]
    line = f4.readline()
    i = i + 1
f4.close()

(
    #颜色
    Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
    .add(
        #名称
        series_name="第一阶段",
        data_pair=[list(z) for z in zip(lista1, x1)],
        radius="30%",
        #圆心位置
        center=["30%", "35%"],
        #标签
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .add(
        series_name="第二阶段",
        data_pair=[list(z) for z in zip(lista2, x2)],
        radius="30%",
        center=["70%", "35%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .add(
        series_name="第三阶段",
        data_pair=[list(z) for z in zip(lista3, x3)],
        radius="30%",
        center=["30%", "78%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .add(
        series_name="第四阶段",
        data_pair=[list(z) for z in zip(lista3, x4)],
        radius="30%",
        center=["70%", "78%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        #标题
        title_opts=opts.TitleOpts(
            #名字
            title="湖北省四个阶段心态扇形图",
            pos_left="center",
            pos_top="20",
            #标题颜色
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        #没用
        legend_opts=opts.LegendOpts(is_show=False),
    )
    #系列
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        #标签颜色
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("湖北省心态扇形图.html")
)