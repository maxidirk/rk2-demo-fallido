#! /usr/bin/env python

'''
Este script resuelve el pendulo simple usando RK2.
'''

import numpy as np
import matplotlib.pyplot as plt


A = np.pi / 30
w = np.sqrt(10)

plt.figure(1)
plt.clf()

t = np.linspace(0, 5 * 2 * np.pi / w, 400)

plt.plot(t, A * np.sin(w * t))


def f(phi, w):
    return w, -10 * np.sin(phi)

def get_k1(phi_n, w_n, h, f):
    f_eval = f(phi_n, w_n)
    return h * f_eval[0], h * f_eval[1]

def get_k2(phi_n, w_n, h, f):
    k1 = get_k1(phi_n, w_n, h, f)
    f_eval = f(phi_n + k1[0]/2, w_n + k1[1]/2)
    return h * f_eval[0], h * f_eval[1]

def rk2_step(phi_n, w_n, h, f):
    k2 = get_k2(phi_n, w_n, h, f)
    phi_n1 = phi_n + k2[0] * h
    w_n1 = w_n + k2[1] * h
    return phi_n1, w_n1












plt.xlabel('tiempo')
plt.ylabel('$\phi(t)$', fontsize=18)
plt.show()
plt.draw()
