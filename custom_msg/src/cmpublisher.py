#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from custom_msg.msg import cm

#inisiasi node dan string publisher dg 10Hz
rospy.init_node("custom_message_publisher_node")
rate = rospy.Rate(10)
pub = rospy.Publisher("custom_message_publisher", cm, queue_size=1)

def kirim():
    #string_msg = "kirim data berhasil"
    #msg = Didik()
    #msg.name = "didik"
    kirim = cm()
    kirim.age = 18
    pub.publish(kirim)


if __name__ == '__main__':
       
    while not rospy.is_shutdown():
        kirim()
        rate.sleep()
