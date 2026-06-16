from gpiozero import LEDBoard, DigitalInputDevice
from time import sleep

# 1. Setup the LEDs to blink independently (GPIO 23, 24, 25)
leds = LEDBoard(23, 24, 25)
leds.blink(on_time=0.5, off_time=0.5, background=True)

# 2. Setup the 4 PNP IR Sensors (GPIO 7, 11, 13, 15)
# pull_up=False is essential for PNP (Active High) sensors
sensors = {
    "Sensor 1 (Pin 4)": DigitalInputDevice(4, pull_up=False),
    "Sensor 2 (Pin 17)": DigitalInputDevice(17, pull_up=False),
    "Sensor 3 (Pin 27)": DigitalInputDevice(27, pull_up=False),
    "Sensor 4 (Pin 22)": DigitalInputDevice(22, pull_up=False)
}

print("LEDs are blinking in the background.")
print("Monitoring 4 PNP IR Sensors... Press Ctrl+C to exit.")
print("-" * 50)

try:
    while True:
        results = []
        for name, sensor in sensors.items():
            # Check if sensor is sending a HIGH signal
            status = "DETECTED" if sensor.is_active else "Clear"
            results.append(f"{name}: {status}")
        
        # Join the results and print on a single line that updates
        print("\r" + " | ".join(results), end="", flush=True)
        
        sleep(0.1)

except KeyboardInterrupt:
    leds.off()
    print("\n\nProgram stopped. LEDs turned off.")