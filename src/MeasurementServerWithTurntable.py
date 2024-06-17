# MeasurementServerWithTurntable.py

import rospy
import os
import sys

# 添加robot_arm_tools模块路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'robot_arm_tools', 'src', 'robot_arm_tools'))

from MeasurementServer import MeasurementServer
from src.turntable_control import TurntableController


class MeasurementServerWithTurntable(MeasurementServer):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.turntable_controller = TurntableController()
		# 初始化转台控制器节点
		rospy.init_node('measurement_server_with_turntable')

	def measure(self):
		# 调用父类的measure方法
		super().measure()
		# 添加转盘旋转逻辑，每次旋转5度
		self.rotate_turntable(5)
		return True  # 假设测量成功

	def recovery(self):
		# 可以根据需要实现恢复逻辑，这里简单返回True
		return True

	def rotate_turntable(self, degrees):
		# 使用转台控制器的set_rel_position方法来旋转转台
		self.turntable_controller.set_rel_position(degrees)
		rospy.loginfo(f"Turntable rotated by {degrees} degrees")
