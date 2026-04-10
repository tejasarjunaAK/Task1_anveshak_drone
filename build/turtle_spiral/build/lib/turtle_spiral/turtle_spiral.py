import rclpy
from rclpy.node import  Node
from geometry_msgs.msg import Twist
import math

class Spiralling(Node):
 def __init__(self):
  super().__init__('spiral_turtle')
  self.theta=0.0
  self.x=2.0
  self.z=0.0
  self.k=0.5
  self.r =2.0
  self.r0=2.0
  self.dt=0.1
  self.pub= self.create_publisher(Twist,"/turtle1/cmd_vel",10)
  self.create_timer(self.dt,self.callback_fn)
 def callback_fn(self):
  msg=Twist()
  self.r=self.r0 +self.k *self.theta
  self.z=self.x/(math.sqrt(self.r**2+self.k**2))
  msg.linear.x=self.x
  msg.angular.z=self.z
  self.pub.publish(msg)
  self.theta+=self.z*self.dt
def main(args=None):
 rclpy.init(args=args)
 node=Spiralling()
 rclpy.spin(node)
 node.destroy_node()
 rclpy.shutdown()
main()  
