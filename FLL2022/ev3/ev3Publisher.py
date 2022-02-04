import paho.mqtt.client as mqtt  

#settings the client 

broker="192.168.1.110" #EV3 IPADRESS
port=1883

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= mqtt.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection

def release_gate(person):
    if person == True:
        client1.publish("topic/release/dt", "open")
        print('opening')
        client1.disconnect()
    else:
        client1.publish("topic/release/dt", 'close')
        print('closing')
        client1.disconnect()
release_gate(True)