# LAB: Node-Red Dashboard with MQTT Protocol


# **Overview LAB 3: Use Node-Red Dashboard control LED of NodeMCU via MQTT**
    
   ทดลองใช้ Node-red Dashboard  เป็น Publish ควบคุม LED บนบอร์ด NodeMCU ผ่าน Mosquitto 
Broker 


![Fig: Node-Red Dashboard controlling LED of NodeMCU via MQTT diagram](https://paper-attachments.dropboxusercontent.com/s_5B2CDC83F09B6CAA259D6A1C2DA4E12C8BBA30AF2DF3C11B70D082BF17634CD2_1675589770699_file.png)


# **ขั้นตอนการทดลอง**


## **Run Mosquiito Broker**

1. เปิด Command promp โดย ไปที่ Search >> พิมพ์ cmd
2. เข้าไปในโฟล์เดอร์ mosquitto ตาม path ที่เราติดตั้งโปรแกรม โดยใช้คำสั่ง พิมพ์คำสั่ง cd 
 
```
   cd C:\Program Files\mosquitto
```

3. Run Mosquitto Broker โดยคำสั่ง -v เพื่อแสดงข้อมูลการทำงานของ broker และใช้คำสั่ง -c เพื่อใช้งานการตั้งค่าตาม mosquitto.conf 


```
    mosquitto -v -c mosquitto.conf
```



บันทึกผล: ภาพการรัน Mosquiito Broker

----------

                                                              *ภาพผลการรัน Mosquiito Broker*



----------

## **Use NodeMCU with MQTT**

1. เปิด Arduino IDE 
2. ทำการติดตั้ง libraly สำหรับใช้งาน ESP8266 ตาม >>[How to Install the ESP8266 Board in Arduino IDE](https://randomnerdtutorials.com/how-to-install-esp8266-board-arduino-ide/))
3. ติดตั้ง PubSubClient Library สำหรับใช้งาน MQTT ไปที่แถบ Sketch>>Include Library>>Manage Libraries…>>พิมพ์ “PubSubClient” >> install


![fig : PubSubClient library](https://paper-attachments.dropboxusercontent.com/s_5B2CDC83F09B6CAA259D6A1C2DA4E12C8BBA30AF2DF3C11B70D082BF17634CD2_1675593267756_Untitled.png)

4. ทดลองสร้างโปรแกรม ไปที่ file >>new >>ใส่ code >>แก้ไขชื่อ ssid และ ip และ password เป็นของตัวเองแล้วทดลอง upload โปรแกรมลงบอร์ด

Downloaf Arduino Code >>[mqtt_node_red_concrol_LED](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/tree/main/term2_65_EMB62_IoT/LAB02/arduino%20code)


บันทึกผล: ภาพผลการรัน code หน้า seriall monitor

----------



                                                              *ภาพผลการรัน* *code  หน้า seriall monitor*



----------


## **Use Switch node on  Node-red Dashboad** 
1. เปิดหน้า CMD ขึ้นมาใหม่อีก 1 teb และใช้คำสั่ง เปิด node-red 
 
 
```    
    node-red start 
```


2. ติดตั้ง modules Dashboard Node-Red ไปที่ Manage palette >>Install>> search modules >> พิมพ์ “Dashboard >> เลือก node-red-dashboard >> install


![รูปภาพ: install node-red-dashboard](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668755968870_file.png)



3. หลังจากติดตั้งเสร็จ สังเกตแถบทางซ้ายมือ จะปรากฎ dashboard node สำหรับใช้งาน


![รูปภาพ: Dashboard node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668756487606_file.png)

4. ใช้ switch node สำหรับควบคุม LED ของ NodeMCU  โดย ไปที่แถบทางซ้ายมือ>>dashboard>>เลือก switch



![fig: switch node](https://paper-attachments.dropboxusercontent.com/s_5B2CDC83F09B6CAA259D6A1C2DA4E12C8BBA30AF2DF3C11B70D082BF17634CD2_1675591211022_Untitled.png)



5. ตั้งค่า switch node ให้ส่งข้อความ string “on/off” ใน payload เมื่อสถานะ switch เปลี่ยน ดังภาพด้านล่าง


![](https://paper-attachments.dropboxusercontent.com/s_5B2CDC83F09B6CAA259D6A1C2DA4E12C8BBA30AF2DF3C11B70D082BF17634CD2_1675591331158_image.png)



5. ใช้ node-red เป็น Publish โดย ไปที่แถบทางซ้ายมือ >> network >> เลือก mqtt out node


![Fig: mqtt out node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675414749610_file.png)



3. ดับเบิ้ลคลิ๊กที่โหนด mqtt out node และ ตั้งค่าใส่ข้อมูลช่องต่าง ๆ ดังนี้
    1. Server >> แก้ไขเป็น “IP address ของ Broker” port: “1883”
    2. Topic >> ตั้งค่าเป็น room/light
    3. QoS >> ตั้งค่าเป็น “0” 
    
![Fig: ตัวอย่างการตั้งค่า Server](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675414885865_image.png)
![Fig: ตัวอย่างการตั้งค่า MQTT out node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675414930644_image.png)



7. เชื่อมต่อ mqtt in node และ  switch node เข้าด้วยกัน


![Fig: ตัวอย่าง Use switch node with MQTT Publish flow](https://paper-attachments.dropboxusercontent.com/s_5B2CDC83F09B6CAA259D6A1C2DA4E12C8BBA30AF2DF3C11B70D082BF17634CD2_1675591649598_image.png)


8. คลิ๊ก Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้
9.  เปิดหน้าเบราว์เซอร์ขึ้นมา ใส่ “your ip address:1883/ui”  จะปรากฎหน้า dashboard ของ node-red 


ตัวอย่าง

```
    http://192.168.101.245:1880/ui
```

บันทึกผล: ภาพการตั้งค่า node-red เป็น Publish และ switch node


----------

                                                          *รูปภาพการตั้งค่า mqtt in node ของ node-red และ switch node*


----------


บันทึกผล: ภาพ flow node-red  ของตัวเองดังตัวอย่างขั้นตอนที่ 7


----------


                                                               *รูปภาพ* Fig: Use Node-red Subscribe flow


----------


บันทึกผล: ภาพหน้า dashboard


----------

                                                      *รูปภาพ รวมการรันทั้งระบบหน้า dashboard* 


----------


## **Use Text node on Node-red Dashboard** 


1. ใช้ text node สำหรับใช้ แสดงข้อมูลที่เป็นข้อความ โดย ไปที่แถบทางซ้ายมือ>>dashboard>>เลือก text input
![รูปภาพ: text node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668758369209_image.png)

2. ตั้งค่า text node แสดงข้อความ string “on/off” ตาม payload เมื่อสถานะ switch เปลี่ยน ดังภาพด้านล่าง


![fig: ตัวอย่างตั้งค่า text node](https://paper-attachments.dropboxusercontent.com/s_5B2CDC83F09B6CAA259D6A1C2DA4E12C8BBA30AF2DF3C11B70D082BF17634CD2_1675594561775_Untitled.png)



3. สร้าง mqtt in node เป็น Subscribe โดย ไปที่แถบทางซ้ายมือ >> network >> เลือก mqtt in node


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674121375258_Screenshot+2023-01-19+164133.png)



4. ดับเบิ้ลคลิ๊กที่โหนด mqtt in node และ ตั้งค่าใส่ข้อมูลช่องต่าง ๆ ดังนี้
    1. Server >> แก้ไขเป็น “IP address ของตัวเอง” port: “1883”
    2. Action >> เลือก “Subscribe to single topic”
    3. Topic >> ตั้งค่าเป็นชื่อเดียวกันกับหัวข้อ Topic ของ publish คือ “room/light”
    4. QoS >> ตั้งค่าเป็น “0” 
    5. Output >> เลือก Auto-detect
    
![Fig: ตัวอย่างการตั้งค่า Server](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675391744627_image.png)
![Fig: ตัวอย่างการตั้งค่า MQTT in node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675392598210_image.png)


  


5. เชื่อมต่อ mqtt in node และ  text node เข้าด้วยกัน


![Fig: flow use text node with mqtt in node](https://paper-attachments.dropboxusercontent.com/s_5B2CDC83F09B6CAA259D6A1C2DA4E12C8BBA30AF2DF3C11B70D082BF17634CD2_1675594473397_image.png)



6. คลิ๊ก Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้
7.  เปิดหน้าเบราว์เซอร์ขึ้นมา ใส่ “your ip address:1883/ui”  จะปรากฎหน้า dashboard ของ node-red 

ตัวอย่าง

    http://192.168.101.245:1880/ui

**บันทึกผล: ภาพการตั้งค่า node-red เป็น Publish และ switch node**

----------




                                                          *รูปภาพการตั้งค่า mqtt in node ของ node-red และ switch node*





----------

**บันทึกผล: ภาพ flow node-red  ของตัวเองดังตัวอย่างขั้นตอนที่ 6**
 ****

----------




                                                               *รูปภาพ* Fig: Use Node-red Subscribe flow





----------


บันทึกผล: ภาพรวมการทำงานทั้งระบบและ หน้า dashboard


----------


                                                      *รูปภาพ รวมการทำงานทั้งระบบและ หน้า dashboard*




----------
----------


[1] Ref. http://stevesnoderedguide.com/node-red-dashboard


