# -*- coding: utf-8 -*-
"""Matplotlib_tutorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WqUzb4oihDrOI_RQMXbH-ecn6pqK_okE

## Matplotlib Line Plot

The pyplot.plot() or plt.plot() is a method of matplotlib pyplot module use to plot the line.

> Syntax: plt.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
"""

import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

plt.plot(days, temperature)
plt.show()

"""To show annotations on the axes

>Syntax: plt.xlabel(xlabel, fontdict=None, labelpad=None, **kwargs)

>Syntax: plt.ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)

>Syntax: plt.title(label, fontdict=None, loc=‘center’, pad=None, **kwargs)
"""

#plotting with x,y -axes and title
plt.plot(days, temperature)
plt.title("Delhi Temperature")
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()

"""to manually set the axis value for starting of the plot use plt.axis() method.

>Syntax: plt.axis(xmin, xmax, ymin, ymax)

"""

#set axis(setting points betweeb which the graph will be shown)
plt.plot(days, temperature)
plt.axis([0,30,0,50])
plt.title("Delhi Temperature")
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()

plt.plot(days, temperature, color='g', marker='o', linestyle='--', markersize=10)
plt.title("Delhi Temperature")
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()

plt.plot(days, temperature, color='r', marker='P', linestyle='-.', markersize=10)
plt.title("Delhi Temperature")
plt.xlabel("days")
plt.ylabel("temperature")
plt.show()

"""### Color Parameter Values

1. b	blue
2. g	green
3. r	red
4. c	cyan
5. m	magenta
6. y	yellow
7. k	black
8. w	white

### Marker Parameter Values

1. .	point marker
2. ,	pixel marker
3. o	circle marker
4. v	triangle_down marker
5. ^	triangle_up marker
6. <	triangle_left marker
7. '>'	triangle_right marker
8. 1	tri_down marker
9. 2	tri_up marker
10. 3	tri_left marker
11. 4	tri_right marker
12. s	square marker
13. p	pentagon marker
14. *	star marker
15. h	hexagon1 marker
16. H	hexagon2 marker
17. +	plus marker
18. x	x marker
19. D	diamond marker
20. d	thin_diamond marker
21. |	vline marker
22. _	hline marker

### Line Style parameters values

1. _	solid line style
2. —	dashed line style
3. _.	dash-dot line style
4. :	dotted line style

If you want to change the bar chart’s background color and add grid then use style.use() method. For this first, need to import the style module from matplotlib. 

>Syntax: style.use(style)

To add a legend in the graph to describe more information about it, use plt.legend().

>Syntax: plt.legend(*args, **kwargs)
"""

#adding legend 
from matplotlib import style
style.use("ggplot")
plt.plot(days, temperature, "mo--", linewidth=3, markersize=10, label="Temp line")
plt.title("Delhi Temperature")
plt.xlabel("days")
plt.ylabel("temperature")
plt.legend(loc=4)
plt.show()

"""### Multiple line plots"""

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
delhi_tem = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]
mumbai_tem = [39,39.4,40,40.7,41,42.5,43.5,44,44.9,44,45,45.1,46,47,46]
 
plt.plot(days, delhi_tem, "mo--", linewidth = 3,
        markersize = 10, label = "Delhi temp")
 
plt.plot(days, mumbai_tem, "yo:", linewidth = 3,
        markersize = 10, label = "Mumbai temp")
 
plt.title("Delhi  & Mumbai Temperature", fontsize=15)
plt.xlabel("days",fontsize=13)
plt.ylabel("temperature",fontsize=13)
plt.legend(loc = 4)
plt.show()

"""If you want to change or add grid then use plt.grid() method.

>Syntax: plt.grid(b=None, which=‘major’, axis=‘both’, **kwargs)
"""

#using grid
plt.plot(days, delhi_tem, "mo--", linewidth = 3,
        markersize = 10, label = "Delhi temp")
 
plt.plot(days, mumbai_tem, "yo:", linewidth = 3,
        markersize = 10, label = "Mumbai temp")
 
plt.title("Delhi  & Mumbai Temperature", fontsize=15)
plt.xlabel("days",fontsize=13)
plt.ylabel("temperature",fontsize=13)
plt.legend(loc = 4)
plt.grid(color='c', linestyle='-', linewidth=2) # grid with parameter
plt.show()

