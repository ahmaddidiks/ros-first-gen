#!/usr/bin/env python

#tes dua node saling berkirim dan menggunakan mesage yg sama.
# kalau pakai keduanya satu2 di masing2 node biasa
# ada 2 msg cm dan node2 tappi hanya pakai cm

import rospy
from std_msgs.msg import String
from custom_msg.msg import cm, node2

rospy.init_node("node2")
rate = rospy.Rate(10)
pub = rospy.Publisher("node2", cm, queue_size=1)



def kirim():
    data = cm()
    data.school = "robotics"
    pub.publish(data)
    
def data_callback(data):
    rospy.loginfo(" Nama: %s , umur = %d , tinggi = %f", data.name, data.age, data.height)

if __name__ == "__main__":

    while not rospy.is_shutdown():
        rospy.Subscriber("node1", cm, data_callback)
        kirim()
        rate.sleep()
       
