import serial
import time
import csv
import os

#create a file of csv to store the values
try:
    os.remove("SensorData.csv")
except OSError:
    pass

#declaring headers of the csv file.
with open('SensorData.csv', mode='a') as sensor_file:
    sensor_writer = csv.writer(sensor_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    sensor_writer.writerow(["X","Y","Z","class"])

#declaring port for serial comminucation and establish connection.
com = "/dev/cu.usbmodem14301"
baud = 9600
x = serial.Serial(com, baud, timeout = 0.1)

# saving data in csv row by row.
while x.isOpen() == True:
    data = str(x.readline().decode('utf-8')).rstrip()
    if data != '':
         print(data)
         sensor_data = []
         readings = data.split(",")
         with open('SensorData.csv', mode='a') as sensor_file:
             sensor_writer = csv.writer(sensor_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
             sensor_writer.writerow([readings[0],readings[1],readings[2],readings[3]])