"""# Histograms

Matplotlib histogram is a representation of numeric data in the form of a rectangle bar. Each bar shows some data,  which belong to different categories. To plot histogram using python matplotlib library need plt.hist() method.

>Syntax: plt.hist(
x,
bins=None,
range=None,
density=None,
weights=None,
cumulative=False,
bottom=None,
histtype=’bar’,
align=’mid’,
orientation=’vertical’,
rwidth=None,
log=False,
color=None,
label=None,
stacked=False,
normed=None,
*,
data=None,
**kwargs,
)
"""

import matplotlib.pyplot as plt
import numpy as np
import random

ml_student_age = np.random.randint(18, 45, (100))
py_student_age = np.random.randint(18, 40, (100))
print(ml_student_age)
print(py_student_age)

plt.hist(ml_student_age)
 
plt.title("ML Students age histograms")
plt.xlabel("Students age cotegory")
plt.ylabel("No. Students age")
plt.show()

bins = [15,20,25,30,35,40,45] # category of ML students age on x axis
plt.figure(figsize = (16,9)) # size of histogram in 16:9 format
 
 
plt.hist(ml_student_age, bins, rwidth=0.8, histtype = "bar",
         orientation='vertical', color = "m", label = "ML Student")
 
plt.title("ML Students age histograms")
plt.xlabel("Students age cotegory")
plt.ylabel("No. Students age")
plt.legend()
plt.show()

"""#### Plotting two histograms using matplotlib with parameters"""

from matplotlib import style 
style.use("ggplot")
plt.figure(figsize=(16,9))

plt.hist([ml_student_age, py_student_age], bins, rwidth=0.8, histtype="bar",
         orientation='vertical', color=["m","y"],label=["ML Student","Py Student"])

plt.title("ML & Py Students age histograms")
plt.xlabel("Students age cotegory")
plt.ylabel("No. Students age")
plt.legend()
plt.show()

"""#Matplotlib Bar Chart
To visualize value associated with categorical data in the bar format use matplotlib bar chart plt.bar() or plt.barh() methods.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

classes = ["Python", "R", "AI", "ML", "DS"]
class1_students = [30, 10, 20, 25, 10] # out of 100 student in each class
class2_students = [40, 5, 20, 20, 10]
class3_students = [35, 5, 30, 15, 15]

"""To plot bar chart using the matplotlib python library, use plt.bar() or plt.barh() methods.

>Syntax: plt.bar(x,height,width=0.8,bottom=None,*,align=’center’,data=None,**kwargs)

Parameters
———-
<br>x : sequence of scalars
<br>height : scalar or sequence of scalars
<br>width : scalar or array-like, optional …….(default: 0.8).
<br>bottom : scalar or array-like, optional
<br>align : {‘center’, ‘edge’}, optional, ……….default: ‘center’
<br>
<br>

Other Parameters
—————-
<br>color : scalar or array-like, optional
<br> edgecolor : scalar or array-like, optional
<br> linewidth : scalar or array-like, optional
<br>tick_label : string or array-like, optional ……. name of Bar
<br> xerr, yerr : scalar or array-like of shape(N,) or shape(2,N), optional
<br>ecolor : scalar or array-like, optional, default: ‘black’
<br>capsize : scalar, optional
<br>error_kw : dict, optional
<br>log : bool, optional, default: False
<br>orientation : {‘vertical’, ‘horizontal’}, optional


<br>


See also
——–
<br> barh: Plot a horizontal bar plot.

<br>

Other optional kwargs:
<br>agg_filter: a filter function, which takes a (m, n, 3) float array and a dpi value, and returns a (m, n, 3) array
<br>alpha: float or None
<br>animated: bool
<br>antialiased: unknown
<br>capstyle: {‘butt’, ’round’, ‘projecting’}
<br>clip_box: `.Bbox`
<br>clip_on: bool
<br>clip_path: [(`~matplotlib.path.Path`, `.Transform`) | `.Patch` | None]
<br>color: color
<br>contains: callable
<br>edgecolor: color or None or ‘auto’
<br>facecolor: color or None
<br>figure: `.Figure`
<br>fill: bool
<br>gid: str
<br>hatch: {‘/’, ‘\\’, ‘|’, ‘-‘, ‘+’, ‘x’, ‘o’, ‘O’, ‘.’, ‘*’}
<br>in_layout: bool
<br>joinstyle: {‘miter’, ’round’, ‘bevel’}
<br>label: object
<br>linestyle: {‘-‘, ‘–‘, ‘-.’, ‘:’, ”, (offset, on-off-seq), …}
<br>linewidth: float or None for default
<br>path_effects: `.AbstractPathEffect`
<br>picker: None or bool or float or callable
<br>rasterized: bool or None
<br>sketch_params: (scale: float, length: float, randomness: float)
<br>snap: bool or None
<br>transform: `.Transform`
<br>url: str
<br>visible: bool
<br>zorder: float
"""

plt.bar(classes, class1_students)

plt.barh(classes, class1_students)

"""#### Use multiple parameters of plt.bar() method"""

