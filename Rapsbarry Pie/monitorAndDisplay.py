import time
import json
#from w1thermsensor import W1ThermSensor


with open('config.json') as f:
  data = json.load(f)

print(data)

#sensor = W1ThermSensor()

while True:
    #temperature = sensor.get_temperature()
    temperature = 20

    if temperature < data['cold_max']:
        #display temperature with blue colour
        print(data['cold_max'])
    elif temperature >= data['comfortable_mix'] or temperature <= data['comfortable_max']:
        #display temperature with green colour.
        print(data['comfortable_max'])
    elif temperature >data['hot_min']:
        #display temperature with red colour
        print(data['hot_min'])

    time.sleep(10)



