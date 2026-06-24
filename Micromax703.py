import board    
import digitalio
import time


# Initialize the in built for prototyping LED pin
led = digitalio.DigitalInOut(board.LED) # Initialize the LED pin
led.direction = digitalio.Direction.OUTPUT

Switch = digitalio.DigitalInOut(board.D5) # Initialize the switch pin
Switch.direction = digitalio.Direction.INPUT
Switch.pull = digitalio.Pull.UP

while True:
    if not Switch.value: # If the switch is pressed (LOW)
        led.value = True  # Turn on the LED
    else:
        led.value = False # Turn off the LED
    
    time.sleep(0.01) # Small delay to debounce the switch
