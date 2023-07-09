import rclpy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range, NavSatFix

HALF_DISTANCE_BETWEEN_WHEELS = 0.045
WHEEL_RADIUS = 0.025


class MyRobotDriver:
    def init(self, webots_node, properties):
        self.__robot = webots_node.robot

        self.__left_motor = self.__robot.getDevice('left wheel motor')
        self.__right_motor = self.__robot.getDevice('right wheel motor')
        self.__left_motor.setPosition(float('inf'))
        self.__left_motor.setVelocity(0)
        self.__right_motor.setPosition(float('inf'))
        self.__right_motor.setVelocity(0)
   
        self.__left_sensor = self.__robot.getDistanceSensor('ds0')
        self.__right_sensor = self.__robot.getDistanceSensor('ds1')
        self.__left_sensor.enable(16)
        self.__right_sensor.enable(16)

        self.__gps_left = self.__robot.getDevice('gps_left')
        self.__gps_left.enable(16)

        self.__gps_right = self.__robot.getDevice('gps_right')
        self.__gps_right.enable(16)

        self.__target_twist = Twist()
        
        rclpy.init(args=None)
        self.__node = rclpy.create_node('my_robot_driver')
        self.__node.create_subscription(Twist, 'cmd_vel', self.__cmd_vel_callback, 1)
        self.__node.create_subscription(Twist, 'cmd_velsss', self.__cmd_velss_callback, 1)
        self.__publisher_left = self.__node.create_publisher(Range, 'left_sensor', 1)
        self.__publisher_right = self.__node.create_publisher(Range, 'right_sensor', 1)
        self.__publisher_gps_left = self.__node.create_publisher(NavSatFix, 'gps_left', 1)
        self.__publisher_gps_right = self.__node.create_publisher(NavSatFix, 'gps_right', 1)
        self.left = Range()
        self.right = Range()
        self.gps_msg_left = NavSatFix()
        self.gps_msg_right = NavSatFix()

    def __cmd_vel_callback(self, twist):
        self.__target_twist = twist

    def __cmd_velss_callback(self, twist):
        self.left.range = self.__left_sensor.getValue()
        self.right.range = self.__right_sensor.getValue()
        self.__publisher_left.publish(self.left)
        self.__publisher_right.publish(self.right)
        self.gps_msg_left.latitude, self.gps_msg_left.longitude, self.gps_msg_left.altitude = self.__gps_left.getValues()
        self.gps_msg_right.latitude, self.gps_msg_right.longitude, self.gps_msg_right.altitude = self.__gps_right.getValues()
        self.__publisher_gps_left.publish(self.gps_msg_left)
        self.__publisher_gps_right.publish(self.gps_msg_right)


    def step(self):
        rclpy.spin_once(self.__node, timeout_sec=0)

        forward_speed = self.__target_twist.linear.x
        angular_speed = self.__target_twist.angular.z

        command_motor_left = (forward_speed - angular_speed * HALF_DISTANCE_BETWEEN_WHEELS) / WHEEL_RADIUS
        command_motor_right = (forward_speed + angular_speed * HALF_DISTANCE_BETWEEN_WHEELS) / WHEEL_RADIUS

        self.__left_motor.setVelocity(command_motor_left)
        self.__right_motor.setVelocity(command_motor_right)

