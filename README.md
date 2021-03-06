# MECA470_AgPods
### MECA 470 Robotic Engineering Project
----------------------------------------------------------------------------------

AgPods Project
<p align = "center">
  Project Members:
  Joseph Oliveri,
  Travis Bybee,
  Nick McConnell
  </p>
  
  <center>
   <h4> California State University Chico</h4>
   <h4> College of Mechanical and Mechatronic Engineering and Advance Manufacturing</h4> 
   <h4> MECA 470 Robotic Engineering</h4> 
   <h4> AgPods</h4> 
</center>

#### Table of Contents
- [1. Introduction](#1-Introduction)
- [2. Cable Robot Degrees Of Freedom](#2-Cable-Robot-Degrees-Of-Freedom)
- [3. Ineverse Kinematics](#3-Ineverse-Kinematics) 
- [4. CoppeliaSim Model](#4-CoppeliaSim-Model)
- [5. ROS API](#5-ROS-API)
- [6. Case-to-go-Forward](#6-Case-to-go-Forward)
- [7. References](#7-References)

## 1. Introduction 
The goal of this project is to create an open hydroponic agriculture platform to streamline current systems that are inefficient and expensive. By utilizing an automated and low-cost concept, coupled with an AI robotic system, we aim to assist growers by tracking, identifying, and optimizing their growing recipes.

## 2. Cable Robot Degrees Of Freedom

We decided to use a design with 4 towers that anchor the support and joint system for the end-effector. The original idea of using a UPU design only provided 2 DoF, so we decided to use a SPS system instead, in which we are able to achieve a 6 degrees of freedom. The SPS system does provide 6 DoF with 3 and 4 towers, however to achieve a larger workspace and more stability we chose to use 4 towers. We solved for the DoF by using Grubler's formula as seen in our work below:

![GrublersFormula](https://user-images.githubusercontent.com/60329920/102401463-36172f00-3f98-11eb-9b34-4a9785f08670.JPG)
 
![AgPodDOF](https://user-images.githubusercontent.com/60329920/102401546-5cd56580-3f98-11eb-9ea6-af8ae86648e0.JPG)

## 3. Ineverse Kinematics

By using only 4 towers with wires in tension to support the end-effector, this mechanism is considered an Incompletely Restrained Parallel Mechanism (IRPM). IRPM systems require at least one dynamical equation added to the unilateral constraints induced by the tensed wires to describe to pose for the end effector. Found below are the hand calculations performed for our system:

![MECA 470 Project - Inverse Kinematics-1](https://user-images.githubusercontent.com/60329920/102404500-aa53d180-3f9c-11eb-8c30-c0b7489ccff2.jpg)
![MECA 470 Project - Inverse Kinematics-2](https://user-images.githubusercontent.com/60329920/102404512-acb62b80-3f9c-11eb-80f2-5be438a3e657.jpg)

We needed to add a thickness to the end-effector and offsets to the joints, which are then subtracted from the P before substituting into the equations.

## 4. CoppeliaSim Model
![image](https://user-images.githubusercontent.com/73966901/102735302-e5d10180-42f6-11eb-8e24-fbed19d97bc0.png)

The CoppeliaSim Model seen above can be found here: 
[Hydroponic_System_Coppelia](https://github.com/Tebybee8/MECA470_AgPods/blob/main/V5_Hydroponics_System_Coppelia(Squared_Base).ttt)

The CoppeliaSim Child Script can be found here:
[Child_Script](https://github.com/Tebybee8/MECA470_AgPods/blob/main/ChildScript.lua)
This Child Scirpt was later implimented into ROS to allow the user to move the end effector to desired locations and orientations.

## 5. ROS API

To Connect the ROS API to the CoppeliaSim Model, follow the steps below:

1. Navigate to the ROS-I Training (Kinetic) Network Settings on the Oracle VM Virtual Box Manager and enable Bridged Adapter
![NetworkSettings](https://user-images.githubusercontent.com/60329920/102727348-10609180-42da-11eb-8d13-91a7b455356e.JPG)

2. Download the [AgPod_ROS_API](https://github.com/Tebybee8/MECA470_AgPods/blob/main/AgPod_ROS_API.zip) files.

3. To ensure that the user computer is linked with CoppeliaSim, edit the AgBot_Program.py file with your Wireless LAN IPv4 address.

4. Once both ROS and CoppeliaSim are open and running, navigate to the directory where you stored the API files and run `python3 AgBot_Program.py` in terminal to begin the API

5. The script will ask for a, b, and c rotation (in degrees) followed by x,y, and z (in meters) location for the end-effector.

6. Once completed the API will begin the simulation in CoppeliaSim and move to the desired orientation.

#### Please Note: 
- You must have numpy installed onto your ROS machine.
- The current RemoteAPI file is configured for Ubuntu 16, so if you are using any other version you must download the RemoteAPI file for that version.
- The DLL file is different for 32-bit and 64-bit devices.
- The current scipts are configured to work for pyton3.5 and above. If you are using an older version you must reconfigure the script.
   
## 6. Case to go Forward

This system currently allows the user to move the robot's end-effector to a desired location with a defined orientation through the provided ROS workspace. Future implimentations of a vision system would allow the AgPod to detect where the desired plants are and move to their locations in real time. This vision system could allow the user to place the plants in various orientations without having issues within the systems operations. 

Another consideration in the future versions of this system would be to add an end effector to the plate we currently have in our model. This end effector could be a complient gripper to pick and place seeds or actual vegetables from the plants. A pneumatic actuator would most likely have to be incorporated into the system in order to meet the functionality of the end effector. 

If the idea of hydroponics becomes undesirable, there were also possible contigency pathways discussed. This end effector could also incorporate a tube that connects to a nearby watertank in order to water the plants when desired. A schedule of these watering operations could be outlined by the user and the system would have to move the end effector over those plants before actuating a pump in the watertank to supply water at the tip of the end effector. 

Overall, this system has proved as a proper foundation for creating an autonomous agricultural cell that can be implimented in a variety of enviornments.

## 7. References
[1] Lynch, Kevin, and Frank C. Park. Modern Robotics: Mechanics, Planning, and Control. Cambridge, United Kingdom: Cambridge UP, 2017. Print.  
[2] Niku, Saeed B. Introduction to Robotics Analysis, Control, Applications. Third ed. John Wiley &amp; Sons. Print.  
