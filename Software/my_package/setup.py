from setuptools import setup

package_name = 'my_package'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/my_world.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/my_robot.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/msg', ['msg/RobotPos.msg']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user.name@mail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_robot_driver = my_package.my_robot_driver:main',
            'robot_controller = my_package.robot_controller:main',
            'obstacle_avoider = my_package.obstacle_avoider:main',  
            'talker = my_package.PC2Pico:main',
            'aruco_detector = my_package.aruco_detector:main',
            'calibrator = my_package.calibrator:main',
        ],
    },
)