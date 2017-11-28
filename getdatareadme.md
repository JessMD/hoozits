


## Project G : Building a Remote Sensing System
## Jessica Davis and Kathryn Murie 
## 09/11/17

## Import packages
` 
import urllib.request
import time
import pylab
import matplotlib.animation as animation
import datetime
 `

## Create files 
`Temp = open('Temperature_data', 'w') 
Hum = open('humidity_data' , 'w')

def getTemp():
	with urllib.request.urlopen('http://192.168.1.2/temp') as response:
		Temperature = str(response.read())
		T = (int(Temperature.split()[1]) - 32 )*(5/9)
	return T
def getHum():
	with urllib.request.urlopen('http://192.168.1.2/humidity') as response:
		Humidity = str(response.read())
	return Humidity`
	
## Empty arrays of time and measurement values to plot
`
t = [ ]
T = [ ]
`
## Set up the plot object
`
plotFigure = pylab.figure() `
## The function to call each time the plot is updated
`
def updatePlot( i ):
    
    t.append( datetime.datetime.now() ) # Store the current time
    T.append( getTemp() )           # Store the measurement
    plotFigure.clear()          # Clear the old plot
    pylab.plot( t, T )       # Make the new plot
    pylab.xlabel('Time of day')
    pylab.ylabel('Temperature (°C)')
    pylab.title('Live Temperature Measurements Over Time')
`
## Make the animated plot
`
ani = animation.FuncAnimation( plotFigure, updatePlot, interval=500 )
pylab.show()`