plt.bar(classes, class1_students, width = 0.2, align = "edge", color = "y",
       edgecolor = "m", linewidth = 5, alpha = 0.9, linestyle = "--",
       label =" Class 1 Students", visible=True)
#visible = false ## bar Chart will hide

#Increase figure size and use style.
style.use("ggplot") 
plt.figure(figsize=(16,9)) # figure size with ratio 16:9
plt.bar(classes, class1_students, width = 0.6, align = "edge", color = "k",
       edgecolor = "m", linewidth = 5, alpha = 0.9, linestyle = "--",
       label =" Class 1 Students")

style.use("ggplot") 
plt.figure(figsize=(16,9)) # figure size with ratio 16:9
plt.barh(classes, class1_students, align = "edge", color = "k",
       edgecolor = "m", linewidth = 5, alpha = 0.9, linestyle = "--",
       label =" Class 1 Students")

plt.figure(figsize=(16,9))
plt.bar(classes, class1_students, width = 0.6, align = "edge", color = "k",
       edgecolor = "m", linewidth = 5, alpha = 0.9, linestyle = "--",
       label =" Class 1 Students") 
 
plt.title("Bar Chart of IAIP Class", fontsize = 18)
plt.xlabel("Classes",fontsize = 15)
plt.ylabel("No. of Students", fontsize = 15)
plt.show()

#Trying to plot two bar charts with a different dataset.
plt.figure(figsize=(16,9))
 
plt.bar(classes, class1_students, width = 0.2, color = "b",
        label =" Class 1 Students")
 
plt.bar(classes, class2_students, width = 0.2, color = "g",
        label =" Class 2 Students") 
 
plt.title("Bar Chart of IAIP Class", fontsize = 18)
plt.xlabel("Classes",fontsize = 15)
plt.ylabel("No. of Students", fontsize = 15)
plt.show()

"""The above code is generating two bar charts in one figure but they are overlapping. So we use the below code to plot multiple bar charts. In below chart plot three bar charts using three different datasets."""

plt.figure(figsize=(16,9))
 
classes_index = np.arange(len(classes))
 
width = 0.2
 
plt.bar(classes_index, class1_students, width , color = "r",
        label =" Class 1 Students")
 
plt.bar(classes_index + width, class2_students, width , color = "b",
        label =" Class 2 Students") 
 
plt.bar(classes_index + width + width, class3_students, width , color = "g",
        label =" Class 2 Students") 
 
plt.xticks(classes_index + width, classes, rotation = 20)
plt.title("Bar Chart of IAIP Class", fontsize = 18)
plt.xlabel("Classes",fontsize = 15)
plt.ylabel("No. of Students", fontsize = 15)
plt.show()

plt.figure(figsize=(16,9))
 
classes_index = np.arange(len(classes))
 
width = 0.2
 
plt.barh(classes_index, class1_students, width , color = "r",
        label =" Class 1 Students") 
 
plt.barh(classes_index + width, class2_students, width , color = "g",
        label =" Class 2 Students") 
 
plt.barh(classes_index + width + width, class3_students, width , color = "b",
        label =" Class 3 Students") 
 
plt.yticks(classes_index + width, classes, rotation = 20)
plt.title("Bar Chart of IAIP Class", fontsize = 18)
plt.ylabel("Classes",fontsize = 15)
plt.xlabel("No. of Students", fontsize = 15)
plt.legend()
plt.show()

"""# Matplotlib Pie Chart
To draw pie char use plt.pie() function. The matplotlib plt.pie() function help to plot pie chart of given numeric data with labels.
"""

import matplotlib.pyplot as plt

plt.pie([1]) # Plot pie chart of value [1]
plt.show() # To show Pie cha

classes = ["Python", 'R', 'Machine Learning', 'Artificial Intelligence', 
           'Data Sciece']
class1_students = [45, 15, 35, 25, 30]

#Plotting pie chart using real dataset
plt.pie(class1_students, labels = classes)
plt.show()

