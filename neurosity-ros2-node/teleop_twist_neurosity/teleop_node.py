import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

from neurosity import NeurositySDK
import os
import time


class NeurosityTeleopNode(Node):

    NEUROSITY_EMAIL = 'reubenr202@gmail.com'
    NEUROSITY_PASSWORD = 'neuro123'
    NEUROSITY_DEVICE_ID = 'e88770a76231aac1ca98f41e7c9094cd'
    FORWARD_TOPIC = 'rightArm'
    BACKWARD_TOPIC = 'leftArm'
    MOVE_SPEED = '30'
    CONFIDENCE_THRESHOLD = '0.9'
    SEND_PERIOD = '0.1'

    def __init__(self):
        super().__init__('teleop_node')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        self.timer = self.create_timer(self.SEND_PERIOD, self.callback_timer)

        # Initialise configurations and subscriptions to neurosity API
        self.init_neurosity_link()

        
    def init_neurosity_link(self):
        neurosity = NeurositySDK({
            "device_id": self.NEUROSITY_DEVICE_ID,
        })

        neurosity.login({
            "email": self.NEUROSITY_EMAIL,
            "password": self.NEUROSITY_PASSWORD
        })

        rover = False
        forwardDistance = 2

        self.forward_subscription_ = neurosity.kinesis(self.FORWARD_TOPIC, self.callback_forward)
        self.backward_subscription_ = neurosity.kinesis(self.BACKWARD_TOPIC, self.callback_backkward)

        self.forward_confidence = 0
        self.backward_confidence = 0

    
    def callback_timer(self):
        forward = self.forward_confidence > self.CONFIDENCE_THRESHOLD
        backward = self.backward_confidence > self.CONFIDENCE_THRESHOLD

        # If we are detecting both forward and backward, stop moving
        if forward and backward:
            self.publish_speed(0)
            return
        
        if forward:
            self.publish_speed(self.MOVE_SPEED)
            return

        if backward:
            self.publish_speed(-self.MOVE_SPEED)
            return

        # If neither are detected, stop moving
        self.publish_speed(0)

    def callback_forward(self, data):
        rclpy.loginfo(data['metric'], data['label'], ":", data['confidence'])
        self.forward_confidence = data['confidence']

    def callback_backkward(self, data):
        rclpy.loginfo(data['metric'], data['label'], ":", data['confidence'])
        self.backward_confidence = data['confidence']

    def publish_speed(self, speed):
        cmd_vel_msg = Twist()
        cmd_vel_msg.linear.x = speed
        self.publisher_.publish(cmd_vel_msg)





def main(args=None):
    rclpy.init(args=args)

    neurosity_teleop = NeurosityTeleopNode()

    rclpy.spin(neurosity_teleop)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    neurosity_teleop.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

