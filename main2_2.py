import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sin, cos, pi

angles = np.asarray([pi/2, -pi/2, pi/4, pi/5, 1])
lengths = np.asarray([1, 0.5, 0.9, 0.8, 0.75])
num_itr = 1000
h = 0.01
g = 9.81
colors = ["green", "red", "blue", "black", "orange"]

def sim(angles, lengths, itr):
    angle_arr = [angles]
    speed_arr = np.zeros(len(angles))       # Am Anfang haben alle Pendel keine Geschwindkeit
    vectorsin = np.vectorize(sin)           # Nötig um sin auf Arrays anzuwenden

    for i in range(itr):
        angles = angles + speed_arr * h
        speed_arr = speed_arr - ((g/lengths) * vectorsin(angles))
        angle_arr.append(angles)
    return angle_arr

def posXY(angles, lengths):
    x = []
    y = []
    for i in range(len(angles)):
        x.append(cos(angles[i]) * lengths[i])
        y.append(sin(angles[i]) * lengths[i])
    return x, y

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])

pos = []
lines = []
text = ax.text(0.1, 0.1, '', transform=ax.transAxes)

for i in range(len(angles)):
    p, = ax.plot([], [], "o", color=colors[i])
    l, = ax.plot([], [], color=colors[i])
    pos.append(p)
    lines.append(l)

angle_arr = sim(angles, lengths, num_itr)

def init():
    for i in range(len(pos)):
        pos[i].set_data([], [])
    ax.plot(0, 0, "o", color="black")
    text.set_text('')
    return pos + lines + [text]

def step(i):
    text.set_text("Schritt: " + str(i))
    y, x = posXY(angle_arr[i], lengths)
    for i in range(len(x)):
        pos[i].set_data(x[i], -y[i])
        lines[i].set_data([0, x[i]], [0, -y[i]])
    return pos + lines + [text]

ani = animation.FuncAnimation(fig, step, np.arange(0, num_itr),
                              interval=30, blit=False, init_func=init)
plt.show()

