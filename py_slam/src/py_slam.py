import time 
import cv2
import numpy as np
import time
import random
import math 
import rospy
import os
from geometry_msgs.msg import Quaternion
import tf


inf = "inf"
angle_min =  0.0
angle_max = 6.28318977355957
angle_increment = 0.017501922324299812
time_increment = 0.0
scan_time = 0.0
range_min =  0.11999999731779099
range_max =  3.5
ranges =  []
scan = []
odom = []
center = [500/2, 500/2] #center =  width/2, height/2 of the base image respecticely 


class robot_pose():
    def __init__(self):
        #pose in quaternion coordinates
        self.position_x = 0.0
        self.position_y = 0.0
        self.orientation_x = 0.0
        self.orientaiton_y = 0.0
        self.orientaition_z = 0.0
        self.orientation_w = 0.0
        #pose in eulierian coordinates
        self.euler_pose = []
    def update_pose():
        pass 
