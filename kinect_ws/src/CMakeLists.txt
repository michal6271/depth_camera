cmake_minimum_required(VERSION 2.8.3)
project(kinect_gazebo)

find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

catkin_package()

include_directories(include ${catkin_INCLUDE_DIRS})
