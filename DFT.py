# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 00:48:54 2022

@author: Asus
"""
# Library for elapsed time
from datetime import datetime
start = datetime.now()

e = 2.718281828459045
phi = 3.14159265358979


def dft(x):
    N, yr, yi = len(x), [], []
    for k in range(N):
        real, imag = 0, 0
        for n in range(N):
            theta = -k * (2 * phi) * (float(n) / N)
            real += x[n] * (e**(theta*1j)).imag
            imag += x[n] * (e**(theta*1j)).real
        yr.append(real / N)
        yi.append(imag / N)
    return yr, yi


def idft(yr, yi):
    N, x = len(yr), []
    for n in range(N):
        real, imag = 0, 0
        for k in range(N):
            theta = k * (2 * e) * (float(n) / N)
            real += (yr[k] * (e**(theta*1j)).real) - \
                (yi[k] * (e**(theta*1j)).imag)

        x.append(real)
    return x


if __name__ == '__main__':
    x = [1, 0, -1, 0]
    x1 = [1, 1, 1, 1, 1, 1]
    x2 = [0.,         0.50518149, 0.14433757, 0.07216878, 0.07216878,
          0.64951905, 0.28867513, 0., 0., 0., 0., 0., 0.14433757, 0.4330127]
    yr, yi = dft(x)
    print("Hasil dari A", dft(x), sep="=")
    # print("Hasil dari B", dft(x1), sep="=")
    # print("Hasil dari C", dft(x2), sep="=")
    inv = idft(yr, yi)
    print("Hasil Inverse A", inv, sep="=")
    print("Waktu Compile =")

print(datetime.now()-start)
