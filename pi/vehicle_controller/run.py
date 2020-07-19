#coding=utf-8
import RPi.GPIO as GPIO
import time

class xiaoche():
    left_pin1=06
    left_pin2=13

    right_pin1=19
    right_pin2=26

    def __init__(self):
        self.setup()

    
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.left_pin1,GPIO.OUT,initial=False)
        GPIO.setup(self.left_pin2,GPIO.OUT,initial=False)
        GPIO.setup(self.right_pin1,GPIO.OUT,initial=False)
        GPIO.setup(self.right_pin2,GPIO.OUT,initial=False)
        
    def run(self,runtime):
        self.time=runtime
        GPIO.output(self.left_pin1,GPIO.LOW)
        GPIO.output(self.left_pin2,GPIO.HIGH)
        GPIO.output(self.right_pin1,GPIO.HIGH)
        GPIO.output(self.right_pin2,GPIO.LOW)
        time.sleep(self.time)
        self.stop()

    def stop(self):
        GPIO.output(self.left_pin1,GPIO.LOW)
        GPIO.output(self.left_pin2,GPIO.LOW)
        GPIO.output(self.right_pin1,GPIO.LOW)
        GPIO.output(self.right_pin2,GPIO.LOW)
        
    def left(self,runtime):
        self.time=runtime
        GPIO.output(self.left_pin1,GPIO.LOW)
        GPIO.output(self.left_pin2,GPIO.HIGH)
        GPIO.output(self.right_pin1,GPIO.LOW)
        GPIO.output(self.right_pin2,GPIO.LOW)
        time.sleep(self.time)
        self.stop()

    def right(self,runtime):
        self.time=runtime
        GPIO.output(self.left_pin1,GPIO.LOW)
        GPIO.output(self.left_pin2,GPIO.LOW)
        GPIO.output(self.right_pin1,GPIO.HIGH)
        GPIO.output(self.right_pin2,GPIO.LOW)
        time.sleep(self.time)
        self.stop()

    def back(self,runtime):
        self.time=runtime
        GPIO.output(self.left_pin1,GPIO.HIGH)
        GPIO.output(self.left_pin2,GPIO.LOW)
        GPIO.output(self.right_pin1,GPIO.LOW)
        GPIO.output(self.right_pin2,GPIO.HIGH)
        time.sleep(self.time)
        self.stop()


    def cleanup():
        GPIO.cleanup()



