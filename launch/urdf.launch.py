import os
from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros.actions


def generate_launch_description():
    package_dir = get_package_share_directory('camera-sensor-example')
    urdf_file = os.path.join(package_dir, 'urdf', 'mobile_robot.urdf')

    rviz_config_file = os.path.join(package_dir, 'rviz', 'default.rviz')

    urdf = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        arguments=[urdf_file],
    )

    rviz = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config_file],
    )

    return launch.LaunchDescription([
        urdf,
        rviz,
    ])


if __name__ == '__main__':
    generate_launch_description()
