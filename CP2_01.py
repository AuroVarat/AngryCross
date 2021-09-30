# Import ADC chip library
from DAH import MCP3208
import time
 
# Define ADC as SPI chip 0 (CE0/GPIO8) 
ADC0 = MCP3208( chip=0 )

# Read all ADC channels in Volts.
#help(ADC0.analogReadAllVolt )

channel = 0
# Play with the following methods
#help(ADC0.analogCount )
#help(ADC0.analogResolution )

#help(ADC0.analogMaximum )
help(ADC0.analogReference )
help(ADC0.analogRead( channel ))

help(ADC0.analogReadFloat( channel ))
help(ADC0.analogReadVolt( channel ))
help(ADC0.analogReadAll )
help(ADC0.analogReadAllFloat )
help(ADC0.analogReadAllVolt)
