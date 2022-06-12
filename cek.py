from cmath import pi
from math import cos, sin
from datetime import datetime
import matplotlib.pyplot as plt

start_time = datetime.now()
x = [1, 1, 1, 1, 1, 1]
N = len(x)
k = 0
n = 0
i = 0
xr = []
xj = []

for i in range(N):
    xr.append(0)
    xj.append(0)

for k in range(N):
    xr[k] = 0
    xj[k] = 0
    for n in range(N):
        xr[k] += x[n]*cos(2*pi*k*n/N)
        xj[k] += x[n]*sin(2*pi*k*n/N)

    format_xr = "{:.2f}".format(xr[k])
    format_xj = "{:.2f}".format(xj[k])
    print(format_xr, '+', format_xj, 'j')

end_time = datetime.now()
