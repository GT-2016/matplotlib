# coding:utf-8
# import matplotlib.pyplot as plt
from plt import PlotDraw,RandomWalk,Die

import pygal        # 可缩放矢量图

x_value = list(range(1,1001))
y_value = [i**3 for i in x_value]
m = 2,4

plot = PlotDraw()

# =======================配置======================= #
plot.setTitle("Squre Number")
plot.setX("value")
plot.setY("Squre of Value")
plot.setTick()
# plot.setAxis([0,1000,0,1100000])
# ==================================================== #
# plot.show_line(x_value,y_value)
# plot.hideAxes()
# rw = RandomWalk(50000)
# rw.fill_walk()
# point_num = list(range(rw.num_points))
# plot.show_p_p(rw.x_values,rw.y_values,point_num)
# plot.show()
# ======================= 骰子======================= #
die1 = Die()
die2 = Die()
results = [die1.roll() + die2.roll() for roo_num in range(1000)]
max_num = die1.num_sides + die2.num_sides
freq = [results.count(value) for value in range(1, max_num+1)]
print(freq)

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(i) for i in range(2, 13)]
hist.x_title = "result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',freq)
hist.render_to_file('die_visual.svg')
