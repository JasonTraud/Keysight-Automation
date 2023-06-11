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

rm = visa.ResourceManager()
v34465A = rm.open_resource('USB0::0x2A8D::0x0101::MY57514375::0::INSTR')    # Open Instrument
v34465A.write(':CONFigure:VOLTage:DC %G,%s' % (1.0, 'MAXimum'))             # Configure our voltage measurements
v34465A.write(':SAMPle:COUNt %d' % (1))                                     # On each trigger, collect 1 sample
v34465A.write(':SAMPle:SOURce %s' % ('IMMediate'))                          # Sample immediately on trigger
v34465A.write(':TRIGger:SOURce %s' % ('EXTernal'))                          # Trigger on external source, positive slope
v34465A.write(':TRIGger:SLOPe %s' % ('POSitive'))                           #
v34465A.write(':TRIGger:COUNt %s' % ('INFinity'))                           # Save as many samples as possible
v34465A.write(':FORMat:DATA %s' % ('ASCii'))                                # Data must be formatted for fetch
v34465A.write(':INITiate:IMMediate')                                        # Start acquiring data

# We need to wait for the sampling to be complete before fetching
print("Sampling...")
input("Press ENTER to continue...")
print("Done.")

# Return instrument to an idle state
v34465A.write(':ABORt')

# Retrieve data from memory
temp_values = v34465A.query_ascii_values(':DATA:POINts?')
points = int(temp_values[0])
temp_values = v34465A.query_ascii_values(':DATA:REMove? %d' % (points))

# Create output file
fileNameString = datetime.datetime.now().strftime("%y%m%d%H%M") + "_data.csv"
f = open(fileNameString, "w", newline='', encoding='utf-8')
c = csv.writer(f)
header = ['Sample', 'Voltage']
c.writerow(header)

data_counter = 0
for x in temp_values:
    data = [data_counter, temp_values[data_counter]]
    c.writerow(data)
    data_counter = data_counter + 1
f.close()

# Close connection to instrument
v34465A.close()
rm.close()