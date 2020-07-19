#coding=utf-8
import RPi.GPIO as GPIO
import time

class distance():
    
    def __init__(self,Trig_pin,Echo_pin):
        self.trig=Trig_pin
        self.echo=Echo_pin
        self.setup()
    
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig,GPIO.OUT,initial=False)
        GPIO.setup(self.echo,GPIO.IN)
        time.sleep(0.5)    
    def getdist(self):
        GPIO.output(self.trig,GPIO.HIGH)
        time.sleep(0.0002)
        GPIO.output(self.trig,GPIO.LOW)
        while not GPIO.input(self.echo):
            pass
        t1=time.time()
        while GPIO.input(self.echo):
            pass
        t2=time.time()
        t3=t2-t1
       
        if (t3>0.0235):
            return 1
        elif (t3<0.00015):
            return 0
        else:
            return t3*34000/2
        
