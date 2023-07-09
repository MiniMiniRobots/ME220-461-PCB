
import json

file_path = '/home/yoy/ros2_ws/src/my_package/worlds/my_world.wbt'  # Replace with the actual path of your file
temp_path = '/home/yoy/ros2_ws/src/my_package/worlds/template.wbt'  # Replace with the actual path of your file
json_path = "/home/yoy/ros2_ws/src/my_package/output.json"

try:
    with open(file_path, 'w') as file:

        with open(temp_path, 'r') as temp:
            file.write(temp.read())


        with open(json_path, 'r') as f:
            data = json.load(f)

        # Parse the data
        visible_width_cm = data["Visible Width (cm)"] / 10
        visible_height_cm = data["Visible Height (cm)"] / 10

        print("Visible Width (cm):", visible_width_cm)
        print("Visible Height (cm):", visible_height_cm)

        formatted_string = "\nRectangleArena {{\n   floorSize {} {}\n}}".format(visible_width_cm, visible_height_cm)
        file.write(formatted_string)

except IOError:
    print("An error occurred while writing to the file.")
