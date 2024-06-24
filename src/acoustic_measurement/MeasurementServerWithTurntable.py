#!/usr/bin/env python3.8

# MeasurementServerWithTurntable.py

import rospy
import os
import sys

from robot_arm_tools.MeasurementServer import MeasurementServer
from acoustic_measurement.turntable_control import TurntableController

class MeasurementServerWithTurntable(MeasurementServer):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.angle = 10.0
		self.turntable_controller = TurntableController()

	def measure(self):
		self.rotate_turntable(self.angle)
		return True

	def recovery(self):
		return True

	def rotate_turntable(self, degrees):
		# Use the set_rel_position function in turntable_controller
		self.turntable_controller.set_rel_position(int(degrees))  # The input has to be int
		rospy.loginfo(f"Turntable rotated by {degrees} degrees")

if __name__ == "__main__":

    turntable_angle = rospy.get_param("turntable_angle",10)

    #Launch ROS service
    MeasurementServerWithTurntable()

    while not rospy.is_shutdown():
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("Shutting down ROS sound measurement server")
            break
