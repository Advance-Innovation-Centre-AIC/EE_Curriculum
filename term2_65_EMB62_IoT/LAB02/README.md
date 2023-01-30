# **Outline**
- How to use Node-red with MQTT protocol
- How to use Node-red Dashboard  

[doc in dropbox](https://www.dropbox.com/scl/fi/uptu3m0qw9knotibbt13p/LAB-Node-red-with-MQTT-Protocol.paper?dl=0&rlkey=mgbdez1gm79j6svsgjls6td3x)

# LAB: Node-red with MQTT Protocol
# **Objectives**
1. เพื่อศึกษาการใช้งาน MQTT protocol บน Node-red 
2. สามารถเขียนโปรแกรม Node-red อ่านข้อมูลผ่าน MQTT Protocol ได้

# **Hardware**
1. NodeMCU
2. Computer

# **Program Tool**
1. Mosquitto server tool
2. Node-red
3. Arduino IDE 


# **LAB: Using Node-red is Subscribe client** 

ทดลองใช้ Node-red เป็น Subscribe client อ่านข้อความจาก topic  “test” ของ mosquitto_pub ผ่าน 
Mosquitto Broker

## **ขั้นตอนการทดลอง**
1. เปิด Command promp โดย ไปที่ Search >> พิมพ์ cmd
2. เข้าไปในโฟล์เดอร์ mosquitto ตาม path ที่เราติดตั้งโปรแกรม โดยใช้คำสั่ง พิมพ์คำสั่ง cd 
    cd C:\Program Files\mosquitto


3. Run Mosquitto Broker โดยคำสั่ง -v เพื่อแสดงข้อมูลการทำงานของ broker และใช้คำสั่ง -c เพื่อใช้งานการตั้งค่าตาม mosquitto.conf 
    mosquitto -v -c mosquitto.conf


4. เปิดหน้า CMD ขึ้นมาใหม่อีก 1 teb และใช้คำสั่ง เปิด node-red 
    node-red start 


5. ทดลองสร้าง node-red เป็น Subscrilbe โดย ไปที่แถบทางซ้ายมือ >> network >> เลือก mqtt in node


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674121375258_Screenshot+2023-01-19+164133.png)



6. ดับเบิ้ลคลิ๊กที่ mqtt in node และ ตั้งค่าตามภาพด้านล่าง


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674122139304_Screenshot+2023-01-19+165345.png)



7. ไปที่แถบซ้ายมือ >> common >> เลือก debug node


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674122277007_Screenshot+2023-01-19+165723.png)



8. ดับเบิ้ลคลิ๊กที่ debug node และ ตั้งค่าตามภาพด้านล่าง และ คลิ๊ก Done


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674122422163_Screenshot+2023-01-19+165723.png)



9. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกันตามภาพด้านล่าง และ คลิ๊ก Done


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674122600698_image.png)


10. คลิ๊ก Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้
11. เปิดหน้า CMD ขึ้นมาใหม่อีก 1 teb และ ใช้คำสั่ง cd เข้าไปที่ path ของ mosquitto ตามขั้นตอนที่ 2 
12. พิมพ์คำสั่งกำหนดให้ 1 tab ทำหน้าที่เป็น publish โดยส่งข้อความ “Hello !!” ใน topic เท่ากับ “test” 

```
#mosquitto_pub -h [hostname or IP] -t test -m "Hello!!" 
mosquitto_pub -h 192.168.101.245 -t test -m "Hello!!"
```

## **บันทึกผลการทดลอง**


----------
# **แบบฝึดหัด**
1. ทดลองเขียน node-red ตั้งค่า mqtt in node ให้ อ่านข้อความจาก NodeMCU


https://www.dropbox.com/s/7k891342fx3po9i/iot_mqtt_text.ino?dl=0

https://www.dropbox.com/s/gaurvmdqxrz23pg/iot_mqtt.ino?dl=0

----------

[1]Ref: http://www.steves-internet-guide.com/using-arduino-pubsub-mqtt-client/
