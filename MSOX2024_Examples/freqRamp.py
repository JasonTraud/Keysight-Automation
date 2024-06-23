import visa
import time

CURRENT_FREQ = 200000
FREQ_INCREMENT = 10000
ENDING_FREQ = 500000

measFreqCh1=0
rm = visa.ResourceManager()

MSO_X_2024A = rm.open_resource('USB0::0x0957::0x1796::MY52140586::0::INSTR')

# setup
MSO_X_2024A.write(':WGEN:FUNCtion %s' % ('SINusoid'))   # set wavegen to a sine wave
MSO_X_2024A.write(':WGEN:VOLTage %G' % (3.3))           # # with amplitude of 3.3V
MSO_X_2024A.write(':WGEN:VOLTage:OFFSet %G' % (1.8))    # # at an offset of 1.8V
MSO_X_2024A.write(':WGEN:FREQuency %G' % (200000.0))    # # starting at 200kHz

# enable wavegen output
MSO_X_2024A.write(':WGEN:OUTPut %d' % (1))

# ramp through a range of target frequencies and print the results to the prompt
while (CURRENT_FREQ <= ENDING_FREQ):
    time.sleep(0.100)
    temp_values = MSO_X_2024A.query_ascii_values(':MEASure:FREQuency? %s' % ('CHANNEL1'))
    measFreqCh1 = temp_values[0]
    print 'Target:  {0}  Meas:  {1}'.format(str(CURRENT_FREQ), str(measFreqCh1))
    CURRENT_FREQ = CURRENT_FREQ + FREQ_INCREMENT
    MSO_X_2024A.write(':WGEN:FREQuency %G' % (float(CURRENT_FREQ)))

MSO_X_2024A.close()
rm.close()