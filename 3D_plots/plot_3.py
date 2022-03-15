# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import environment

my_x =np.zeros((40))
my_y = np.zeros((40))
my_z = np.zeros((20))
for i in range(len(my_x)):
    my_x[i]=i+3
print(my_x)

for i in range (len(my_y)):
    my_y[i] = i + 6

print(my_y)

for i in range (len(my_y)):
    my_z[i] = i


# Creating datas
z = my_z
x = my_x
y = my_y

# Creating figure
fig = plt.figure(figsize = (16, 9))
ax = plt.axes(projection ="3d")

# Add x, y gridlines
ax.grid(b = True, color ='grey',
		linestyle ='-.', linewidth = 0.3,
		alpha = 0.2)


# Creating color map
my_cmap = plt.get_cmap('hsv')

# Creating plot
sctt = ax.scatter3D(x, y, z,
					alpha = 0.8,
					c = (x + y + z),
					cmap = my_cmap,
					marker ='^')

plt.title("Probability of Collison")
ax.set_xlabel('X-axis', fontweight ='bold')
ax.set_ylabel('Y-axis', fontweight ='bold')
ax.set_zlabel('Z-axis', fontweight ='bold')
fig.colorbar(sctt, ax = ax, shrink = 0.5, aspect = 5)

# show plot
plt.show()
