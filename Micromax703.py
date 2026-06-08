import time 
import board 
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
while True: 
    pass

kbd = Keyboard(usb_hid.devices)
pin_pins = [board.D5, board.D6, board.D9, board.D10, board.D11, board.D12]

buttons = []
for pin in pin_pins:
    button = digitalio.DigitalInOut(pin)
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP
    buttons.append(button)

key_map = [
    (Keycode.GUI, Keycode.R),
    (Keycode.KEYPAD_2),
    (Keycode.KEYPAD_3),
    (Keycode.KEYPAD_4),
    (Keycode.KEYPAD_5),
    (Keycode.KEYPAD_6)
]

last_states = [True] * 6

print("Ready to send keystrokes...")

while True:
    for i in range(6):
        current_state = buttons[i].value
        if not current_state and last_states[i]:  # Button pressed
            kbd.press(key_map[i])
        elif current_state and not last_states[i]:  # Button released
            kbd.release(key_map[i])
        
        last_states[i] = current_state

time.sleep(0.01)  # Debounce delay

