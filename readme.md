Żeby działało to trzeba pobrać model kinecta
http://bitbucket.org/osrf/gazebo_tutorials/raw/default/ros_depth_camera/files/kinect.zip
Rozpakować w
~/.gazebo/models
I zmienić "name" w model.config i model.sdf

Potem pobrać repo, wejść do folderu kinect_ws, i odpalić
./make
potem
. devel/setup.bash

żeby odpalić gazebo z tym światem:
roslaunch kinect_gazebo kinect.launch

odpalanie wizualizacji co widzi kamerka
http://gazebosim.org/tutorials/?tut=ros_depth_camera
rozdział View Depth Camera Output in RViz
