"""Class to control motion in L293DNE
by Auro Varat Patnaik & Luisa Schrempf
Version 11/11/21
"""
import RPi.GPIO as io
io.setmode(io.BCM)
import time
# Constants should go here
G0 = 6.67384E-11            # From CODATA 2010
ASTRO_U = 149597870700.0    # From IAU resolution 2012/08 B2
YEAR = float(3.15576e7)     # Julian year = 365.25 days


class motorControl(object):

    def __init__(self, label, in1, in2, en, power,state):
        """
        Initialises a particle in 3D space

        :param label: String w/ the name of the particle
        :param mass: float, mass of the particle
        :param position: [3] float array w/ position
        :param velocity: [3] float array w/ velocity
        """

        io.setmode(io.BCM)

        self.label = str(label)
        self.in1 = in1
        self.in2 = in2
        self.en = en
        self.state = state
        io.setup(in1, io.OUT)
        io.setup(in2, io.OUT)
        io.setup(en, io.OUT)
        self.power = io.PWM(en, power)
        self.power.start(0)
        

    @staticmethod
    def new_motor(label,in1,in2,en,power,state,n=1):
        print("ini")
        return motorControl(label,in1,in2,en,power,state)
 


    def __str__(self):
        """
        XYZ-compliant string. The format is
        <label>    <x>  <y>  <z>
        """
         
        return str(self.label)


    def changePower(self,new_power):
        """
        Returns the kinetic energy of a Particle3D instance

        :return ke: float, 1/2 m v**2
        """
        self.power.ChangeDutyCycle(new_power)
        
        return "Power changed for {} to {}".format(self.label,new_power)
        


    def clockwise(self):
        """
        Returns the linear momentum of a Particle3D instance
        :return p: (3) float np.array, m*v
        """
        self.power.ChangeDutyCycle(70)
        io.output(self.in1, True)    
        io.output(self.in2, False)
        self.state = True
        print("{} moving in clockwise".format(self.label))
       


    def counter_clockwise(self):
        """
        Returns the linear momentum of a Particle3D instance
        :return p: (3) float np.array, m*v
        """
        self.power.ChangeDutyCycle(70)
        io.output(self.in1, False)    
        io.output(self.in2, True)
        self.state = False
        return "{} moving in counter-clockwise".format(self.label)
        
      

    @staticmethod
    def forward(motor_list):
        """
        2nd order position update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """

        for motor in motor_list:
            motor.counter_clockwise()
            
            
        return "Forward"
    @staticmethod
    def backward(motor_list):
        """
        2nd order position update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """

        for motor in motor_list:
            motor.clockwise()
            
        return "Moving Backward"
    
    @staticmethod
    def turn_left(motor_list,start_time,degtime):
        """
        2nd order position update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """

        end_time = start_time + degtime
        motorControl.counter_clockwise(motor_list[0])
        motorControl.clockwise(motor_list[1])
        
        if time.time() == end_time:
            return False
        else:
            return True
        
    @staticmethod
    def turn_right(motor_list,start_time,degtime):
        """
        2nd order position update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """

        end_time = start_time + 0.7
        motor_list[1].counter_clockwise()
        motor_list[0].clockwise()
        
        if time.time() == end_time:
            return False
        else:
            return True
            
    
    @staticmethod
    def start_turn(motor_list,pin,start):
        """
        2nd order position update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """
        
        while 0 == io.input(pin):
        
                motorControl.counter_clockwise(motor_list[1])
                motorControl.clockwise(motor_list[0])
                
        i = True
        while i:
                i = motorControl.turn_right(motor_list,start,0.5)
        
        return False
        
    @staticmethod
    def check_and_run(motor_list,start_time,pin,degtime):
        """
        2nd order position update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """

        
        while 0 == io.input(pin):
                motorControl.start_turn(motor_list,start_time,pin)
        

    def stop(self):
        """
        Velocity update

        :param dt: timestep
        :param force: [3] float array, the total force acting on the particle
        """
        io.output(self.en, False)
        self.power.stop()
        io.cleanup()
        
        print( "Stopped {}".format(self.label))
        
     
        
     
