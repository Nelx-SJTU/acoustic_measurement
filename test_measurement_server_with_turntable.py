#!/home/student/anaconda3/envs/acoustic/bin/python

# test_measurement_server_with_turntable.py
import sys
import os
import rospy

from acoustic_measurement.MeasurementServerWithTurntable import MeasurementServerWithTurntable

if __name__ == "__main__":
    
    # Launch ROS node
    # rospy.init_node('turntable_measurement_server')

    # Launch ROS service
    MeasurementServerWithTurntable()

    while not rospy.is_shutdown():
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("Shutting down ROS sound measurement server")
            break

	
