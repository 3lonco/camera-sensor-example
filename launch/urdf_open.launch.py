import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import launch
import launch_ros

def generate_launch_description():
    try:
        # URDFファイルのパスを取得
        pkg_share = get_package_share_directory('camera-sensor-example')
    except FileNotFoundError as e:
        print(f"PackageNotFoundError: {e}")
        return LaunchDescription()

    try:
        urdf_file = os.path.join(pkg_share, 'urdf', 'mobile_robot.urdf')
        # 以降の処理
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return LaunchDescription()
    # RViz設定ファイルのパスを取得
    rviz_config_file = os.path.join(pkg_share, 'rviz', 'defalut.rviz')

    # launchファイルのパラメータ設定
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    # RVizノードの起動
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=["-d", rviz_config_file]
    )

    # URDFロードノードの起動
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'use_sim_time': use_sim_time}],
        arguments=[urdf_file]
    )
    joint_state_pub_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen",
    )

    # launchファイルの構成
    ld = LaunchDescription()

    # launchファイルへの引数の追加
    ld.add_action(DeclareLaunchArgument(
        'use_sim_time',
        default_value=use_sim_time,
        description='Use simulation/Gazebo clock if true'))

    # ノードの起動
    ld.add_action(rviz_node)
    ld.add_action(robot_state_publisher_node)
    ld.add_action(joint_state_pub_gui_node)

    return ld
def main(argv=None):
    # Create launch description and execute it
    ld = generate_launch_description()
    launch.launch(ld)

if __name__ == '__main__':
    main()