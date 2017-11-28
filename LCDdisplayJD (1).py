
#import
import time
import Adafruit_CharLCD as LCD
import urllib.request
import pylab
import matplotlib.animation as animation
import datetime
import math
import numpy
# Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()
t = 1 #define sleeptime for all messages

#define function to program the LCD display when given 5 arguments; the colour (c1,c2,c3), the text to be displayed (message) and the sleeptime
def display(c1,c2,c3, message, sleeptime):
        lcd.set_color(c1,c2,c3)
        lcd.clear()
        width = 16
        lcd.message(message[:width]+'\n'+message[width:])
        time.sleep(sleeptime)
def displaydata(c1,c2,c3, message, sleeptime):
        lcd.set_color(c1,c2,c3)
        lcd.clear()
        lcd.message(message)
        time.sleep(sleeptime)
#defining function that returns the temperature in degrees celsius
def getT():
	with urllib.request.urlopen('http://192.168.1.2/temp') as response:
		Temperature = str(response.read())
		T = (int(Temperature.split()[1]) - 32 )*(5/9)
	return T
#defining function that returns the humidity
def getH():
	with urllib.request.urlopen('http://192.168.1.2/humidity') as response:
		Humidity = str(response.read())
		H = (int(Humidity.split()[1][:-2]))
	return H

#defining function that returns the outside temperature in degrees celsius
def getoutT():
	with urllib.request.urlopen('http://192.168.1.3/temp') as response:
		Temperature = str(response.read())
		outT = Temperature.split()[1]
	return outT
#defining function that returns the outside humidity
def getoutH():
	with urllib.request.urlopen('http://192.168.1.3/humidity') as response:
		Humidity = str(response.read())
		outH = Humidity.split()[1][:-2]
	return outH 
      
#welcome start up
#initial message changes relative to the time of day
time_of_day = time.time() 
if time_of_day < 1200000000 :
        display(0.0, 1.0, 0.0 , 'Good morning',t)
if time_of_day > 1700000000 :
        display(0.0, 1.0, 0.0 , 'Good evening',t)
else :
        display(0.0, 1.0, 0.0 , 'Good afternoon',t)

display(0.0, 1.0, 0.0 , 'Welcome to work!',t)
display(0.0, 1.0, 0.0 , 'The date is...',t)
display(0.0, 1.0, 0.0 , time.strftime("%d/%m/%Y"),t)
display(0.0, 1.0, 0.0 , 'The time is...',t)
display(0.0, 1.0, 0.0 , time.strftime("%H:%M"),t)

display(0.0, 1.0, 0.0 , 'Please refer to the console',t)
ctime = input('How often would you like to check the conditions today? Please enter your answer in minutes: ')
checktime = float(ctime*60) #interval time between checking the humidity and temperature

#user has the option to input their own temperature and humidity or go with our recommendation
temp_ans = input('We recommend 25 degrees as the ideal temperature, would you like to change this? (yes/no)') 
if temp_ans == 'yes':
        ideal_temp = int(input('What would you like to set the temperature to?'))
else:
        ideal_temp = 25 #(degree celcius)
hum_ans = input('We recomend a humidity of 50%, would you like to change this? (yes/no)') 
if hum_ans == 'yes':
        ideal_hum = int(input('What would you like to set the humidity to?'))
else:
        ideal_hum = 50 #(%)
