# SPDX-License-Identifier: Apache-2.0
"""Subscriber callback -> bounded queue -> background log worker."""
import queue
import threading
from example_interfaces.msg import String
import rclpy
from rclpy.node import Node

class NovelSubnode(Node):
    def __init__(self, node_name='novel_sub'):
        super().__init__(node_name)
        self.messages = queue.Queue(maxsize=100)
        self.stopping = threading.Event()
        self.subscription = self.create_subscription(String, 'novel', self.novel_callback, 10)
        self.worker = threading.Thread(target=self.consume, daemon=True)
        self.worker.start()

    def novel_callback(self, message):
        try:
            self.messages.put_nowait(message.data)
        except queue.Full:
            self.get_logger().warning('Worker queue is full; dropping a message.')

    def consume(self):
        while not self.stopping.is_set():
            try:
                text = self.messages.get(timeout=0.1)
            except queue.Empty:
                continue
            self.get_logger().info(f'Received: {text}')

    def stop_worker(self):
        self.stopping.set()
        self.worker.join(timeout=2.0)

def main(args=None):
    rclpy.init(args=args)
    node = NovelSubnode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.stop_worker()
        node.destroy_node()
        rclpy.try_shutdown()
