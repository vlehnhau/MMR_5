from math import *
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# f((x+h,y)−f(x−h,y))/2h

def xAbl(imgarr):
    return_val = []
    for y in range(len(imgarr)):
        row = [imgarr[y][1] / 2]
        for x in range(1, len(imgarr[y]) - 1):
            row.append((imgarr[y][x + 1] - imgarr[y][x - 1]) / 2)

        row.append(-(imgarr[y][len(imgarr[y]) - 2] / 2))
        return_val.append(row)

    return np.asarray(return_val)


def yAbl(imgarr):
    return_val = [[]]

    for y in range(1, len(imgarr) - 1):
        row = []
        for x in range(0, len(imgarr[0])):
            row.append((imgarr[y - 1][x] - imgarr[y + 1][x]) / 2)
        return_val.append(row)

    row = []

    for x in range(0, len(imgarr[0])):
        return_val[0].insert(0, imgarr[1][x] / 2)
        row.append(imgarr[len(imgarr) - 2][x] / 2)
    return_val.append(row)

    return np.asarray(return_val)


def xyAbl(imgarr):
    return_val = []

    xabl = xAbl(imgarr)
    yabl = yAbl(imgarr)

    for y in range(len(imgarr)):
        return_val.append([])
        for x in range(1, len(imgarr[y]) - 1):
            return_val[y].append(sqrt((xabl[y][x] ** 2) + (yabl[y][x] ** 2)))

    return return_val


image = Image.open("Image.jpeg").convert("L")
img = np.asarray(image, dtype=np.int16)

fig = plt.figure()
ax_1 = fig.add_subplot(2, 2, 1)
ax_2 = fig.add_subplot(2, 2, 2)
ax_3 = fig.add_subplot(2, 2, 3)
ax_4 = fig.add_subplot(2, 2, 4)

ax_1.imshow(img, cmap='gray')

xabl = xAbl(img)
yabl = yAbl(img)
both = xyAbl(img)

ax_2.imshow(xabl, cmap='gray')
ax_3.imshow(yabl, cmap='gray')
ax_4.imshow(both, cmap='gray')

plt.show()
