## Project G : Building a Remote Sensing System
## Jessica Davis and Kathryn Murie 
## Reading and writing temperature and humidity data to a file
## 09/11/17

## import packages 
`
import urllib.request
import time
import pylab
import matplotlib.animation as animation
import datetime
`

## Create files 
`
Temp = open('Temperature_data', 'w') 
Hum = open('humidity_data' , 'w')
`
## While loop allows code to write successive data readings to the file 
`
while True: 
	#Temperature data 
	with urllib.request.urlopen('http://192.168.1.6/temp') as response:
		Temperature = str(response.read())
		T = (int(Temperature.split()[1]) - 32 )*(5/9)
		Temp.write(str(T) + ' oC' + '\n')
	#Humidity data 
	with urllib.request.urlopen('http://192.168.1.6/humidity') as response:
		Humidity = str(response.read())
		Hum.write(Humidity.split()[1] + '\n')
		time.sleep(2) 
		`
