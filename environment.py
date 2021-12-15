import numpy as np 
import matplotlib.pyplot as plt
import random
from random_location import a_random_position
from numpy.core.fromnumeric import shape
from robot import Robot
from human import Human
from robot_path_plan import robot_path_planning


# initial Environment 

dimension = 40
no_of_static_obstacles = 8

map = np.zeros((dimension,dimension))
obstacle = np.full((3,3),255)

#initial State 
print(map)
print(obstacle)
print("Length: ",len(map[0]))
print("FIrst row: ", map[0])

print("\n\n\n")

# ALGORITHM FOR CREATING THE OBSTACLES : 

number_of_obstacle = 0

while (number_of_obstacle < no_of_static_obstacles):
        i = random.randint(0,dimension-1)
        j = random.randint(0,dimension-1)
        print("DEbug", i,j)
        try:
            map[i,j]=  obstacle[1,1] 
        except IndexError:
            pass
        try:
            map[i,j+1]= obstacle[1,2]
        except IndexError:
            pass
        try:
            map[i,j-1]= obstacle[1,0]
        except IndexError:
            pass
        try:
            map[i-1,j]= obstacle[0,1]
        except IndexError:
            pass
        try:
            map[i+1,j]= obstacle[2,1]
        except IndexError:
            pass
        try:
            map[i-1,j-1]= obstacle[0,0]
        except IndexError:
            pass
        try:
            map[i+1,j-1]= obstacle[2,0]
        except IndexError:
            pass
        try:
            map[i-1,j+1]= obstacle[0,2] 
        except IndexError:
            pass
        try:
            map[i+1,j+1]= obstacle[2,2]
        except IndexError:
            pass
        number_of_obstacle += 1
#print("Dimension: ",shape(map))
print("After", map)  




R1 = Robot ("Robot_1")
H1 = Human ("Human_1")

R1.set_init_loc( a_random_position(dimension,dimension))
R1.set_dest_loc(a_random_position(dimension,dimension))
r1_src = R1.get_init_loc()
r1_dst = R1.get_dest_loc()
r1_path = robot_path_planning(r1_src, r1_dst)
R1.set_planned_path(r1_path)
check = R1.get_path_robot()


H1.set_init_loc(a_random_position(dimension,dimension))
H1.set_dst_loc(a_random_position(dimension,dimension))

#H1.print_details()
R1.print_details()

plt.imshow(map, interpolation='none')
#plt.matshow(a)
plt.show()