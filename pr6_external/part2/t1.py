import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

im_width, im_height = 1000, 1000
c = complex(0.11301, -0.74543)
zabs_max = 2
nit_max = 1000
xmin, xmax = -1.5, 1.5
xwidth = xmax - xmin
ymin, ymax = -1.5, 1.5
yheight = ymax - ymin

julia = np.zeros((im_width, im_height))
for ix in range(im_width):
    for iy in range(im_height):
        nit = 0

        z = complex(ix / im_width * xwidth + xmin,
                    iy / im_height * yheight + ymin)

        while abs(z) <= zabs_max and nit < nit_max:
            z = z**2 + c
            nit += 1
        julia[ix, iy] = 1 - nit / nit_max

fig, ax = plt.subplots()
ax.imshow(julia, interpolation='nearest', cmap=cm.hot)

xtick_labels = np.linspace(xmin, xmax, int(xwidth / 0.5))
ax.set_xticks([(x-xmin) / xwidth * im_width for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])

ytick_labels = np.linspace(ymin, ymax, int(yheight / 0.5))
ax.set_yticks([(y-ymin) / yheight * im_height for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])

plt.show()
