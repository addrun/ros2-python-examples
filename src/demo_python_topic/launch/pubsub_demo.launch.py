# SPDX-License-Identifier: Apache-2.0
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='demo_python_topic', executable='novel_sub_node', output='screen'),
        Node(package='demo_python_topic', executable='novel_pub_node', output='screen'),
    ])
