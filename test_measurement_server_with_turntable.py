#!/home/student/anaconda3/envs/acoustic/bin/python

# test_measurement_server_with_turntable.py
import sys
import os
import rospy

# 添加robot_arm_tools模块路径
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'robot_arm_tools', 'src', 'robot_arm_tools'))

from acoustic_measurement.MeasurementServerWithTurntable import MeasurementServerWithTurntable

if __name__ == "__main__":
    
    #Launch ROS node
    rospy.init_node('turntable_measurement_server')

    #Launch ROS service
    MeasurementServerWithTurntable(30)

    while not rospy.is_shutdown():
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("Shutting down ROS sound measurement server")
            break

	
