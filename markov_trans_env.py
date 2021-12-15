from generate_transistion_probability_matrix import generate_transistion_matrix
import numpy as np



if __name__ == "__main__":

    DIMENSION = (20,20)

    env_map_transistion_matrix = np.zeros((20,20,9,9))
    env_map_transistion_matrix_2 = np.zeros((20,20,9,9))


    for i in range(DIMENSION[0]):
        for j in range(DIMENSION[1]):
            env_map_transistion_matrix[i,j] = generate_transistion_matrix()

    for i in range(DIMENSION[0]):# THis Phenemenon. How it Works?
        for j in range(DIMENSION[1]):
            env_map_transistion_matrix_2[i] = generate_transistion_matrix()
    






    print("Details")
    #print(env_map_transistion_matrix.shape)
    print(env_map_transistion_matrix)
    print(env_map_transistion_matrix.shape)

    if (env_map_transistion_matrix.shape == env_map_transistion_matrix_2.shape):
        print("True")

    count = 0
    for i in range(20):
        for j in range(20):

            print("i and j",i,j)
            print(env_map_transistion_matrix[i,j])
            for k in range(9):
                print("k",k,np.sum(env_map_transistion_matrix[i,j,k]))
            count = count +1 
            print(count)

    test_vector = np.zeros(9)
    test_vector[5]= 1

    qwerty = np.dot(env_map_transistion_matrix[1,2],test_vector)
    print(qwerty, np.sum(qwerty))
    print("Test Successful!")