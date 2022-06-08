import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from control_msgs.action import FollowJointTrajectory


class RArmActionClient(Node):

    def __init__(self):
        super().__init__('r_arm_action_client')
        self._action_client = ActionClient(self, FollowJointTrajectory, 'r_index_controller')

    def send_goal(self):
        goal_msg = FollowJointTrajectory()
        
        goal_msg.trajectory.joint_names = ["r_index_joint"]
        goal_msg.trajectory.points[0].positions = [1]
        goal_msg.trajectory.points[0].time_from_start.sec = 1
        goal_msg.trajectory.points[0].time_from_start.nanosec = 0
        
        # goal_msg.trajectory = {
        #     joint_names: [r_index_joint],
        #     points: [{ 
        #         positions: [1], time_from_start: { sec: 1, nanosec: 0 } 
        #     }]
        # }


        self._action_client.wait_for_server()

        return self._action_client.send_goal_async(goal_msg)


def main(args=None):
    rclpy.init(args=args)

    action_client = RArmActionClient()

    future = action_client.send_goal()

    rclpy.spin_until_future_complete(action_client, future)


if __name__ == '__main__':
    main()
