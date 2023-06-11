# Keysight-Automation
Automating tasks with Keysight / Agilent / HP test equipment

## Downloading the Tools
You'll need the Keysight IO Libraries before moving forward. Download them from the link below. 

[Keysight IO Libraries Suite](https://www.keysight.com/en/pd-1985909/io-libraries-suite?nid=-33002.977662&cc=US&lc=eng)

## MSOX2024A Examples
### HelloWorld
As a simple introduction to scripting with an instrument, this walks you through how to retrieve the serial number of an Agilent MSOX-2024 over USB. 

[Click here for a detailed blog post](http://oshgarage.com/keysight-automation-with-python/)

### FreqRamp
Stepping this a bit further, this provides an example of configuring the waveform generator on the scope and ramping it over a range. At each step it will measure the frequency of Channel1.

[Click here for a detailed blog post](http://oshgarage.com/keysight-automation-with-python/)

## 34465A Examples
### singleShot
Example of taking individual samples. Example also exports all data into a CSV file with time stamps for each acquisition to highlight the sampling rate limitations when taking individual measurements.  

### maxSampling
Example of sampling data as quickly as possible on the 34465A and retrieving once complete. This will sample at 5000 samples/second. The base model supports 50,000 readings with the optional memory upgrade supporting 2,000,000 readings. 

### timeBasedSampling
Example of acquiring data on the 34465A based on an internal timer. This example sets the timer 100ms and collects 100 samples.  

### externalTrigger
Example of using the external trigger on the 34465A to capture data into memory and then retrieving it from the device. 