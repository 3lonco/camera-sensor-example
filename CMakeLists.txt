cmake_minimum_required(VERSION 3.5)
project(camera-sensor-example)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(rviz2 REQUIRED)

# Include directories
include_directories(include)

# Create executable
#add_executable(my_node src/my_node.cpp)
#ament_target_dependencies(my_node rclcpp)

# Install
#install(TARGETS my_node
 # DESTINATION lib/${PROJECT_NAME}
#)

install(DIRECTORY launch rviz urdf
  DESTINATION share/${PROJECT_NAME}
)

install(FILES package.xml
  DESTINATION share/${PROJECT_NAME}
)

# Export dependencies
ament_export_dependencies(rclcpp robot_state_publisher rviz2)

ament_package()
