import RPi.GPIO as GPIO # type: ignore
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
pwm = GPIO.PWM(14,100)

print("\nPress Ctrl+C to quit \n")
pwm.start(0)

try:
    while True:
        temp = subprocess.getoutput("vcgencmd measure_temp|sed 's/[^0-9.]//g'")
        
        if round(float(temp)) >= 70:
            print("CPU temperature is over 70°C --> Fan speed: 100%")
            pwm.ChangeDutyCycle(100)
        elif round(float(temp)) >= 65:
            print("CPU temperature is over 65°C --> Fan speed: 80%")
            pwm.ChangeDutyCycle(80)
        elif round(float(temp)) >= 60:
            print("CPU temperature is over 60°C --> Fan speed: 25%")
            pwm.ChangeDutyCycle(25)
        else:
            print("CPU temperature is lower than 50°C. --> Fan speed: 0%")
            pwm.ChangeDutyCycle(0)
        
        print("Current Temperature: " + temp + "°C")
        time.sleep(20)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
    print("Ctrl + C pressed -- Ending program")
