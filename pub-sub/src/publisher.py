#!/usr/bin/env python

import rospy
from std_msgs.msg import String

#inisiasi node dan string publisher dg 20Hz
rospy.init_node("publisher_node")
rate = rospy.Rate(20)
pub = rospy.Publisher("publisher", String, queue_size=1)

def kirim():
    string_msg = "kirim data berhasil"
    pub.publish(string_msg)


if __name__ == '__main__':
       
    while not rospy.is_shutdown():
        kirim()
        rate.sleep()