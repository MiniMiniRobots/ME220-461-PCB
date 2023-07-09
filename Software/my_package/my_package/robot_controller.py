import rclpy, time
from rclpy.node import Node
from std_msgs.msg import String
# from my_package.msg import RobotPos
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist, Vector3

MAX_RANGE = 0.15

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.__publisher = self.create_publisher(Twist, 'cmd_vel', 1)
        self.__publisher = self.create_publisher(String, 'robot_command', 1)

        self.create_subscription(Range, 'left_sensor', self.__left_sensor_callback, 1)
        self.create_subscription(Range, 'right_sensor', self.__right_sensor_callback, 1)
        self.control_robot()

    def __left_sensor_callback(self, message):
        self.__left_sensor_value = message.range

    def __right_sensor_callback(self, message):
        self.__right_sensor_value = message.range

        command_message = Twist()

        command_message.linear.x = 0.1

        if self.__left_sensor_value < 0.9 * MAX_RANGE or self.__right_sensor_value < 0.9 * MAX_RANGE:
            command_message.angular.z = -2.0

        self.__publisher.publish(command_message)

    def command_robot(self, command):
        # command_message = RobotPos()
        # command_message.robotName = "robot1"
        # command_message.command = Vector3()
        # command_message.command.x = float(command)
        command_message = String()
        command_message.data = command
        self.__publisher.publish(command_message)
    
    def control_robot(self):
        while rclpy.ok():
            self.command_robot('1')
            time.sleep(0.1)


def main(args=None):
    rclpy.init(args=args)
    avoider = RobotController()
    rclpy.spin(avoider)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    avoider.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
