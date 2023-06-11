import pyvisa as visa
import time
import csv
import datetime

def tic():
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    if 'startTime_for_tictoc' in globals():
        return float(time.time() - startTime_for_tictoc)
    else:
        return float(0.0)

def toc_print():
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds.")
    else:
        print("toc: Start time not set")

counts = 0
sample_limit = 1000

sample_array = []       # Data to be written to CSV
elapsed_array = []
voltage_array = []

# Open connection to instrument
rm = visa.ResourceManager()
v34465A = rm.open_resource('USB0::0x2A8D::0x0101::MY57514375::0::INSTR')

# Collect our data
tic()
print("Start")

while (counts < sample_limit):
    temp_values = v34465A.query_ascii_values(':MEASure:VOLTage:DC? %G,%s' % (1.0, 'MAXimum'))
    voltage_array.append(temp_values[0])
    elapsed_array.append(toc())
    sample_array.append(counts)
    counts = counts + 1

print("Stop")

# Create output file
fileNameString = datetime.datetime.now().strftime("%y%m%d%H%M") + "_data.csv"
f = open(fileNameString, "w", newline='', encoding='utf-8')
c = csv.writer(f)
header = ['Sample', 'Elapsed Time', 'Delta Time', 'Voltage']
c.writerow(header)

data_counter = 0
for x in sample_array:
    if data_counter < 1:
        data = [sample_array[data_counter], elapsed_array[data_counter], elapsed_array[data_counter], voltage_array[data_counter]]
    else:
        data = [sample_array[data_counter], elapsed_array[data_counter], elapsed_array[data_counter] - elapsed_array[data_counter-1], voltage_array[data_counter]]
    c.writerow(data)
    data_counter = data_counter + 1
f.close()

# Close connection to instrument
v34465A.close()
rm.close()