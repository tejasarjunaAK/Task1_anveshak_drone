import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class Publisher(Node):
   def __init__(self):
     self.num=0.0
     super().__init__("publisher")
     self.pub=self.create_publisher(Float32, "my_topic", 10)
# here arg1: msg_type, arg2: topic_name, arg3: length
     self.timer=self.create_timer(1.0,self.callback)
   def callback(self):
     msg=Float32()
     self.num+=2.2
     msg.data=self.num
     self.get_logger().info("Publishing msg")
     self.pub.publish(msg)
def main(args=None):
  rclpy.init(args=None)
  node=Publisher()
  rclpy.spin(node)
  node.destroy_node()
  rclpy.shutdown()
main()
