import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class Subscriber(Node):
  def __init__(self):
    super().__init__("subscriber")
    self.subscribe= self.create_subscription(Float32, "my_topic",self.callback,10)
  def callback(self,msg):
    if (msg.data <80):
     self.get_logger().info(f"msg received {msg.data}")
    else: 
     self.get_logger().warn(f"flying at high high altitude : {msg.data}") 
def main(args=None):
    rclpy.init(args=None)
    node=Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
main()
   
