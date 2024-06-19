# Step 1 : Rescale the stl file
'''
cd ~/catkin_ws/src/acoustic_measurement/config/tools
'''
Set the scale_factor in STLRescale.py.
Normally it is 0.001 (Transform from mm to m)
'''
python3 STLRescale.py
'''


# Step 2 : Create a new tool
Calculate the transform vector of tool. (m)
coordinate: x - front, y - down, z - outside
EE_X = -0.090
EE_Y = 0.090675
EE_Z = -0.038
EE_RX = 1.57
EE_RY = 0.0
EE_RZ = 0.0
collisions_safety_distance = 0.1
tool_mass = 0.8

'''
cd ~/catkin_ws/src/robot_arm_tools/config/tools
./NewTool.sh ~/catkin_ws/src/acoustic_measurement/config/tools/speaker/speaker_asm.stl -0.090 0.090675 -0.038 1.57 0.0 0.0 0.1 0.8
'''
