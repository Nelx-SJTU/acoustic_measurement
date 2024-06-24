# CMakeLists.txt 和 package.xml 设置正确：

确保在 CMakeLists.txt 中正确地添加了可执行文件并进行了安装。例如：

'''
add_executable(acoustic_measurement_step_node src/acoustic_measurement_step_node.cpp)
target_link_libraries(acoustic_measurement_step_node ${catkin_LIBRARIES})
install(TARGETS acoustic_measurement_step_node RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
'''

确保在 package.xml 中正确声明了依赖项。
