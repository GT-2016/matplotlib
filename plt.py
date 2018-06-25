# coding:utf-8
import matplotlib.pyplot as plt
from random import choice
from random import randint

class PlotDraw():
    """draw some plot by matplotlib module"""
    def __init__(self):
        self.title_fontsize = 24
        self.label_fontsize = 14
        self.title = "Squre Numbers"

    def setTitle(self, title, fontSize=24):
        plt.title(title, fontsize=fontSize)

    def setX(self, xs,fontSize=14):
        plt.xlabel(xs, fontsize=fontSize)

    def setY(self, ys, fontSize=14):
        plt.ylabel(ys, fontsize=fontSize)

    def setTick(self, _axis='both',whitch='major', labelSize=14):
        plt.tick_params(axis=_axis, labelsize=labelSize)

    def setAxis(self,arr):
        plt.axis(arr)

    def show_line(self, *arr, lineWidth=5):
        plt.plot(*arr,linewidth=lineWidth)

    def show_point(self, *arr):
        # plt.scatter(*arr)
        #删除数据点的轮廓,自定义颜色c='red',颜色映射colormap
        plt.scatter(*arr, edgecolor='none',s=15,c='red')

    def hideAxes(self):
        "hide x and y axis"
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

    def show_p(self,x_value, y_value,color):
        plt.scatter(x_value, y_value, c=color, cmap=plt.cm.Blues,edgecolor='none',s=15)

    def show_p_p(self, x_value, y_value,color):
        "start point and end point to outstanding"
        plt.scatter(0,0,c='green',s=100)
        plt.scatter(x_value[-1], y_value[-1],c='red',s=100)
        plt.scatter(x_value, y_value, c=color, cmap=plt.cm.Greens, edgecolor='none', s=1)

    def show(self):
        plt.show()

class RandomWalk():
    """随机漫步"""
    def __init__(self, num_points=5000):
        """init property"""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

class Die():
    """表示一个骰子的类"""
    def __init__(self, num_sides=6):
        """6个面"""
        self.num_sides = num_sides

    def roll(self):
        """随机返回某个面"""
        return randint(1, self.num_sides)


