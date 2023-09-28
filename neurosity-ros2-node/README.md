# Neurosity Crown Ros2 Node

ROS2 node that uses the Neurosity SDK to move the robot forward and back. Neurosity forward and back topics are converted to /cmd_vel messages.

## Build Instructions
- Install and source ROS2 Humble (other ROS2 distributions will likely build but may take some massaging)
- Install Neurosity (TODO: Neurosity configuration instructions)
- Create your workspace,
```bash
mkdir ros2_ws
mkdir ros2_ws/src
cd ros2_ws/src
```
- Clone the teleop_twist_neurosity package into the `src/` directory
- Return to the `ros2_ws/` directory
- Build the project,
```bash
colcon build
```
- Source the workspace overlay,
```bash
source install/setup.bash
```
- Run the node with,
```bash
ros2 run teleop_twist_neurosity teleop_node
```

# Contributers:

- [Timothy Mead](https://github.com/TTMead)