# Import
from DAH import DS18B20
import time
# Readout temperature sensor
tmp0 = DS18B20( address="10-00080379b4fb" )
while True:
	
	print(tmp0.getCelsius())
	time.sleep(0.5)
