# Example using PWM to dade an LED
import utime
from machine import Pin, PWM

PWM_width = 0

# Constrcut PWM object, with LED on Pin(25)
pwm = PWM(Pin(25))

# Set the PWM frequency
pwm.freq(1000)

while True:
    while PWM_width < 65536:
        PWM_width += 10
        utime.sleep(0.0001)
        pwm.duty_u16(PWM_width)
    
    while PWM_width > 0:
        PWM_width -= 10
        utime.sleep(0.0001)
        pwm.duty_u16(PWM_width)