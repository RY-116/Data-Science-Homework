import pyecharts.options as opts  # 导入pyecharts库
from pyecharts.charts import Line

num = [0.7073, 0.6472, 0.8294, 0.8315]  # 导入数据
num2 = [0.6131, 0.7733, 0.8283, 0.8237]
num3 = [0.6256, 0.7551, 0.8286, 0.8269]
lab = ["第一阶段", "第二阶段", "第三阶段", "第四阶段"]

(
    Line(init_opts=opts.InitOpts(width='720px', height='320px'))  # 指定画布大小,括号内为空则默认大小
        .add_xaxis(xaxis_data=lab)
        .add_yaxis("湖北", num)
        .add_yaxis("其他省份", num2, symbol="triangle")
        .add_yaxis("总体心态", num3, symbol="")
        .set_global_opts(title_opts=opts.TitleOpts(title="积极心态变化图"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
).render('积极心态折线图.html')
