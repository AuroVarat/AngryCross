
# Import DAC chip library nd time
from DAH import MCP4922
from DAH import MCP3208
import time




# Define ADC as SPI chip 0 (CE0/GPIO8) 
ADC0 = MCP3208( chip=0 )
#Set MCP3208 Channel
channel = 0 
# Define DAC as SPI chip 1 (CE1/GPIO7)
DAC1 = MCP4922( chip=1 )

# Output range of voltage on channel 0 of DAC1
volt_range = [0.5,1.8,2.0,2.5,2.8,3.0,3.3]
file = open("output.txt","w")
file.write("#ADC Input from LED,DAC Output at LDR\n")
for volt in volt_range:
	DAC1.analogWriteVolt( 0, volt)
	print("Voltage at Channel 0 with Input "+str(volt)+ "V: "+ str(ADC0.analogReadVolt( channel )))
	file.write(str(volt)+","+str(ADC0.analogReadVolt( channel ))+"\n")
	
	time.sleep(0.5)

DAC1.analogWriteVolt( 0, 0.0)
file.close()
