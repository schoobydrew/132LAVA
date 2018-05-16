# 132LAVA
CSC 132 Project
#.ino file is for arduino, to upload to board you should use the Arduino IDE and a usb cable to interface
Serial transfer from arduino to pi is done via usb and serial print

to find the path for usb port that the arduino will be connected to
1: open terminal
2: ls /dev/tty*
3: plug in arduino
4: ls /dev/tty*
5. the new one should have appeared and that should be the arduino it should look something like this "/dev/ttyACM0"
