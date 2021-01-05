#!/usr/bin/env python

#tes dua node saling berkirim dan menggunakan mesage yg sama.
# kalau pakai keduanya satu2 di masing2 node biasa.
# ada 2 msg cm dan node2 tappi hanya pakai cm

import rospy
from std_msgs.msg import String
from custom_msg.msg import cm, node2

#inisiasi node dan string publisher dg 10Hz
rospy.init_node("node1")
rate = rospy.Rate(10)
pub = rospy.Publisher("node1", cm, queue_size=1)

def kirim():
    data = cm()
    data.age = 22
    data.name = "Didik"
    data.height = 165.5
    pub.publish(data)

def node1_callback(data):
    rospy.loginfo("kuliah = %s", data.school)



if __name__ == '__main__':
       
    while not rospy.is_shutdown():
        kirim()
        rospy.Subscriber("node2", cm, node1_callback)
        rate.sleep()
