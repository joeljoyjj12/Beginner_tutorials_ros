#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('robot_move_topic', anonymous=True)
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1) 
    timeval=rospy.get_time()

    twist=Twist()
    twist.linear.x=1.1

    while not rospy.is_shutdown():
        #timeval2=rospy.get_time()
        #if timeval2-timeval>=0.9:
        #    timeval=timeval2
        #    twist.linear.x=twist.linear.x * -1
        twist.linear.y=1.0
        twist.linear.y=0.0
        twist.linear.z=0.0
        twist.angular.x=0.0
        twist.angular.y=0.0
        twist.angular.z=0.5
        speed_publisher.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
