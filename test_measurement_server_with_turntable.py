# test_measurement_server_with_turntable.py
import sys
import os

# 添加robot_arm_tools模块路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'robot_arm_tools', 'src', 'robot_arm_tools'))

from src.MeasurementServerWithTurntable import MeasurementServerWithTurntable


def main():
	# 初始化测量服务器
	measurement_server = MeasurementServerWithTurntable()

	# 模拟测量过程，并控制转台旋转
	for _ in range(10):  # 测试循环10次，每次转动5度
		measurement_server.measure()


if __name__ == "__main__":
	main()
