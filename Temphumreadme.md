## Project G : Building a Remote Sensing System
## Jessica Davis and Kathryn Murie
## Animated Temperature and Humidity graph 
## 09/11/17

## Import 
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
def getTemp():
	with urllib.request.urlopen('http://192.168.1.2/temp') as response:
		Temperature = str(response.read())
		T = (int(Temperature.split()[1]) - 32 )*(5/9)
	return T
def getH():
	with urllib.request.urlopen('http://192.168.1.2/humidity') as response:
		Humidity = str(response.read())
		H = (int(Humidity.split()[1][:-2]))
	return H
	`
	
## Empty arrays of time and measurement values to plot
`
H = [ ]
T = [ ]
`
## Set up the plot object
`
plotFigure = pylab.figure()
`
## The function to call each time the plot is updated
`
def updatePlot( i ):
    H.append( getHum() ) # Store the Humidity
    T.append( getTemp() )           # Store the Temperature
    plotFigure.clear()                       # Clear the old plot
    pylab.plot( H, T )       # Make the new plot
    pylab.xlabel('Humidity (%)')
    pylab.ylabel('Temperature (degree celcius)')
    pylab.title('temperature measurements against Humidity ')
    `
## Make the animated plot 
`
ani = animation.FuncAnimation( plotFigure, updatePlot, interval=500 )
pylab.show()
`

