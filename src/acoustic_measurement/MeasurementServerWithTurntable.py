#!/usr/bin/env python3.8

# MeasurementServerWithTurntable.py

import rospy
import os
import sys

from robot_arm_tools.MeasurementServer import MeasurementServer
from acoustic_measurement.turntable_control import TurntableController

class MeasurementServerWithTurntable(MeasurementServer):
	def __init__(self, angle, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.angle = angle
		self.turntable_controller = TurntableController()

	def measure(self):
		# 调用父类的measure方法
		# super().measure()
		# 添加转盘旋转逻辑，每次旋转10度
		self.rotate_turntable(self.angle)
		return True  # 假设测量成功

	def recovery(self):
		# 可以根据需要实现恢复逻辑，这里简单返回True
		return True

	def rotate_turntable(self, degrees):
		# 使用转台控制器的set_rel_position方法来旋转转台
		self.turntable_controller.set_rel_position(degrees)
		rospy.loginfo(f"Turntable rotated by {degrees} degrees")

if __name__ == "__main__":

    angle = rospy.get_param("turntable_angle",10)

    #Launch ROS service
    MeasurementServerWithTurntable(angle)

    while not rospy.is_shutdown():
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("Shutting down ROS sound measurement server")
            break
