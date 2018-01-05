#!/usr/bin/env python3

import time
import pigpio
import numpy
import math

class MStepper:

  def __init__(self,MicroStep):
    self.CoilA = 23
    self.CoilB = 24
    self.CoilC = 4
    self.CoilD = 17
    self.PwmAC = 18
    self.PwmBD = 22
    self.MicroStep = int(MicroStep)
    self.delay = 0.01
    self.Position = 0
    self.gpioMask = 0
    self.PwmRange    = 1000
    self.Flag = False
    self.BuildMicroStepTable()

  def BuildMicroStepTable(self):
    self.TableSize = int(self.MicroStep * 4)
    self.coilTable = numpy.zeros(self.TableSize, dtype = numpy.uint32)
    self.pwmACTable = numpy.zeros(self.TableSize, dtype = numpy.int16)
    self.pwmBDTable = numpy.zeros(self.TableSize, dtype = numpy.int16)
    #calculate CoilTable for gpio
    HalfSize = int(self.TableSize/2)
    for i in range(HalfSize):
      self.coilTable[i] = 1 << self.CoilA
    for i in range(HalfSize,self.TableSize):
      self.coilTable[i] = 1 << self.CoilC
    for i in range(HalfSize):
      self.coilTable[i+self.MicroStep]= self.coilTable[i+self.MicroStep] | (1 << self.CoilB)
    for i in range(HalfSize, self.TableSize):
      self.coilTable[(i+self.MicroStep) % self.TableSize]= self.coilTable[(i+self.MicroStep) % self.TableSize] | (1 << self.CoilD)
    # calculate PWM
    for i in range(self.TableSize):
      PValue =  math.sqrt(math.fabs(math.sin(math.pi * i / (self.TableSize / 2.0))))
      self.pwmACTable[i]= math.floor(self.PwmRange * PValue)
      self.pwmBDTable[(i + self.MicroStep) % self.TableSize]= self.pwmACTable[i]

  def setGPIO(self):
    #set GPIO OUTPUT
    self.gpioMask = 1<<self.CoilA | 1<<self.CoilB | 1<<self.CoilC | 1<<self.CoilD
    pi.set_mode(self.CoilA,pigpio.OUTPUT)
    pi.set_mode(self.CoilB,pigpio.OUTPUT)
    pi.set_mode(self.CoilC,pigpio.OUTPUT)
    pi.set_mode(self.CoilD,pigpio.OUTPUT)
    pi.set_mode(self.PwmAC,pigpio.OUTPUT)
    pi.set_mode(self.PwmBD,pigpio.OUTPUT)
    #No power on coil
    pi.clear_bank_1(self.gpioMask)

    pi.set_PWM_frequency(self.PwmAC,1000000)
    pi.set_PWM_frequency(self.PwmBD,1000000)
    pi.set_PWM_range(self.PwmAC,self.PwmRange)
    pi.set_PWM_range(self.PwmBD,self.PwmRange)

    self.BuildMicroStepTable()
    self.Flag= True

  def setStepper(self,position):
     if(self.Flag):
       #set gpio
       index = position % self.TableSize
       setmask = self.coilTable[index]
       pi.clear_bank_1(self.gpioMask & ~setmask)
       pi.set_bank_1(setmask)
       #set PWM
       pi.set_PWM_dutycycle(self.PwmAC, self.pwmACTable[index])
       pi.set_PWM_dutycycle(self.PwmBD, self.pwmBDTable[index])
       self.Position= position

  def stop(self):
   pi.clear_bank_1(self.gpioMask)
   #set PWM
   pi.set_PWM_dutycycle(self.PwmAC,0)
   pi.set_PWM_dutycycle(self.PwmBD,0)


  def moveTo(self, Target):
    if Target == self.Position :
      return
    if self.Position < Target:
      direction=1
    else:
      direction=(-1)
    for i in range(self.Position,Target, direction) :
      self.setStepper(i)
      time.sleep(self.delay)

  def move(self, Target):
    Target = Target + self.Position
    self.moveTo(Target)


pi=pigpio.pi()

#create a 5 micro-step stepper
m1 = MStepper(5)

#define your own GPIO pin

m1.CoilA = 17
m1.CoilB = 22
m1.CoilC = 18
m1.CoilD = 25
m1.PwmAC = 23
m1.PwmBD = 24

#set GPIO and calculate GPIO Table
m1.setGPIO()

#Activate coil and set position
m1.setStepper(0)
time.sleep(1.0)


#ok move half turn
m1.move(500)

#ok move to a specific position
#this will move full turn backward
#and move faster
m1.delay=0.001
m1.moveTo(0)

#ok let's do 10 micro-step
m1.MicroStep=10
m1.setGPIO()

#and do half turn

m1.delay=0.01
m1.moveTo(2000)

#de-activate coil
m1.stop()

pi.stop()
