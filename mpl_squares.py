# coding:utf-8
# import matplotlib.pyplot as plt
from plt import PlotDraw,RandomWalk
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
plot.hideAxes()
rw = RandomWalk(50000)
rw.fill_walk()
point_num = list(range(rw.num_points))
plot.show_p_p(rw.x_values,rw.y_values,point_num)
plot.show()
