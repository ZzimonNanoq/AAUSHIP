#!/usr/bin/env python
import rospy
import time
import geometry_msgs.msg
from aauship_control.msg import *
import tf


rospy.init_node('range_proportional_control') #initialise so we can publish and subscribe

listener = tf.TransformListener() #create a listener, not a subcriber 
pub = rospy.Publisher('lli_input', LLIinput, queue_size=1000) #LLI publisher for the thrust values

pub_msg = LLIinput() #initialize the message container
pub_msg.DevID = int(10)
pub_msg.MsgID = int(5)

time.sleep(1) #sleep to let transforms arrive before we start polling them

while (1):
	time.sleep(0.1)
	(trans,rot) = listener.lookupTransform('/usb_cam', '/map', rospy.Time(0)) #get the transform between map and usb_cam
	pub_msg.Data = int(trans[2]*60)
	tf.transformations.euler_from_quaternion(rot)
	pub.publish(pub_msg)



def test():
	(trans,rot) = listener.lookupTransform('/usb_cam', '/map', rospy.Time(0)) #get the transform between map and usb_cam
	print("trans", trans)
	print("rot",  tf.transformations.euler_from_quaternion(rot))
