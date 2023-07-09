import cv2
import cv2.aruco as aruco
import numpy as np
import math

# Load the predefined dictionary
dictionary = aruco.Dictionary_get(aruco.DICT_4X4_250)

# Load an image
img = cv2.imread("/home/yoy/ros2_ws/src/my_package/my_package/Screenshot from 2023-07-06 14-55-18.png")

# Initialize the detector parameters using default values
parameters = aruco.DetectorParameters_create()

# Detect the markers in the image
marker_corners, marker_ids, _ = aruco.detectMarkers(img, dictionary, parameters=parameters)

def calculate_tilt(corners):
    # Calculate the vector of the top line from left to right
    vec = corners[1] - corners[0]

    # Calculate the angle between this vector and the horizontal axis
    angle = math.atan2(vec[1], vec[0]) * 180 / math.pi

    # If the marker is upright, the angle should be 180 (or 0, depending on your coordinate system)
    # So subtract 180 to get the tilt: zero for upright, negative for left tilt, positive for right tilt
    tilt = angle - 180

    return tilt

file_path = '/home/yoy/ros2_ws/src/my_package/worlds/my_world.wbt'  # Replace with the actual path of your file
temp_path = '/home/yoy/ros2_ws/src/my_package/worlds/template.wbt'  # Replace with the actual path of your file

try:
    with open(file_path, 'w') as file:

        with open(temp_path, 'r') as temp:
            file.write(temp.read())

        width = img.shape[1]/100
        height = img.shape[0]/100
        formatted_string = "\nRectangleArena {{\n   floorSize {} {}\n}}".format(width, height)
        file.write(formatted_string)

        for i in range(len(marker_ids)):
            aruco_id = marker_ids[i][0]
            corners = marker_corners[i][0]
            print(aruco_id, corners)
            
            # Calculate size as the average distance between top corners and bottom corners
            size = np.mean([np.linalg.norm(corners[2] - corners[3]), np.linalg.norm(corners[0] - corners[1])])/100

            # Calculate position as the center of the marker
            x, y = np.mean(corners, axis=0)/100
            
            # Calculate tilt
            tilt = calculate_tilt(corners)


            formatted_string = "\nSolidBox{{\n   physics Physics{{}}\n   name {} \n   size {} {} {}\n   translation {} {} {}\n   rotation 0 0 1 {}\n}}".format(f'"box{aruco_id}"', size, size, size, x - width/2, y - height/2, size/2, tilt)
            #print(formatted_string)

            file.write(formatted_string)
        print("Content appended successfully.")
except IOError:
    print("An error occurred while writing to the file.")

# Draw circles on each corner of the markers
for corners in marker_corners:
    for corner in corners:
        for point in corner:
            cv2.circle(img, tuple(point.astype(int)), 3, (0,255,0), -1)

# Display the result
#cv2.imshow("Result", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()