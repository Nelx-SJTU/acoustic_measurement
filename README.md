# Run the Example node
'''
roslaunch acoustic_measurement TurntableExample.launch robot_name:=ur10e tool_name:=speaker_asm simulation:=true
'''

# Run the scan node
The control of turntable is written in acoustic_measurement_step_node.cpp, in robot.runMeasurementRoutine(). 
'''
roscore
rosrun turntable_ros turntable_node
roslaunch acoustic_measurement TurntableScan.launch robot_name:=ur10e tool_name:=speaker_asm simulation:=true
rosparam set measurementServerName turntable
rosrun acoustic_measurement test_measurement_server_with_turntable.py
'''

# Run the turntable test code
'''
rosrun acoustic_measurement turntable_control.py
'''
