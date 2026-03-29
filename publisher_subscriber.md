import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32  # float message

class FloatPublisher(Node):
    def __init__(self, start_value=0.0, increment=2.2):
        super().__init__('float_publisher')
        self.publisher_ = self.create_publisher(Float32, 'float_topic', 10)
        self.value = start_value
        self.increment = increment
        self.timer = self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = self.value
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.value += self.increment

def main(args=None):
    rclpy.init(args=args)
    node = FloatPublisher(start_value=5.0, increment=0.1)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

main()


import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class FloatSubscriber(Node):
    def __init__(self, threshold=10.0):
        super().__init__('float_subscriber') 
        self.subscription = self.create_subscription(
            Float32,
            'float_topic',
            self.listener_callback,
            100)
        self.threshold = threshold

    def listener_callback(self, msg):
        if msg.data < self.threshold:
            self.get_logger().info(f'Received value below threshold: {msg.data}')
        else:
            self.get_logger().warn(f'HIGH VALUE {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = FloatSubscriber(threshold=10.0)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


