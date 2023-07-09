## my_package Package

The package is written for ROS2 Foxy (Ubuntu 20.04). It consists of several python scripts, a launch file for calling required nodes with respective order. The continuation of this file has detailed information about the python files in the package.

### Launch File

After the build is done, using this launch command on the terminal will launch a webots instance with required scripts in the background. The world consists of an arena with a robot in the middle of it.

If looked into it, the launch file calls a webots world, whose file is `/worlds/my_world.wbt`, a robot instance whose file is `/resources/my_robot.urdf` and 5 nodes with names `my_robot_driver`, `obstacle_avoider`, `robot_controller`, `aruco_detector`, `calibrator`, respectively. All of these nodes are located under `../my_package/`, as the ROS2 structure requires.

### my_robot_driver.py

`my_robot_driver.py` consists of a class named after its file name. It is used to create the robots and bind them in the Webots Simulation.

`init()` method creates required variables for interacting with Webots environment. Motors, distance sensors and GPS are initialized here. Then, ros node is created with the same name and required subscriptions and publications for the webots communicated variables are made.   

callback functions are created for using in subscriptions created in `init()` method. 

`step()` method is used for calculating motor velocities and publishing it to Webots environment.

### obstacle_avoider.py

`obstacle_avoider.py` consists of a class named `avoider` with a main function to call it. It is used to find and publish required messages to avoid the obstacles.

`init()` method creates subscriptions for sensors and publications for velocity and turn topics. It also creates a connection to the socket server. 

callback functions are created for using in subscriptions created in `init()` method. 

`calc_pos()` method is the method where the algorithm runs. It firstly creates storing variables, then looks for the sensor readings and change them. The if conditions are consecutive, therefore one of them is adequate for deciding where to go for avoiding the obstacle. 

`timer_callback()` method is used in publishing the final decisions made in `calc_pos()` function to both Webots via ROS and Raspberry Pi Pico via socket.

### robot_controller.py

`robot_controller.py` consists of a class named after its file name with a main function to call it. This script is used to create and publish the command messages.

`init()` method creates subscriptions for sensors and publications for velocity and robot_command topics. It also creates a connection to the socket server. 

callback functions are created for using in subscriptions created in `init()` method. 

`command_robot()` method takes the command message created by this node and publishes it.

`control_robot()` method is the method that runs in a infinite loop until the program stops by the user.


### aruco_detector.py

`aruco_detector.py` consists of a class named after its file name with a main function to call it. This node uses opencv2 to detect aruco markers on the arena and publishes their location information.

`init()` method creates subscription for center of mass and creates aruco marker dictionary and parameters. Then, a videocapture device is created to be able to use the connected camera. Finally, timer is created to be able to call the `timer_callback()` method.

`timer_callback()` method is the method where the detection is made. For every frame that captured from the camera, color conversion is made and arudo marker detection function is called. Then, for every marker found, pixel length is calculated and converted into cm with the ratio found from the camera location on the arena. Then, center of mass of the marker is found from the corner locations. Finally, the results are published.

### calibrator.py

`calibrator.py` consists of a class named after its file name with a main function to call it. This script is used to correct the movement of the robot with the results of `aruco_detector` and `obstacle_avoider` nodes.

`init()` method creates storing variables and subscription for the topics poblished from `aruco_detector` and `obstacle_avoider` nodes. It also creates subscription from GPS topics published from `my_robot_driver`.

The callback methods are used for the subscriptions created on `init()` method and used for storing the incoming messages.

`calculate_center_of_mass()` method is used for calculating the Center of Mass of the robot on the Webots Simulation. 

`calculate_distance()` method is used for calculating the distance between the center of mass and the gps information.

`calculate_angle()` method is used for calculating the angle for between the center of mass and the gps information.

`calculate_angle_between_gps()` method is used for calculating the angle between two gps sensors located on the simulated robot.

`compare_robot()` method is the combining method. It compares the results of the previous methods and make corrections. Firstly, it looks for the gps information coming from the Simulation and make the corrections and uses the previously declared methods. Then, It corrects the angle values to its principal values. It logs (or prints) the found values, and creates the storing values for publishing. After that, it makes comparisons with the time difference and gives the necessary translational and rotational speed values to `twist`  Finally, the storing values are published with the predetermined aruco_id. 