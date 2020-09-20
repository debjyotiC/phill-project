import RPi.GPIO as GPIO

GPIO.setwarnings(False)

class MotorControl:
  m1_0 = 0
  m1_1 = 0
  m2_0 = 0
  m2_1 = 0
  def __init__(self, m1_0, m1_1, m2_0, m2_1):
    self.m1_0 = m1_0
    self.m1_1 = m1_1
    self.m2_0 = m2_0
    self.m2_1 = m2_1

  def setGPIO(self, mode):
    if(mode == 'OUTPUT')
      GPIO.setup()
