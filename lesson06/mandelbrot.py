import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(N, threshold, nx, ny):
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)
    c = x[:,np.newaxis] + 1j * y[np.newaxis,:]

    z = c
    for j in range(N):
        z = z**2 + c

    mandelbrot_set =(abs(z) < threshold)
    return mandelbrot_set

mandelbrot_set = mandelbrot(50, 50., 601, 401)

plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
plt.gray()
plt.show()
