#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from custom_msg.msg import cm

rospy.init_node("custom_message_subcriber")
rate = rospy.Rate(10)

def pub_callback(cm):
    rospy.loginfo(" Data diterima: %d", cm.age)

if __name__ == "__main__":
    while not rospy.is_shutdown():
        rospy.Subscriber("custom_message_publisher", cm, pub_callback)
        rate.sleep()
       
