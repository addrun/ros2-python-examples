# SPDX-License-Identifier: Apache-2.0
"""Publish bundled original sample lines, without network access."""
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from example_interfaces.msg import String
import rclpy
from rclpy.node import Node

class NovelPubNode(Node):
    def __init__(self, node_name='novel_pub'):
        super().__init__(node_name)
        default = str(Path(get_package_share_directory('demo_python_topic')) / 'data/demo_lines.txt')
        self.declare_parameter('text_file', default)
        self.declare_parameter('period', 1.0)
        self.declare_parameter('repeat', True)
        period = self.get_parameter('period').value
        if period <= 0:
            raise ValueError('period must be positive.')
        path = Path(self.get_parameter('text_file').value).expanduser()
        self.lines = [line.strip() for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
        if not self.lines:
            raise ValueError(f'No sample lines found in {path}')
        self.index = 0
        self.publisher = self.create_publisher(String, 'novel', 10)
        self.timer = self.create_timer(period, self.timer_callback)

    def timer_callback(self):
        if self.index >= len(self.lines):
            if self.get_parameter('repeat').value:
                self.index = 0
            else:
                self.timer.cancel()
                return
        message = String()
        message.data = self.lines[self.index]
        self.publisher.publish(message)
        self.get_logger().info(f'Published: {message.data}')
        self.index += 1

def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = NovelPubNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node is not None:
            node.destroy_node()
        rclpy.try_shutdown()
