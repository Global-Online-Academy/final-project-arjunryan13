#
# Bokeh Plot
#
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.models import Label
import numpy as np 
import math
import random

s3 = []
d = []

# Subject S3 Heart Rates
f = open("S3-hr.txt", "r")
for line in f:
    line = line.strip()
    s3.append(line)

for i in range(len(s3)):
    d.append(str(i))

labels = d
data = {'Heart Rate': s3, 'Time': labels}
source = ColumnDataSource(data=data)
p = figure(title="Chart of heart rate for Subject S3", x_axis_label='x', y_axis_label='y')
p.line(d, s3, line_width=2)
p.yaxis.axis_label = 'Heart Rate'

show(p)
