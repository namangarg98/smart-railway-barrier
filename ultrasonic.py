import time
import RPi.GPIO as GPIO
import sys
import urllib2

#from LED_display import display_number
time_t = 5
def getSensorData():
    GPIO.setmode(GPIO.BOARD)

    trig = 38  # sends the signal
    echo = 40  # listens for the signal

    GPIO.setwarnings(False)
    GPIO.setup(echo, GPIO.IN)
    GPIO.setup(trig, GPIO.OUT)



        

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == 0: pass

    start = time.time()  # reached when echo listens

    while GPIO.input(echo) == 1:  pass

    end = time.time() # reached when signal arrived

    distance = ((end - start) * 34300) / 2

    return (int (distance))
def main():
    print 'starting...'
    
    baseURL = 'https://api.thingspeak.com/update?api_key=VO7QBIMGYCL3DEOL'
    count = 0    
    ar = []
    while count < 2:
        try:
            distance = getSensorData()
            if (count == 1):
	       	if (distance  in range(ar[0]-1,ar[0]+2)):
		    f = urllib2.urlopen(baseURL + "&field1=%s" % int(distance))
	            print f.read()
        	    f.close()
	    ar.append(distance)	
            time.sleep(time_t)
        except:
            print 'checking.'
	finally:
	    count = count + 1       
            
# call main
if __name__ == '__main__':
    main() 
