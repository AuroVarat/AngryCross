"""
Main script instantiating and running a controller class for robot K
By Auro Varat Patnaik & Luisa Schrempf
Version 25/11/21
"""

from robot import Robot

# Instantiate robot
k = Robot(2, 23, 24, 18, 27, 22, 17, label="KD6-3.7")

# Run main control algorithm for 10 seconds
k.run(10)
