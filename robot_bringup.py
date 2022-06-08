import subprocess as sp

COMMAND = ["ros2", "action", "send_goal", "/head_controller/follow_joint_trajectory", "control_msgs/action/FollowJointTrajectory", "{ trajectory: { joint_names: [head_pan_joint, head_tilt_right_joint, head_tilt_left_joint, head_tilt_vertical_joint], points: [ { positions: [0.5, 0.0, 0.0, 0.0], time_from_start: { sec: 1, nanosec: 0 } }]}}"]

class RobotBringup():
    def __init__(self) -> None:
        self.bring_up()

    def bring_up():
        sp.run(["ros2", "launch", "robot", "robot.launch.py"])
        sp.run(["ros2", "control", "load_start_controller", "joint_state_controller"])
        sp.run(["ros2",  "control", "load_configure_controller", "head_controller"])
        sp.run(["ros2", "control", "switch_controllers", "--start-controllers", "head_controller"])

if __name__ == "__main__":
    RobotBringup()