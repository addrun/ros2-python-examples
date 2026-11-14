# SPDX-License-Identifier: Apache-2.0
"""Minimal ROS 2 Python node and log example."""
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node = Node('python_node')
    node.get_logger().info('Hello, ROS 2!')
    node.get_logger().warning('This is a learning example.')
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
