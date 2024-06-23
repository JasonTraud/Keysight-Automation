import pyvisa
import time

# initialize visa resource
rm = pyvisa.ResourceManager()

# open the resource using the VISA address from Keysight Connection Expert
MSO_X_2024A = rm.open_resource('USB0::0x0957::0x1796::MY52140586::0::INSTR')

# request the instrument to identify itself
modelSerialnumber = MSO_X_2024A.query('*IDN?')
print(str(modelSerialnumber))

# Configure the output
MSO_X_2024A.write(':SAVE:IMAGe:FORMat %s' % ('PNG'))        # Sets to PNG
MSO_X_2024A.write(':SAVE:IMAGe:INKSaver %d' % (0))          # Black background

# Save the output
MSO_X_2024A.write(':SAVE:IMAGe:STARt "%s"' % ('test.png'))

# close
MSO_X_2024A.close()
rm.close()