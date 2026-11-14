# SPDX-License-Identifier: Apache-2.0
"""Drive turtle1 to a parameterized target using signed angle error."""
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from demo_python_topic.control_math import compute_velocity

class TurtleControlNode(Node):
    def __init__(self, node_name='turtle_control'):
        super().__init__(node_name)
        for name, value in [('target_x', 1.0), ('target_y', 1.0),
                            ('gain', 1.0), ('max_speed', 3.0),
                            ('max_turn_rate', 2.0), ('tolerance', 0.1)]:
            self.declare_parameter(name, value)
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)

    def pose_callback(self, pose):
        values = {name: self.get_parameter(name).value for name in
                  ['target_x', 'target_y', 'gain', 'max_speed', 'max_turn_rate', 'tolerance']}
        message = Twist()
        message.linear.x, message.angular.z = compute_velocity(pose.x, pose.y, pose.theta, **values)
        self.publisher.publish(message)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if rclpy.ok():
            node.publisher.publish(Twist())
        node.destroy_node()
        rclpy.try_shutdown()
