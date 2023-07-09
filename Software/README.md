# MiniMiniRobots Software

Software is divided into two sub-parts. First part should be flashed into the Raspberry Pi Pico which is connected to the PCB. Second part is a ROS2 package named **my_package** which is used for controlling the Robot via a Socket node and AR application with a Webots Simulation. 

Detailed information about the python files for the programs and nodes in this project can be found in the `README.md` files under their respective folders for users want to make change and use in their own projects. 

If you want to simply build and run the package inside your computer, you can put the folder named `my_package`  under a ros2 workspace and build it with `colcon build` command. After that, source the setup file in the install folder under the workspace. For instance, if you are using bash (default by ubuntu), you can use the following command while you are inside the workspace folder in the terminal:

```
source install/setup.bash  
``` 

After sourcing is done, you can launch the program by writing this command on the terminal:

```
ros2 launch my_package robot_launch.py 
``` 
If you want to launch the package with 2 robots, you can use this command:

```
ros2 launch my_package robot_launch.py robot_number:=2 
``` 
