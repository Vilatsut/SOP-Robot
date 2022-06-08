import subprocess

COMMAND = ["ros2", "action", "send_goal", "/head_controller/follow_joint_trajectory control_msgs/action/FollowJointTrajectory", "{ trajectory: { joint_names: [head_pan_joint, head_tilt_right_joint, head_tilt_left_joint, head_tilt_vertical_joint], points: [ { positions: [0.5, 0.0, 0.0, 0.0], time_from_start: { sec: 1, nanosec: 0 } }]}}"]

subprocess.run(COMMAND)
