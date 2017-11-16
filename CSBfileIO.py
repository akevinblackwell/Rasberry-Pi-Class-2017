from time import strftime, sleep, gmtime
import time
import random

try:
    temperature_file = open("tempfile.txt","w")
except:
    print("Error - file can't be opened.")
    quit()

temperature = 0.0

for x in range(0,20):
    temperature = random.randint(70,90)
    temp_string = str(temperature)
    time.sleep(1)
    temperature_file.write(strftime(" %m %d %y %H:%M:%S", gmtime())+"GMT "+temp_string+"\n")

temperature_file.close()




try:
    temperature2_file = open("tempfile.txt","r")
except:
    print("Error - file can't be opened.")
    quit()

temperaturesum = 0
linecount = 0
while EOFError:
    linecount = linecount + 1
    line = temperature2_file.readline()
    log_string = line.split()
    temperature_string = log_string[4]
    temperature_numeric = round(float(temperature_string))
    print(temperature_string, temperature_numeric+1)
    temperaturesum = temperaturesum+temperature_numeric
averagetemperature = temperaturesum/linecount
print(averagetemperature)

temperature2_file.close()
