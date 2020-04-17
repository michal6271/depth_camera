import rospy
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField
from roslib import message

def callback_kinect(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.height)
    

def listener():
    rospy.Subscriber("/camera/depth/points", PointCloud2, callback_kinect)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('testnode', anonymous=True)
    listener()