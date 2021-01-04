#!/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node("subcriber")
rate = rospy.Rate(20)

def pub_callback(msg):
    rospy.loginfo(" Data diterima: %s", msg.data)

if __name__ == "__main__":
    while not rospy.is_shutdown():
        rospy.Subscriber("publisher", String, pub_callback)
        rate.sleep()
       