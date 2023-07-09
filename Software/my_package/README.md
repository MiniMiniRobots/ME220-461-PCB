## my_package Package

The package is written for ROS2 Foxy (Ubuntu 20.04). It consists of several python scripts, a launch file for calling required nodes with respective order. 

### Launch File

After the build is done, using this launch command on the terminal will launch a webots instance with required scripts in the background. The world consists of an arena with a robot in the middle of it.

If looked into it, the launch file calls a webots world, whose file is `/worlds/my_world.wbt`, a robot instance whose file is `/resources/my_robot.urdf` and 5 nodes with names `my_robot_driver`, `obstacle_avoider`, `robot_controller`, `aruco_detector`, `calibrator`, respectively. All of these nodes are located under `../my_package/`, as the ROS2 structure requires.

### my_robot_driver.py

`my_robot_driver.py` consists of a class named after its file name.

`init()` method creates required variables for interacting with Webots environment. Motors, distance sensors and GPS are initialized here. Then, ros node is created with the same name and required subscriptions and publications for the webots communicated variables are made.   

callback functions are created for using in subscriptions created in `init()` method. 

`step()` method is used for calculating motor velocities and publishing it to Webots environment.

### obstacle_avoider.py

`obstacle_avoider.py` consists of a class named `avoider` with a main function to call it.

`init()` method creates subscriptions for sensors and publications for velocity and turn topics. It also creates a connection to the socket server. 

callback functions are created for using in subscriptions created in `init()` method. 

`calc_pos()` method is the method where the algorithm runs. It firstly creates storing variables, then looks for the sensor readings and change them. The if conditions are consecutive, therefore one of them is adequate for deciding where to go for avoiding the obstacle. 

`timer_callback()` method is used in publishing the final decisions made in `calc_pos()` function to both Webots via ROS and Raspberry Pi Pico via socket.

### robot_controller.py

TODO

### aruco_detector.py

TODO

### calibrator.py

TODO
