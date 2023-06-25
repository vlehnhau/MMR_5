from random import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.asarray([random(), random()])
D = 4
m = 3
h = 1
num_steps = 1000
speed = np.asarray([random(), random()])


def sim(x, speed):
    new_x = x
    a = 0
    new_speed = speed
    F = np.asarray([- D * x[0], - D * x[1]])

    pos_arr = []
    speed_arr = []

    for i in range(0, num_steps):
        pos_arr.append(new_x)
        speed_arr.append(new_speed)

        new_x = new_x + new_speed * h
        a = F / m
        new_speed = new_speed + a * h

        F = np.asarray([- D * new_x[0], - D * new_x[1]])

    return pos_arr, speed_arr


fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-20, 20])
ax.set_ylim([-20, 20])

obj, = ax.plot([], [], "-", color="blue")
sp, = ax.plot([], [], color="red")
text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

(pos_arr, sp_arr) = sim(x, speed)

xplot = []
yplot = []
for i in range(len(pos_arr)):
    xplot.append(pos_arr[i][0])
    yplot.append(pos_arr[i][1])


def init():
    obj.set_data([], [])
    text.set_text('')
    ax.plot(0, 0, "x", color="red")
    ax.plot(xplot, yplot, color="black")
    return obj, text


def step(i):
    obj.set_data([pos_arr[i][0]], [pos_arr[i][1]])
    text.set_text("Schritt: " + str(i))
    return obj, text


ani = animation.FuncAnimation(fig, step, np.arange(0, num_steps),
                              interval=5, blit=False, init_func=init)
plt.show()

# # folgende objekte sollen wie gezeichnet werden
# curve, = ax.plot([], [], "-", color="blue")
# origin = ax.plot(0, 0, "x", color="red")
# pos, = ax.plot([], [], "o", color="black")
# text = ax.text(0.1, 0.2, '', transform=ax.transAxes)
#
# # wir merken uns alle positionen
# curve_pos = [[], []]
#
# # berechnnung der neuen position
# t = np.linspace(0, 100, 5000)
# a = np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5
# curve_pos = [np.sin(t) * a, np.cos(t) * a]  # x- und zugehörige y-Werte
#
#
# # initialisierung der animation (startbild)
# def init():
#     curve.set_data(curve_pos[0], curve_pos[1])
#     pos.set_data([], [])
#     text.set_text('')
#     return pos, text
#
#
# # animationsschritt
# def step(i):
#     pos.set_data([curve_pos[0][i]], [curve_pos[1][i]])
#     text.set_text("Schritt " + str(i))
#     return pos, text
#
#
# # interval gibt an, wie lange gewartet wird in ms
# # blit=True (nicht alles wird sets neu gezeichnet)
# # drittes argument gib an wie sich der index i in step(i) verhält
# ani = animation.FuncAnimation(fig, step, np.arange(1, len(t)), interval=25, blit=True, init_func=init)
#
# # als film speichern (mit 15 fps)
# # ani.save('butterfly.mp4', fps=15)
#
# # anzeigen
# plt.show()
