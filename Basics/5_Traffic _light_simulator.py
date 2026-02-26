import time

lights = ["Red", "Green", "Yellow"]

def traffic_light(cycles):
    for i in range(cycles):
        for light in lights:
            print(f"Light is: {light}")
            if light == "Red":
                time.sleep(3)
            elif light == "Green":
                time.sleep(3)
            elif light == "Yellow":
                time.sleep(1)

traffic_light(3)