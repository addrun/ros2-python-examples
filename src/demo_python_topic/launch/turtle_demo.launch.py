# SPDX-License-Identifier: Apache-2.0
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('target_x', default_value='1.0'),
        DeclareLaunchArgument('target_y', default_value='1.0'),
        Node(package='turtlesim', executable='turtlesim_node', output='screen'),
        Node(package='demo_python_topic', executable='turtle_control', output='screen', parameters=[{
            name: ParameterValue(LaunchConfiguration(name), value_type=float)
            for name in ['target_x', 'target_y']}]),
    ])
