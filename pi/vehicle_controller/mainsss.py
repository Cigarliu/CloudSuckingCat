
#coding=utf-8

import threading
import inspect
import ctypes
from anglex import angleN
from distance import distance
from L298N_RUN import Car
import RPi.GPIO as GPIO
import time

#GPIO.output(07,GPIO.HIGH)
global dj #舵26机
global xc #小车
global dist #超声波测距
global jkAI

def _async_raise(tid, exctype):  #线程终止
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread): #线程终止
    _async_raise(thread.ident, SystemExit)


def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(02,GPIO.IN)
    global dj
    dj=angleN(14)
    global xc
    xc=xiaoche()
    global dist
    dist=distance(20,16)

def checkway():

    if  not GPIO.input(02):
        return 1 #无落差
    else:
        return 0 #有落差

def bignum(left,straight,right):
    dict={}
    if left>straight :
        if left >right:
            dict['left']=left
            return dict
        elif left==right:
            dict['left']=left
            return dict
        else:
            dict['right']=right
            return dict
    elif left==straight:
        if straight>right:
            dict['straight']=straight
            return dict
        elif straight==right:
            dict['straight']=straight
        else:
            dict['right']=right
            return dict
    else:
        if straight>right:
            dict['straight']=straight
            return dict
        elif straight==right:
            dict['straight']=straight
            return dict
        else:
            dict ['right']=right
            return dict 

def AI():
    time.sleep(1)
    global dj
    global xc
    global dist
    
    a90= dist.getdist() #正90方向为初始值  直接获取距离
    if a90==1:
        xc.run(2) #小车速度经测试为56/s  当返回的值为1 代表当前距离大于4m  故前进5秒钟时间为安全事件
        
    elif a90==2:
        xc.back(0.5)
        print 'back'
    else:
        time.sleep(1)
        dj.outangle(0) #舵机指向0度
        time.sleep(1)
        a0=dist.getdist() #取0度方向距离
        if a0==1:
            dj.outangle(90)
            xc.right(0.5)
            time.sleep(0.5)
            xc.run(2)
        else:
            time.sleep(1)
            dj.outangle(180)
            time.sleep(1)
            a180=dist.getdist()
            if a180==1:
                dj.outangle(90)
                xc.left(0.5)
                time.sleep(1)
                xc.run(2)
            else:
                dj.outangle(90)
                distn=bignum(a180,a90,a0)
                for key in distn:
                    distnkey=key
                    print(distnkey)
                    distnvalue=distn[key]
                    print(distnvalue)
                if distnvalue==0 :
                    xc.back(0.2)
                else:
                    t=distnvalue/100
                    command=distnkey
                    if command=='left':
                        xc.left(0.5)
                        time.sleep(0.5)
                        xc.run(t)
                    elif command=='straight':
                        xc.run(t)
                    else:
                        xc.right(0.5)
                        xc.run(t)


def jk():
    while 1:
        if checkway():
            time.sleep(0.2)
            pass
        else:
            xc.back(0.5)
            xc.left(0.5)

init()
jkAI  =threading.Thread(target=jk) #红外落差子线程
jkAI.start
AI()