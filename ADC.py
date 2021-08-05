import machine
import utime

adc_read = machine.ADC(28)

while True:
    reading = adc_read.read_u16()
    print("ADC: ", reading)
    utime.sleep(0.2) 
    