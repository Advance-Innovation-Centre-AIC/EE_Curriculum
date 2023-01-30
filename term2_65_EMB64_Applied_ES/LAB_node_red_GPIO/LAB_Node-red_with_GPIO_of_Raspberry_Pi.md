# LAB: Node-red with GPIO of Raspberry Pi



# **จุดประสงค์**



# **ติดตั้ง modules**







# **LAB1: …**
## **อุปกรณ์ทดลอง**
## **โปรแกรม**
## **ขั้นตอนการทดลอง**
## **Schematic**
## **code**
## **บันทึกผลการทดลอง**
1. บันทึกภาพการเชื่อมต่อวงจร (Circuit)
2. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม


----------
# **LAB2: …**
## **อุปกรณ์ทดลอง**
## **โปรแกรม**
## **Schematic**
## **code**
## **บันทึกผลการทดลอง**
1. บันทึกขั้นตอนการทดลอง
2. บันทึกภาพการเชื่อมต่อวงจร (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม





----------

https://projects.raspberrypi.org/en/projects/getting-started-with-node-red/6


https://www.hackster.io/pitg2000/remotely-control-gpio-pins-on-the-rpizw-using-only-node-red-9ba318#toc-6--to-allow-remote-access-to-the-gpio-pins-on-the-rpi-5

https://simonprickett.dev/controlling-raspberry-pi-gpio-pins-from-bash-scripts-traffic-lights/




    # Input is a message object with a `payload` property
    # Output is the modified message object
    
    def transform(msg):
        # Modify the payload of the message
        msg.payload = "Hello, " + msg.payload
        return msg



    import RPi.GPIO as GPIO
    
    # Use the BCM numbering scheme for the GPIO pins
    GPIO.setmode(GPIO.BCM)
    
    # Set pin 18 as an output pin
    GPIO.setup(18, GPIO.OUT)
    
    # Input is a message object with a `payload` property
    def transform(msg):
        # Turn the LED on or off based on the value of the payload
        if msg.payload == "ON":
            GPIO.output(18, GPIO.HIGH)
        elif msg.payload == "OFF":
            GPIO.output(18, GPIO.LOW)
            
        # Return the original message
        return msg
    


