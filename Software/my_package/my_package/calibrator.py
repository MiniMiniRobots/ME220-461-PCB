import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
from geometry_msgs.msg import Twist, Point
from std_msgs.msg import Float32,Int32
import math
import time
from std_msgs.msg import Bool

class Calibrator(Node):
    def __init__(self):
        super().__init__('calibrator')
        self.gps_left = None
        self.gps_right = None
        self.cm = None
        self.direction = 0.0
        self.last_turn_time = None
        self.turning_time = 0
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        self.publisher_turn = self.create_publisher(Float32, 'turn', 10)
        self.publisher_ids = self.create_publisher(Int32, 'aruco_id', 10)
        self.subscription_gps_left = self.create_subscription(
            NavSatFix,
            'gps_left',
            self.listener_callback_gps_left,
            10)
        self.subscription_gps_right = self.create_subscription(
            NavSatFix,
            'gps_right',
            self.listener_callback_gps_right,
            10)
        self.subscription_cm = self.create_subscription(
            Point,
            'center_of_mass_cm',
            self.listener_callback_cm,
            10)
        self.timer = self.create_timer(0.1, self.compare_values)
        self.ids = [15,4,1,2]
        self.i = 0
        self.aruco_id = Int32()
        self.aruco_id.data = self.ids[self.i]

    def listener_callback_gps_left(self, msg):
        self.gps_left = msg

    def listener_callback_gps_right(self, msg):
        self.gps_right = msg

    def listener_callback_cm(self, msg):
        self.cm = msg

    def calculate_center_of_mass(self):
        # Calculate center of mass based on GPS readings
        cm_x = (self.gps_left.longitude + self.gps_right.longitude) / 2
        cm_y = (self.gps_left.latitude + self.gps_right.latitude) / 2
        return Point(x=cm_x, y=cm_y, z=0.0)

    def calculate_distance(self):
        # Calculate Euclidean distance
        return math.sqrt((self.cm.x - self.gps.x)**2 + (self.cm.y - self.gps.y )**2)

    def calculate_angle(self):
        # Calculate angle (in radians) for turning
        return math.atan2(self.gps.x - self.cm.x, self.gps.y - self.cm.y)

    def calculate_angle_between_gps(self):
        # Calculate angle between the two GPS sensors
        return math.atan2(self.gps_left.longitude - self.gps_right.longitude,
                          self.gps_left.latitude - self.gps_right.latitude)

    def compare_values(self):
        if self.gps_left is not None and self.gps_right is not None and self.cm is not None:
            self.gps = self.calculate_center_of_mass()
            distance = self.calculate_distance()
            angle = self.calculate_angle() / math.pi * 180 + 180
            theta = self.calculate_angle_between_gps() / math.pi * 180 - 90

            if theta < -180  and theta > -270:
                theta += 360

            elif theta > 180:
                theta -= 360

            if angle > 180:
                angle -= 360

            self.get_logger().info(f'Distance to target: {distance}')
            self.get_logger().info(f'Self.cm: {self.cm.x}, {self.cm.y}')
            self.get_logger().info(f'Self.gps: {self.gps.x}, {self.gps.y}')
            #self.get_logger().info(f'theta: {theta}')

            self.get_logger().info(f'Distance to target: {distance}, Angle to target: {angle}, Theta: {theta}')

            twist = Twist()
            doruk = Float32()
            # If distance is greater than threshold, move robot
            if distance > 0.1:
                # rotate to face the target
                if abs(theta - angle ) > 5:
                    self.last_turn_time = self.last_turn_time or time.time()
                    if angle > 0:
                        # turn right (clockwise)
                        twist.angular.z = 0.1
                        doruk.data = 40.125
                    else:
                        # turn left (counterclockwise)
                        twist.angular.z = -0.1
                        doruk.data = 30.125
                    # move forward with constant speed, only if angle is small enough (less than 10 degrees here)
                else:
                    self.last_turn_time = None
                    twist.linear.x = 0.01
                    doruk.data = 10.750
            else:
                # stop if target is close enough
                twist.angular.z = 0.0
                twist.linear.x = 0.0
                doruk.data = 20.125
                self.i += 1
                if self.i > 3:
                    self.i = 0
                
                self.aruco_id.data = 15

            #self.direction += (twist.angular.z * self.turning_time) / math.pi * 180 / 52
            #self.get_logger().info(f'Current direction: {self.direction}')

            self.publisher_.publish(twist)
            self.publisher_turn.publish(doruk)
            self.publisher_ids.publish(self.aruco_id)

def main(args=None):
    rclpy.init(args=args)
    calibrator = Calibrator()
    rclpy.spin(calibrator)

    calibrator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
