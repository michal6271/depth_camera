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
rozdział View Depth Camera Output in RV

'BEGIN OF CHANGE MADE BY AC-SAWINAL01 ON 27.04.2020
* W modelu kinekta podmieniono model graficzny i pliki konfiguracyjne na intela
* W pliku world zmieniono lokalizacje modelu na folder i plik intela 
* Rviz działa git 
* Michał zamienił osie X i Y i jest git 
* Dodano skrypcik w make.sh który kopiuje do .gazebo nasz nowy model i jest git 
* Nowa paczka depth_camera leci na git i jest git 
* https://github.com/Alber97 oto git i jest git
'END OF CHANGE MADE BY AC-SAWINAL01 ON 27.04.2020
