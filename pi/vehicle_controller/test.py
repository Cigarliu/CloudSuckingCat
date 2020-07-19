#coding=utf-8
from anglex import angleN
from distance import distance
from run import xiaoche
import RPi.GPIO as GPIO
import time
global dj #舵机
global xc #小车
global dist #超声波测距

dj=angleN(14)
dj=outangle(90)
