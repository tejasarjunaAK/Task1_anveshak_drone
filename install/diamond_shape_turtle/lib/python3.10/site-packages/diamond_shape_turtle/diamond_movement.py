import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class DiamondMover(Node):
    def __init__(self):
        super().__init__('diamond_mover')
        self.pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)
        self.msg = Twist()
        self.state = 0   
        self.counter = 0
    def control_loop(self):
        self.counter += 1
        if self.state == 0: 
            self.msg.linear.x = 2.0
            self.msg.angular.z = 0.0

            if self.counter >= 20:   
                self.counter = 0
                self.state = 1

        elif self.state == 1:
            self.msg.linear.x = 0.0
            self.msg.angular.z = math.pi / 2  

            if self.counter >= 10:   
                self.counter = 0
                self.state = 0

        self.pub.publish(self.msg)


def main(args=None):
    rclpy.init(args=args)
    node = DiamondMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


