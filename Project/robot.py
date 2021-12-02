"""
Robot class implementing a basic obstacle avoidance algorithm
by Auro Varat Patnaik & Luisa Schrempf
Version 25/11/21
"""

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

class Robot(object):
    def __init__(self, proximityIn, motorLeftOut1, motorLeftOut2, motorLeftEnable, motorRightOut1, motorRightOut2, motorRightEnable, pwmFreq=1000, label=""):
        """
        Initialise Robot class.
        """

        # Init class variables
        self.isMovingForward = False
        self.isTurningClockwise = False
        self.proximityIn = proximityIn
        self.motorLeftOut1 = motorLeftOut1
        self.motorLeftOut2 = motorLeftOut2
        self.motorLeftEnable = motorLeftEnable
        self.motorRightOut1 = motorRightOut1
        self.motorRightOut2 = motorRightOut2
        self.motorRightEnable = motorRightEnable
        self.stationaryPoints = []
        self.label = str(label)

        # Init GPIO pins
        GPIO.setup(proximityIn, GPIO.IN)
        GPIO.setup(motorLeftOut1, GPIO.OUT)
        GPIO.setup(motorLeftOut2, GPIO.OUT)
        GPIO.setup(motorLeftEnable, GPIO.OUT)
        GPIO.setup(motorRightOut1, GPIO.OUT)
        GPIO.setup(motorRightOut2, GPIO.OUT)
        GPIO.setup(motorRightEnable, GPIO.OUT)

        # Init PWM controllers
        self.motorLeftPWM = GPIO.PWM(motorLeftEnable, pwmFreq)
        self.motorRightPWM = GPIO.PWM(motorRightEnable, pwmFreq)

    def __str__(self):
        return str(self.label)

    def stop(self):
        self.motorLeftPWM.stop()
        self.motorRightPWM.stop()
        GPIO.output(self.motorLeftEnable, GPIO.LOW)
        GPIO.output(self.motorRightEnable, GPIO.LOW)
        self.isMovingForward = False
        self.isTurningClockwise = False
        print("Robot {self.label}: Stopping, recording stationary point")
        time.sleep(0.5) # Wait for half a second for robot to stop completely
        self.stationaryPoints.append(time.time())


    def startTurnClockwise(self):
        print(f"Robot {self.label}: Start clockwise turn")
        self.motorLeftPWM.start(70)
        self.motorRightPWM.start(70)
        GPIO.output(self.motorLeftOut1, True)
        GPIO.output(self.motorLeftOut2, False)
        GPIO.output(self.motorRightOut1, True)
        GPIO.output(self.motorRightOut2, False)
        self.isMovingForward = False
        self.isTurningClockwise = True
        # Wait one second to ensure we rotate sufficiently to clear obstacle before performing proximity check again
        time.sleep(1)

    def startMovingForward(self):
        print(f"Robot {self.label}: Start moving forward")
        self.motorLeftPWM.start(70)
        self.motorRightPWM.start(70)
        GPIO.output(self.motorLeftOut1, True)
        GPIO.output(self.motorLeftOut2, False)
        GPIO.output(self.motorRightOut1, False)
        GPIO.output(self.motorRightOut2, True)
        self.isMovingForward = True
        self.isTurningClockwise = False

    def update(self):
        if (GPIO.input(self.proximityIn) != 0):
            # No obstacle
            if (self.isMovingForward):
                # No obstacle, moving forward
                return
            else:
                if (self.isTurningClockwise):
                    # No obstacle, not moving forward, turning clockwise
                    self.stop()
                    self.startMovingForward()
                    return
                else:
                    # No obstacle, not moving forward, not turning clockwise
                    self.startMovingForward()
                    return
        else:
            # Obstacle
            if (self.isMovingForward):
                # Obstacle, moving forward
                self.stop()
                self.startTurnClockwise()
                return
            else:
                if (self.isTurningClockwise):
                    # Obstacle, not moving forward, turning clockwise
                    return
                else:
                    # Obstacle, not moving forward, not turning clockwise
                    self.startTurnClockwise()
                    return

    def run(self, runTime):
        # Keep running update for runTime seconds
        startTime = time.time()
        while (time.time() - startTime) <= runTime:
            self.update()
