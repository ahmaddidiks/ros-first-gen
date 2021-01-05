#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from custom_msg.msg import cm, node2

rospy.init_node("node2")
rate = rospy.Rate(10)
pub = rospy.Publisher("node2", node2, queue_size=1)



def kirim():
    data = node2()
    data.school = "undip"
    pub.publish(data.school)
    
def data_callback(data):
    rospy.loginfo(" Nama: %s , umur = %d , tinggi = %f", data.name, data.age, data.height)

if __name__ == "__main__":

    while not rospy.is_shutdown():
        rospy.Subscriber("node1", cm, data_callback)
        kirim()
        rate.sleep()
       
