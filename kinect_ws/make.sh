rm -rf build devel
catkin_make
. devel/setup.bash
cp -r inteld435 ~/.gazebo/models
