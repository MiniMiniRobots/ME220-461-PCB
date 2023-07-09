#!/usr/bin/env python3.8

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float32
import socket
import time
from geometry_msgs.msg import Twist

class SocketNode(Node):
    def __init__(self):
        super().__init__('socket_node')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_address = ('192.168.1.108', 8000)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.msg = Float32()
        self.msg.data = 991.0
        self.subscription = self.create_subscription(
            Float32,
            'turn',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.msg.data = msg.data
        self.get_logger().info(f'Received: "{msg.data}"')

    def timer_callback(self):
        self.get_logger().info(f'Publishing: "{self.msg.data}"')
        sent = self.sock.sendto(str(self.msg.data).encode(), self.server_address)


def main(args=None):
    rclpy.init(args=args)
    node = SocketNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
