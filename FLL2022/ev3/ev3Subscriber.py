import paho.mqtt.client as mqtt
from ev3dev.ev3 import *
import time as tm

m = MediumMotor(OUTPUT_A)

def on_connect(client , userdata, flags, rc):
    print("Connectadoc com o seguinte codigo " +str(rc))
    client.subscribe("topic/release/dt")

def on_message(client, userdata, msg):
    if (msg.payload == 'close'):
      m.stop()
      print('Face is not igual.')
    else: 
      m.duty_cycle_sp = 10 
      tm.sleep(3)
      m.duty_cycle_sp = -10 
      
            
client = mqtt.Client()
client.connect("192.168.1.110",1883,60) #my broker has this ip: 192.168.1.110

client.on_connect = on_connect
client.on_message = on_message

m.run_direct()
m.duty_cycle_sp=0

client.loop_forever()