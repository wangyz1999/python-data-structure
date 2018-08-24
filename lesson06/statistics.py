import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

samples = np.random.normal(size=10000)

bins = np.linspace(-5, 5, 30)
histogram, bins = np.histogram(samples, bins=bins, normed=True)

bin_centers = 0.5*(bins[1:] + bins[:-1])

pdf = stats.norm.pdf(bin_centers)  # original probability density function

plt.plot(bin_centers, histogram, label="Histogram of samples")
plt.plot(bin_centers, pdf, label="PDF")
plt.legend()
plt.show()
