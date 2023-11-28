import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the ocean current vector field
def ocean_current(x, y):
    # Simplified circular current pattern
    return -y, x

# Create a grid for the vector field visualization
x = np.linspace(-2, 2, 20)
y = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x, y)
U, V = ocean_current(X, Y)

# Initialize the figure
fig, ax = plt.subplots()
ax.quiver(X, Y, U, V)
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_title("Boat on Ocean Currents")

# Initial position of the boat
boat_x, boat_y = [0], [0.1]
boat, = ax.plot(boat_x, boat_y, 'bo', markersize=6)  # 'bo' means blue circle

# Function to update the boat's position
def animate(i):
    global boat_x, boat_y
    u, v = ocean_current(boat_x[-1], boat_y[-1])
    dx = u * 0.1
    dy = v * 0.1
    boat_x.append(boat_x[-1] + dx)
    boat_y.append(boat_y[-1] + dy)
    boat.set_data(boat_x[-1], boat_y[-1])

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100)

plt.show()
