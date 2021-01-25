from pyecharts.charts import Bar, Pie
from pyecharts import options as opts
import numpy as np


x1 = np.loadtxt('四阶段-江苏-合并后.txt', delimiter=':', usecols=(1), unpack=True)
a1 = x1.shape
b = a1[0]
f1 = open('四阶段-江苏-合并后.txt', encoding="GB2312")
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



(
    #颜色
    Pie(init_opts=opts.InitOpts(bg_color="#2c343c"))
    .add(
        #名称
        series_name="第四阶段",
        data_pair=[list(z) for z in zip(lista1, x1)],
        radius=["40%", "65%"],
        #圆心位置
        center=["50%", "50%"],
        #标签
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        #标题
        title_opts=opts.TitleOpts(
            #名字
            title="江苏第四阶段心态空心图",
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
    .render("江苏心态空心图.html")
)
