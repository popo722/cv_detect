# cv_detect

# RaspBerryPi3 python3 Setup手順
$ sudo apt install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev  
$ sudo apt install python3-pip  
  
$ sudo apt-get install python3-numpy  
$ sudo apt-get install python3-imaging  
$ sudo apt-get install python3-pandas  
$ sudo apt-get install python3-matplotlib  
  
$ wget https://github.com/mt08xx/files/raw/master/opencv-rpi/libopencv3_3.4.0-20180115.1_armhf.deb  
$ sudo apt install -y ./libopencv3_3.4.0-20180115.1_armhf.deb  
$ sudo ldconfig  
  
# ラズパイカメラをマウント
$ sudo modprobe bcm2835-v4l2   
$ ls /dev/video*  
/dev/video0  
  
# 実行
$ python3 personal_detect.py  
Escキーで終了  
