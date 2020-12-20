import numpy as np
import sim
import sys
import time
import random

def a_Vectors(int):
    Column = np.array([a*np.cos(np.radians((int-1)*Spacing)), a*np.sin(np.radians((int-1)*Spacing)), 0, 1]) 
    a_Matrix = np.array(Column).reshape(4,1)
    print(a_Matrix)
    return a_Matrix

def Initial_b_Vectors(int):
    Column = np.array([b*np.cos(np.radians((int-1)*Spacing)), b*np.sin(np.radians((int-1)*Spacing)), 0, 1])
    Initial_b_Matrix = np.array(Column).reshape(4,1)
    print(Initial_b_Matrix)
    return Initial_b_Matrix

def Roll_Matrix():
    My_Roll_Matrix = np.array([[1, 0, 0, 0], [0, np.cos(np.radians(Roll)), -np.sin(np.radians(Roll)), 0], 
                 [0, np.sin(np.radians(Roll)), np.cos(np.radians(Roll)), 0], [0, 0, 0, 1]])
    print(My_Roll_Matrix)
    return My_Roll_Matrix

def Pitch_Matrix():
    My_Pitch_Matrix = np.array([[np.cos(np.radians(Pitch)), 0, np.sin(np.radians(Pitch)), 0], [0, 1, 0, 0], 
                 [-np.sin(np.radians(Pitch)), 0, np.cos(np.radians(Pitch)), 0], [0, 0, 0, 1]])
    print(My_Pitch_Matrix)
    return My_Pitch_Matrix

def Yaw_Matrix():
    My_Yaw_Matrix = np.array([[np.cos(np.radians(Yaw)), -np.sin(np.radians(Yaw)), 0, 0], [np.sin(np.radians(Yaw)), np.cos(np.radians(Yaw)), 0, 0], 
                 [0, 0, 1, 0], [0, 0, 0, 1]])
    print(My_Yaw_Matrix)
    return My_Yaw_Matrix

def Euler_Matrix():
    My_Euler_Matrix = np.array([[np.cos(np.radians(Yaw))*np.cos(np.radians(Pitch)), np.cos(np.radians(Yaw))*np.sin(np.radians(Pitch))*np.sin(np.radians(Roll)) - np.sin(np.radians(Yaw))*np.cos(np.radians(Roll)), np.cos(np.radians(Yaw))*np.sin(np.radians(Pitch))*np.cos(np.radians(Roll)) + np.sin(np.radians(Yaw))*np.sin(np.radians(Roll)), 0], 
                          [np.sin(np.radians(Yaw))*np.cos(np.radians(Pitch)), np.sin(np.radians(Yaw))*np.sin(np.radians(Pitch))*np.sin(np.radians(Roll)) + np.cos(np.radians(Yaw))*np.cos(np.radians(Roll)), np.sin(np.radians(Yaw))*np.sin(np.radians(Pitch))*np.cos(np.radians(Roll)) - np.cos(np.radians(Yaw))*np.sin(np.radians(Roll)), 0], 
                          [-np.sin(np.radians(Pitch)), np.cos(np.radians(Pitch))*np.sin(np.radians(Roll)), np.cos(np.radians(Pitch))*np.cos(np.radians(Roll)), 0], 
                          [0, 0, 0, 1]])
    print(My_Euler_Matrix)
    return My_Euler_Matrix

def d_Vector_Magnitude(array):
    Magnitude = np.sqrt(array.item(0)**2 + array.item(1)**2 + array.item(2)**2)
    print(Magnitude)
    return Magnitude

if __name__ == '__main__':
    a = .07071  # Radius to the center of the end effector
    b = .4950   # Radius to the center of the fixed base 
    Spacing = 90    # Joint spacing
    Roll = int(input('Enter the angle of rotation about the x-axis: '))
    Pitch = int(input('Enter the angle of rotation about the y-axis: '))
    Yaw = int(input('Enter the angle of rotation about the z-axis: '))
    P = list(map(float, (input('Enter the x, y, and z vector magnitudes for the desired location P(seperated by a space): ').split())))
    P.append(1)
    P_Matrix = np.array(P).reshape(4,1)
