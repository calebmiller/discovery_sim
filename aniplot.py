import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# Create subplots
figure, ax = plt.subplots(figsize=(10, 8))
bins = 100  # Number of bins for the histogram

x=np.linspace(100,1000,1800)
counts,bin_edges=np.histogram(x,bins)
bin_centres= (bin_edges[:-1]+bin_edges[1:])/2

def update(frame):
	global x
	# Append new random data point
	x = np.append(x, np.random.uniform(100, 1000, 100))  # Add more data points per frame for better visual effect
	x = np.append(x, np.random.normal(250, 20, 2))  # Add more data points per frame for better visual effect

	counts,bin_edges=np.histogram(x,bins)
	err=np.sqrt(counts)

	# Clear the axes and redraw the histogram
	ax.clear()
	ax.errorbar(bin_centres, counts, yerr=err, fmt='o')
	ax.set_xlabel("X-axis")
	ax.set_ylabel("Y-axis")
	ax.set_xlim(100,1000)

# Create animation
ani = FuncAnimation(figure, update, frames=100, repeat=False)

# Save animation
ani.save('histogram_animation.gif', writer='pillow', fps=10)

plt.show()

