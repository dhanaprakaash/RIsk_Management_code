import numpy as np 
import matplotlib.pyplot as plt
import random
from human_path_prediction import human_path_prediction
from new_path import new_path
from random_location import a_random_position
from numpy.core.fromnumeric import shape
from robot import Robot
from human import Human
from robot_path_plan import robot_path_planning
from distance_funs import manhatten_distance
from new_path import new_path


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


# Human Path Prediction 
h1_src_loc = H1.get_init_loc()
h1_dst_loc = H1.get_dst_loc()

h1_src_loc  = (round(h1_src_loc[0]), round(h1_src_loc[1]))

time_taken =  manhatten_distance(h1_src_loc,h1_dst_loc)
print("HI source",h1_src_loc)
H1.print_details()
R1.print_details()

transistion_vector = human_path_prediction(h1_src_loc, time_taken)
print ("*****new path****** ",transistion_vector)


human_path = new_path(h1_src_loc, transistion_vector)
H1.set_path(human_path)
print("Human Path",human_path)

plt.imshow(map, interpolation='none')
#plt.matshow(a)
plt.show()


print("robot_Path and Humsn Path\n", r1_path, human_path)

# PLOTTING HUMAN AND ROBOT PATH:

time_axis_robot = np.zeros(len(r1_path))
time_axis_human = np.zeros(len(human_path))

for i in range(len(time_axis_robot)):
    time_axis_robot[i] = i

for i in range(len(time_axis_human)):
    time_axis_human[i] = i

print("time_axis_robot",time_axis_robot)
print("time_axis_human", time_axis_human)

robot_x_axis = [0] * len(r1_path)
robot_y_axis = [0] * len(r1_path)
human_x_axis = [0] * len(human_path)
human_y_axis = [0] * len(human_path)


for i in range(len(r1_path)):
    robot_x_axis[i] = r1_path[i][0]
    robot_y_axis[i] = r1_path[i][1]

print ("ra_path", r1_path)

for i in range(len(human_path)):
    human_x_axis[i] = human_path[i][0]
    human_y_axis[i] = human_path[i][1]


print ("robot_y",robot_y_axis, "robot_x",robot_x_axis, "human_x",human_x_axis, "human_y",human_y_axis)
print("*****\n\n\n\n\n")  
'''

plt.plot(r1_path,time_axis_robot)
plt.plot(human_path,time_axis_human)

plt.show()


plt.scatter(robot_x_axis,robot_y_axis)
plt.scatter(human_x_axis, human_y_axis)

plt.show()
'''
print("Debug: ","Human Path", "Robot Path")
print("HUman:", human_path)
print("Robot:", r1_path)

x_axis_human = [0] * len(human_path)
y_axis_human = [0] * len(human_path)

x_axis_robot = [0] * len(r1_path)
y_axis_robot = [0] * len(r1_path)

for i in range(len(human_path)):
    x_axis_human[i] = human_path[i][0]
    y_axis_human[i] = human_path[i][1]

print("x_axis: ", x_axis_human)
print("y_axis: ",y_axis_human )

for i in range(len(r1_path)):
    x_axis_robot[i] = r1_path[i][0]
    y_axis_robot[i] = r1_path[i][1]

print("x_axis: ", x_axis_robot)
print("y_axis: ",y_axis_robot )


plot1 = plt.figure(1)
ax = plt.subplot()
for i in range(len(human_path)):
    plt.scatter(x_axis_human[i], y_axis_human[i])
for i in range(len(r1_path)):  
    plt.scatter(x_axis_robot[i], y_axis_robot[i])
plt.plot(x_axis_human, y_axis_human, label="Human motion")
plt.plot(x_axis_robot, y_axis_robot, label="Robot motion")
plt.grid()
plt.legend()
plt.show()



print("Debug: Robot and Human Path")
print("Robot:", r1_path)
print("Human: ", human_path)


H1.print_details()
R1.print_details()

### *** End of the ENvironemental Details *** 