#    print(f'P_Matrix is:\n {P_Matrix} \n')
    a_Cable_1 = a_Vectors(1)
    a_Cable_2 = a_Vectors(2)
    a_Cable_3 = a_Vectors(3)
    a_Cable_4 = a_Vectors(4)
    Initial_b_Cable_1 = Initial_b_Vectors(1)
    Initial_b_Cable_2 = Initial_b_Vectors(2)
    Initial_b_Cable_3 = Initial_b_Vectors(3)
    Initial_b_Cable_4 = Initial_b_Vectors(4)
    Roll_Matrix = Roll_Matrix()
    Pitch_Matrix = Pitch_Matrix()
    Yaw_Matrix = Yaw_Matrix()
    Identity_Matrix = np.identity(4)
    Euler_Matrix = Euler_Matrix()
    New_b_Cable_1 = np.matmul(Euler_Matrix, Initial_b_Cable_1)
    New_b_Cable_2 = np.matmul(Euler_Matrix, Initial_b_Cable_2)
    New_b_Cable_3 = np.matmul(Euler_Matrix, Initial_b_Cable_3)
    New_b_Cable_4 = np.matmul(Euler_Matrix, Initial_b_Cable_4)
    d_Matrix_Cable_1 = P_Matrix + New_b_Cable_1 - a_Cable_1
    d_Matrix_Cable_2 = P_Matrix + New_b_Cable_2 - a_Cable_2
    d_Matrix_Cable_3 = P_Matrix + New_b_Cable_3 - a_Cable_3
    d_Matrix_Cable_4 = P_Matrix + New_b_Cable_4 - a_Cable_4
    print(d_Matrix_Cable_1)
    Cable_1_Length = d_Vector_Magnitude(d_Matrix_Cable_1)
    Cable_2_Length = d_Vector_Magnitude(d_Matrix_Cable_2)
    Cable_3_Length = d_Vector_Magnitude(d_Matrix_Cable_3)
    Cable_4_Length = d_Vector_Magnitude(d_Matrix_Cable_4)

    # Connect to CoppeliaSim
    sim.simxFinish(-1)
    your_IP='192.168.1.5'
    clientID = sim.simxStart(your_IP,19997,True,True,10000,5)
    if clientID != -1:
        print("Connected to remote API server")
    else:
        print("Not connected to remote API server")
        sys.exit ("could not connect")

    #-----Start the Paused Simulation
    err_code = sim.simxStartSimulation(clientID,sim.simx_opmode_oneshot)
    # Call the joints
    err_code,j1 = sim.simxGetObjectHandle(clientID,"rope1",sim.simx_opmode_blocking)
    err_code,j2 = sim.simxGetObjectHandle(clientID,"rope2",sim.simx_opmode_blocking)
    err_code,j3 = sim.simxGetObjectHandle(clientID,"rope3",sim.simx_opmode_blocking)
    err_code,j4 = sim.simxGetObjectHandle(clientID,"rope4",sim.simx_opmode_blocking)

    pos_val = Cable_1_Length # in meters
    err_code = sim.simxSetJointTargetPosition (clientID, j1,pos_val,sim.simx_opmode_streaming) # set the postion of J1
    time.sleep(1) #wait a short amount of time

    pos_val = Cable_2_Length # in meters
    err_code = sim.simxSetJointTargetPosition (clientID, j2,pos_val,sim.simx_opmode_streaming) # set the postion of J2
    time.sleep(1) #wait a short amount of time

    pos_val = Cable_3_Length # in meters
    err_code = sim.simxSetJointTargetPosition (clientID, j3,pos_val,sim.simx_opmode_streaming) # set the postion of J3
    time.sleep(1) #wait a short amount of time

    pos_val = Cable_4_Length # in degrees 0 # in degrees 0
    err_code = sim.simxSetJointTargetPosition (clientID, j4,pos_val,sim.simx_opmode_streaming) # set the postion of J4
    time.sleep(1) #wait a short amount of time

