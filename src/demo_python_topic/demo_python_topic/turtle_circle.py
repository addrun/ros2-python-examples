# SPDX-License-Identifier: Apache-2.0
"""Timer-driven circular motion example for turtlesim."""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleCircleNode(Node):
    def __init__(self, node_name='turtle_circle'):
        super().__init__(node_name)
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        message = Twist()
        message.linear.x = 2.0
        message.angular.z = 1.0
        self.publisher.publish(message)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleCircleNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.try_shutdown()
