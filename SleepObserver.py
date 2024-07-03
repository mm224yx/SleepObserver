import network
import time
import pyRTOS
import machine
from machine import Pin
from umqtt.simple import MQTTClient
import gc
 
SEND_DATA=1000
wifi_status = False
mqtt_server = 'broker.hivemq.com'
client_id = 'clientId-ZgTa1dVUwb'
 
def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print("Connected to", mqtt_server)
    return client

def reconnect():
    print("Failed to connect to MQTT")
    time.sleep(3)
    machine.reset()
    
def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("Morse_Code_RPI", "Getyourownwifi") #Change depending on available internet!
    time.sleep(3)
    return wlan.isconnected()

def sound_sensor(self):
    s_s = Pin(16, Pin.IN, Pin.PULL_DOWN)
    yield
    
    while True:
        if s_s.value() == 0:
            self.send(pyRTOS.Message(SEND_DATA, "sound", "sender"))
            print("sound")
        yield [pyRTOS.timeout(.5)]
        

def vibration_sensor(self):
    v_s = Pin(17, Pin.IN)
    currentState = False
    lastState = False
    yield
    
    while True:
        value = v_s.value()
        if value == 1:
            currentState = True
        else:
            currentState = False
        if currentState != lastState:
            self.send(pyRTOS.Message(SEND_DATA, "vibration", "sender"))
            print("movement")
            lastState = currentState
        yield [pyRTOS.timeout(1)]
        

def msg_handler(self):
    yield
    sCount = 0
    vCount = 0
    topic = b'Morse_Data'
    sTopic = b'Morse_Sound'
    vTopic = b'Morse_Move'#Change to change what topic you want it to publish to.
    print("Connecting to wifi...")
    while not wifi_connect():
        print("Reconnecting to wifi...")
        wifi_connect()
    print("Wifi connected")
    try:
        client = mqtt_connect()
    except OSError:
        reconnect()
    yield
    while True:
        msgs = self.recv()
        for msg in msgs:
            if msg.source == "sound":
                sCount += 1
                msgToSend = "Sound instances detected:"
                client.publish(sTopic, b'%s %d' % (msgToSend, sCount))
                client.publish(topic, b'%s %d' % (msgToSend, sCount))
            elif msg.source == "vibration":
                vCount += 1
                msgToSend = "Movement instances detected:"
                client.publish(vTopic, b'%s %d' % (msgToSend, vCount))
                client.publish(topic, b'%s %d' % (msgToSend, vCount))
                
        yield [pyRTOS.wait_for_message(self)]

# Adding tasks to pyRTOS
pyRTOS.add_task(pyRTOS.Task(vibration_sensor, priority=0,name="vibration"))
pyRTOS.add_task(pyRTOS.Task(sound_sensor, priority=2, name="sound"))
pyRTOS.add_task(pyRTOS.Task(msg_handler, priority=1, name="sender", mailbox=True))
pyRTOS.start()

      
