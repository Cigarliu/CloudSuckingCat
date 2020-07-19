#coding=utf-8
import RPi.GPIO as GPIO
import time
#角度控制模块

class  angleN:
    frequency=50 #脉冲频率
    
    def __init__(self,channel):
        self.channel=channel
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.channel,GPIO.OUT)
        self.pwm=GPIO.PWM(self.channel,self.frequency)
        self.pwm.start(7.5) #初始角度 90
        time.sleep(0.4)


    def outangle(self,angleXN):
        self.angleXN=angleXN
        self.dutycycle=2.5+self.angleXN*10/180
        self.pwm.ChangeDutyCycle(self.dutycycle)
        time.sleep(0.4)

    def cleanup(self):
        self.pwm.stop()
        time.sleep(0.4)
        GPIO.cleanup()
