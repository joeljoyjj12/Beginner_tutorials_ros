#!/usr/bin/env python

import rospy
from beginner_tutorials.msg import IoT_sensor

def iot_publish():
    pub = rospy.Publisher('IoT_sensor_topic', IoT_sensor, queue_size=10)
    rospy.init_node('IoT_publisher', anonymous=True)
    rate = rospy.Rate(1) 
    iot_obj=IoT_sensor()
    iot_obj.name="Immobile"
    iot_obj.id=1
    iot_obj.Humidity=23
    iot_obj.Temperature=98
    count=0

    while not rospy.is_shutdown():
        rospy.loginfo("Number:%d || Data : %d %s %f %f \n",count,iot_obj.id,iot_obj.name,iot_obj.Humidity,iot_obj.Temperature)
        pub.publish(iot_obj)
        rate.sleep()
        count=count+1

if __name__ == '__main__':
    try:
        iot_publish()
    except rospy.ROSInterruptException:
        pass
