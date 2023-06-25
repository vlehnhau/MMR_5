from random import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xy_pos = np.asarray([random(), random()])
speed = np.asarray([random(), random()])
D = 2
m = 5
num_itr = 1000
h = 0.01


def sim(pos, speed):
    old_pos = pos
    old_speed = speed

    pos_arr = [pos]
    speed_arr = [speed]

    for i in range(num_itr):
        F = -D * old_pos
        a = F / m

        next_pos = old_pos + old_speed * h
        pos_arr.append(next_pos)

        next_speed = old_speed + a * h
        speed_arr.append(next_speed)

        old_pos = next_pos
        old_speed = next_speed
    return pos_arr


fig, ax = plt.subplots()
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])

pos, = ax.plot([], [], "o", color="black")
text = ax.text(0.1, 0.1, '', transform=ax.transAxes)

pos_arr = sim(xy_pos, speed)

plot_x = []
plot_y = []
for i in range(len(pos_arr)):
    plot_x.append(pos_arr[i][0])
    plot_y.append(pos_arr[i][1])

def init():
    pos.set_data([], [])
    text.set_text('')

    ax.plot(0, 0, "x", color="red")
    ax.plot(plot_x, plot_y, color="black")

    return pos, text


def step(i):
    pos.set_data(pos_arr[i][0], pos_arr[i][1])
    text.set_text("Step: " + str(i))

    return pos, text


ani = animation.FuncAnimation(fig, step, np.arange(0, num_itr), interval=5, blit=False, init_func=init)

plt.show()
