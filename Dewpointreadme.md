## Project G : Building a Remote Sensing System
## Jessica Davis and Kathryn Murie 
## Dew point temperature calculation from humidity reading
`
import urllib.request
import time
import pylab
import datetime
import numpy as np
import time
import pylab
import datetime
import matplotlib.pyplot as plt`


## Defining function that returns the outside humidity
`
def getoutH():
	with urllib.request.urlopen('http://192.168.1.3/humidity') as response:
		Humidity = str(response.read())
		outH = Humidity.split()[1][:-2]
	return outH`
## Check temperature and humidity and then calculate Td for plotting a T-Td graph
`
H = getoutH()

T = np.linspace(-30, 30, 20)
A = float(17.625)
B = float(243.04) #degrees celsius
x = float(H)/100
Td = (B*((np.log(x))+((A*T)/(B+T))))/(A-(np.log(x))-((A*T)/(B+T)))
`
## Uncertainty of Td calculation is 0.4 percent 
`
Tderr=0.004*Td
plt.plot(T, Td, linewidth=0.7, c='red')
`
## Split graph into four quadrants
`
plt.axhline(y=0, linewidth=0.7,color="black")

plt.axvline(x=0,linewidth=0.7, color="black")`
## Plot Graph using matplotlib
# mfc=markerfacecolor, mec=markeredgecolor, ms=markersize and mew=markeredgewidth.
`
plt.title('Dew Point Temperature for Measured Humidity')
plt.axis([-30, 30, -30, 30])
plt.errorbar(T, Td, Tderr, marker='s', mfc='red', mec='black', ms=4, mew=1, capsize= 3, capthick=1,)
plt.xlabel('Air Temperature (°C)')
plt.ylabel(u'Dew Point Temperature (°C)')
plt.grid()
plt.savefig('Td.png') 
plt.show()`
