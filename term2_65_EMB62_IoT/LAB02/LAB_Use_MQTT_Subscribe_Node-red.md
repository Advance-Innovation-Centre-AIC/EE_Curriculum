# **Outline**
- [Overview](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB02/LAB_1_Use_MQTT_Subscribe_Node-red.md#overview)
- [ขั้นตอนการทดลอง](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB02/LAB_1_Use_MQTT_Subscribe_Node-red.md#ขั้นตอนการทดลอง)


# **Overview**

  ทดลองใช้ Node-red เป็น Subscribe อ่านข้อความจาก Publish ที่มี Topic ดังตัวอย่าง เช่น 
Topic:“Test” โดยใช้ โปรแกรมของ Mosquito_pub เป็น Publish ผ่าน Mosquitto Broker


![Fig: flow MQTT Subscribe Using Node-red diagram](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675590605877_file.png)


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

***หมายเหตุ ถ้า port 1883 มีการใช้งานอยู่ ให้ทำการ kill process ด้วยคำสั่งดังนี้

คำสั่ง ค้นหาตัวเลข PID 

```
    netstat -ano | findstr 1883
```

คำสั่ง kill process โดยแก้ไข ตัวเลข 5212 เป็น ตัวเลขที่แสดงคอลัมท์ PID จากคำสั่งก่อนหน้า

```
    taskkill /F /PID 5212
```


## **Run Mosquiito_pub**
1. เปิดหน้า CMD ขึ้นมาใหม่อีก 1 teb และ ใช้คำสั่ง cd เข้าไปที่ path ของ mosquitto 
2. พิมพ์คำสั่ง สำหรับ รัน Mosquiito_pub ทำหน้าที่เป็น publish กำหนดค่าดังนี้ 
    a. ตั้งชื่อ topic เท่ากับ **“test”**
    b. ส่งข้อความ **“Hello!!  I’m ชื่อนิสิต”**

ตัวอย่าง command line

```
    #mosquitto_pub -h [hostname or IP address] -t test -m "Hello!!"
    mosquitto_pub -h 192.168.101.245 -t test -m  “Hello!!  I’m ชื่อนิสิต”
```

บันทึกผล: คำสั่งที่ใช้(command line) ในการรัน Mosquiito_pub

----------

                           #ใส่คำสั่งที่ใช้
    
----------

  

บันทึกผล: ภาพการรัน Mosquiito_pub

----------

                     *ภาพผลการรัน Mosquiito Broker*


----------



## **Use Node-red Subscrilbe**

1. เปิดหน้า CMD ขึ้นมาใหม่อีก 1 teb และใช้คำสั่ง เปิด node-red 

```
    node-red start 
```

2. ทดลองสร้าง node-red เป็น Subscribe โดย ไปที่แถบทางซ้ายมือ >> network >> เลือก mqtt in node


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674121375258_Screenshot+2023-01-19+164133.png)



3. ดับเบิ้ลคลิ๊กที่โหนด mqtt in node และ ตั้งค่าใส่ข้อมูลช่องต่าง ๆ ดังนี้
    1. Server >> แก้ไขเป็น “IP address ของตัวเอง” port: “1883”
    2. Action >> เลือก “Subscribe to single topic”
    3. Topic >> ตั้งค่าเป็นชื่อเดียวกันกับหัวข้อ Topic ของ publish
    4. QoS >> ตั้งค่าเป็น “0” 
    5. Output >> เลือก Auto-detect


![Fig: ตัวอย่างการตั้งค่า Server](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675391744627_image.png)

![Fig: ตัวอย่างการตั้งค่า MQTT in node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675392598210_image.png)



4. ไปที่แถบซ้ายมือ >> common >> เลือก debug node


![fig:  debug node](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674122277007_Screenshot+2023-01-19+165723.png)



5. ดับเบิ้ลคลิ๊กที่ debug node และ ตั้งค่าให้แสดงค่า output เป็น object โดยสามารถตั้งค่าตามภาพด้านล่าง และ คลิ๊ก Done


![Fig: ตัวอย่างการตั้งค่า debug node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675409973531_image.png)



6. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกันตามภาพด้านล่าง และ คลิ๊ก Done


![Fig: ตัวอย่าง Use Node-red Subscribe flow](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675409908674_image.png)





7. คลิ๊ก Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้


บันทึกผล: ภาพการตั้งค่า node-red เป็น Subscribe ของตัวเองดังตัวอย่างขั้นตอนที่ 3 


----------

                                                          *รูปภาพการตั้งค่า mqtt in node ของ node-red* 


----------


บันทึกผล: ภาพ flow node-red  ของตัวเองดังตัวอย่างขั้นตอนที่ 6


----------

                                                               *รูปภาพ* Fig: Use Node-red Subscribe flow



----------

บันทึกผล: ภาพรวมการทำงานทั้งระบบ

----------



                                                      *รูปภาพ รวมการรันทั้งระบบ*


----------
----------

[1]Ref: http://www.steves-internet-guide.com/using-arduino-pubsub-mqtt-client/

[2]Ref: https://randomnerdtutorials.com/esp8266-and-node-red-with-mqtt/


