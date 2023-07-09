import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import json
import socket


MAX_RANGE = 0.15
TIME_STEP = 64
MAX_SPEED = 6.28

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__('obstacle_avoider')

        self.__publisher = self.create_publisher(Twist, 'cmd_vel', 1)
        self.__publisherTurn = self.create_publisher(String, 'turn', 1)
        self.__left_sensor_value = 99999
        self.__right_sensor_value = 99999

        self.create_subscription(Range, 'left_sensor',
                                 self.__left_sensor_callback, 1)
        self.create_subscription(
            Range, 'right_sensor', self.__right_sensor_callback, 1)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to the Raspberry Pi Pico
        self.sock.connect(('192.168.48.220', 8000))
        self.server_address = ('192.168.48.220', 8000)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.command_message = String()
        self.command_message.data = "s"
        self.__target_twist = Twist()


    def __left_sensor_callback(self, message):
        self.__left_sensor_value = message.range
        #self.get_logger().info("Going forwards")
        self.calc_pos()

    def __right_sensor_callback(self, message):
        self.__right_sensor_value = message.range
        #self.get_logger().info("Going forwards")
        self.calc_pos()

    def calc_pos(self):

        self.left_obstacle = False
        self.right_obstacle = False
        # leftSpeed  = 0.5 * MAX_SPEED
        # rightSpeed = 0.5 * MAX_SPEED
        self.command_message.data = "s"
        self.__target_twist.linear.x = 0.1
        self.get_logger().info("Going forwards")

        if self.__left_sensor_value < 0.9 * MAX_RANGE and self.__right_sensor_value < 0.9 * MAX_RANGE:
            self.command_message.data = "b"
            self.__target_twist.linear.x = -0.1
            self.get_logger().info("Going backwards")

        elif self.__left_sensor_value < 0.9 * MAX_RANGE:
            self.left_obstacle = True
            self.command_message.data = "l"
            self.__target_twist.angular.z = 0.1
            self.get_logger().info("Turn Left")
            # leftSpeed  = 0.5 * MAX_SPEED
            # rightSpeed = -0.5 * MAX_SPEED
        
        elif self.__right_sensor_value < 0.9 * MAX_RANGE:
            self.right_obstacle = True
            self.command_message.data = "r"
            self.__target_twist.angular.z = -0.1
            self.get_logger().info("Turn Right")

            # leftSpeed  = -0.5 * MAX_SPEED
            # rightSpeed = 0.5 * MAX_SPEED


    def timer_callback(self):

        #sent = self.sock.sendto(str(self.msg.data).encode(), self.server_address)
        self.__publisher.publish(self.__target_twist)
        self.sock.sendall(self.command_message.data.encode())
        response = self.sock.recv(1024).decode().strip()

def main(args=None):
    rclpy.init(args=args)
    avoider = ObstacleAvoider()
    rclpy.spin(avoider)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    avoider.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
