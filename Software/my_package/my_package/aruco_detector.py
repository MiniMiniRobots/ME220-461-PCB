#!/usr/bin/env python

import rclpy
from rclpy.node import Node
import cv2
import cv2.aruco as aruco
import numpy as np
from geometry_msgs.msg import Point
import time
from std_msgs.msg import Bool

class ArucoDetector(Node):

    def __init__(self):
        super().__init__('aruco_detector')
        #self.pub_width = self.create_publisher(String, 'visible_width_cm', 10)
        #self.pub_height = self.create_publisher(String, 'visible_height_cm', 10)
        #self.pub_center_px = self.create_publisher(String, 'center_of_mass_px', 10)
        self.pub_center_cm = self.create_publisher(Point, 'center_of_mass_cm', 10)
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        self.parameters = aruco.DetectorParameters_create()
        self.marker_size_cm = 5.0
        self.cap = cv2.VideoCapture(2)
        # self.is_available = Bool()
        # self.is_available.data = True
        # self.subscription_result = self.create_subscription(
        #     Bool,
        #     'is_available',
        #     self.result_callback,
        #     10)
        

        if not self.cap.isOpened():
            self.get_logger().info("Cannot open camera")
            return

        self.timer = self.create_timer(1, self.timer_callback)

    # def result_callback(self, msg):
    #     self.is_available.data = msg.data
    #     print(self.is_available.data)

    def timer_callback(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().info("Can't receive frame (stream end?). Exiting ...")
            self.cap.release()
            cv2.destroyAllWindows()
            return
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.parameters)
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
        if ids is not None:
            for i, id in enumerate(ids):
                if id == 4:
                    pixel_length = np.linalg.norm(corners[i][0][0] - corners[i][0][1])
                    pixel_to_cm_ratio = self.marker_size_cm / pixel_length
                    img_height_px, img_width_px = frame.shape[:2]
                    visible_width_cm = img_width_px * pixel_to_cm_ratio
                    visible_height_cm = img_height_px * pixel_to_cm_ratio
                    center_of_mass_px = np.mean(corners[i][0], axis=0)
                    center_of_mass_cm = center_of_mass_px * pixel_to_cm_ratio

                    # publish the data
                    #self.pub_width.publish(String(data=str(visible_width_cm)))
                    #self.pub_height.publish(String(data=str(visible_height_cm)))
                    #self.pub_center_px.publish(String(data=str(center_of_mass_px)))
                    self.pub_center_cm.publish(Point(x=float(center_of_mass_cm[0]/54), y=float(center_of_mass_cm[1]/36)))
                    #self.pub_center_cm.publish(Point(x=float(-0.1), y=float(-0.1)))

                    #time.sleep(10)
                    #self.get_logger().info("Data published")

        if cv2.waitKey(1) == ord('q'):
            self.cap.release()
            cv2.destroyAllWindows()


def main(args=None):
    rclpy.init(args=args)
    detector = ArucoDetector()
    rclpy.spin(detector)
    detector.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