#compare data inside to ideal variables set.
timetemp = []
timeHum = []
i = 0
while i<50 :
        #check temperature and humidity from inside and outside sensor
        t1temp = time.time()
        T = getT()
        t2temp = time.time()
        timetemp.append(t2temp-t1temp)
        t1Hum = time.time()
        H = getH()
        t2Hum = time.time()
        timeHum.append(t2Hum-t1Hum)
        
        dispTin = str(T)[0]+str(T)[1]+str(T)[2]+str(T)[3]
        outT = getoutT()
        outH = getoutH()
        if T > ideal_temp:
                display(1.0, 0.0, 0.0 , 'The temperature is currently...',t)
                displaydata(1.0, 0.0, 0.0 , '{dispTin} degrees'.format(dispTin = dispTin),t)
                display(1.0, 0.0, 0.0 , 'It is too warm',t)
        elif T == ideal_temp :
                display(0.0, 1.0, 0.0 , 'The temperature is currently...',t)
                displaydata(0.0, 1.0, 0.0 , '{dispTin} degrees'.format(dispTin = dispTin),t)
                display(0.0, 1.0, 0.0 ,'The temperature is ideal',t)
        else :
                display(0.0, 0.0, 1.0 ,'The temperature is currently...',t)
                displaydata(0.0, 0.0, 1.0 ,'{dispTin} degrees'.format(dispTin = dispTin),t)
                display(0.0, 0.0, 1.0 ,'It is too cold',t)
        
        if H > ideal_hum:
                display(1.0, 0.0, 0.0 , 'The humidity is currently...',t)
                displaydata(1.0, 0.0, 0.0 , '{Humid} %'.format(Humid=str(H)),t)
                display(1.0, 0.0, 0.0 , 'The humidity is too high',t)
        elif H == ideal_hum :
                display(0.0, 1.0, 0.0 , 'The humidity is currently...',t)
                displaydata(0.0, 1.0, 0.0 , '{Humid} %'.format(Humid=str(H)),t)
                display(0.0, 1.0, 0.0 ,'The humidity is ideal',t)
        else :
                display(0.0, 0.0, 1.0 ,'The humidity is currently...',t)
                displaydata(0.0, 0.0, 1.0 ,'{Humid} %'.format(Humid=str(H)),t)
                display(0.0, 0.0, 1.0 ,'The humidity is too low',t)
        display(0.0, 1.0, 0.0 , 'Please refer to the console',t)
        outside_ans = input('Would you like to know the conditions outside? (yes/no)')
        if outside_ans == 'yes':
                display(1.0, 0.0, 0.0 , 'The temperature outside is...',t)
                displaydata(1.0, 0.0, 0.0 , '{out} degrees'.format(out = str(outT)),t)
                display(1.0, 0.0, 0.0 , 'The humidity outside is...',t)
                displaydata(1.0, 0.0, 0.0 , '{outhum} %'.format(outhum = str(outH)),t)
                #calculate dew point temp and see if is raining outside. In report write about to go further could add light sensor and tell them how dark it is outside
                Td = float(outT) - ((100-float(outH))/5)        
                display(1.0, 0.0, 0.0 , 'The dew point is currently:',t)
                dispTd = str(Td)[0]+str(Td)[1]+str(Td)[2]+str(Td)[3]
                displaydata(1.0, 0.0, 0.0 , '{dispTd} degrees'.format(dispTd=str(dispTd)),t)
                if float(outT) > (Td+1):
                        display(0.0, 1.0, 0.0 , 'Rain is unlikely',t)
                     
                #Since the relative humidity cannot exceed 100%, the dew point can never be higher than the temperature.
                elif float(outT)< (Td):
                        display(1.0, 0.0, 0.0 , 'ERROR: check sensor',t)
                else: 
                        display(0.0, 0.0, 1.0 , 'We suggest you take an umbrella today',t)
                display(0.0,0.1,0.0, 'check back in {ctime} minute(s)'.format(ctime=ctime),t)                  
        else:
                display(0.0,1.0,0.0,'okay, check back in {ctime} minute(s)'.format(ctime=ctime),t)
        
        print(i)
        i+=1
        time.sleep(1)
print(timetemp)
print(timeHum)
avg_timetemp = sum(timetemp)/len(timetemp)    
SEtimetemp = numpy.std(timetemp)/(len(timetemp))**0.5
avg_timeHum = sum(timeHum)/len(timeHum)
SEtimeHum = numpy.std(timeHum)/(len(timeHum))**0.5

print('average time taken to recieve temperature=' ,avg_timetemp, 'with uncertainty=',SEtimetemp)
print('average time taken to recieve humidity = ' ,avg_timeHum,'with uncertainty=',SEtimeHum)

