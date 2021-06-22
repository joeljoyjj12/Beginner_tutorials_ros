#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import math

def move():
    rospy.init_node('robo_spiral', anonymous=True)
    speed_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1000)
    rate = rospy.Rate(180) 
    timeval=rospy.get_time()

    twist=Twist()

    period=2*math.pi/2
    twist.linear.x=5
    twist.linear.y=0.0
    twist.linear.z=0.0
    twist.angular.x=0.0
    twist.angular.y=0.0
    twist.angular.z=2

    while not rospy.is_shutdown():
        timeval2=rospy.get_time()
        if timeval2-timeval>=period/2:
            timeval=timeval2
            twist.linear.x=twist.linear.x-0.4
        speed_publisher.publish(twist)
        rate.sleep()

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
