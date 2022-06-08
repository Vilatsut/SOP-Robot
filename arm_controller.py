import subprocess as sp
import random


class ArmController():
    def __init__(self):
        self.thumb = ["r_thumb_controller", "r_thumb_joint"]
        self.index = ["r_index_controller", "r_index_joint"]
        self.middle = ["r_middle_controller", "r_middle_joint"]
        self.ring = ["r_ring_controller", "r_ring_joint"]
        self.pinky = ["r_pinky_controller", "r_pinky_joint"]

    def move_command(self, finger, position):
        command = ["ros2", "action", "send_goal", 
        f"/{finger[0]}/follow_joint_trajectory", 
        "control_msgs/action/FollowJointTrajectory", 
        "{ trajectory:", 
        "{",  f"joint_names: [{finger[1]}],", 
        "points: [ {", 
        f"positions: [{position}],", 
        "time_from_start: { sec: 1, nanosec: 0 } }]}}"]
        sp.run(command)

    def move_arm(self, thumb_pos, index_pos, middle_pos, ring_pos, pinky_pos):
        self.move_command(self.thumb, thumb_pos)
        self.move_command(self.index, index_pos)
        self.move_command(self.middle, middle_pos)
        self.move_command(self.ring, ring_pos)
        self.move_command(self.pinky, pinky_pos)

    def play_rps(self):
        num = random.randrange(0, 3)
        if num == 0: self.move_arm(0, 0, 0, 0, 0)
        elif num == 1: self.move_arm(1, 1, 1, 1, 1)
        elif num == 2: self.move_arm(0, 1, 1, 0, 0)



        