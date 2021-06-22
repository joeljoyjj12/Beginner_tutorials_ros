#!/usr/bin/env python

import rospy
from beginner_tutorials.msg import IoT_sensor
def callback(iot_dat):
    rospy.loginfo("Data received %d %s %f %f \n",iot_dat.id,iot_dat.name,iot_dat.Humidity,iot_dat.Temperature)

def IoT_subscriber():

    rospy.init_node('IoT_subscriber', anonymous=True)

    rospy.Subscriber('IoT_sensor_topic', IoT_sensor, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    IoT_subscriber()
