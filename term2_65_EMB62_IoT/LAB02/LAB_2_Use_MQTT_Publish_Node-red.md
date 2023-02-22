# Outline
- [Overview](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB02/LAB_2_Use_MQTT_Publish_Node-red.md#overview-lab2-use-mqtt-publish-on-node-red)
- [ขั้นตอนการทดลอง](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB02/LAB_2_Use_MQTT_Publish_Node-red.md#%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%94%E0%B8%A5%E0%B8%AD%E0%B8%87)

# **Overview LAB2: Use MQTT Publish on Node-red**

   ทดลองใช้ Node-red เป็น Publish อ่านข้อความจาก Subscribe ที่มี Topic ตัวอย่างเช่น  Topic:“Test” 
โดยใช้ โปรแกรมของ Mosquito_sub เป็น Subscribe ผ่าน Mosquitto Broker



![Fig: flow MQTT Publish Using Node-red diagram](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675590724219_file.png)



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


## **Run  Mosquiito_sub**

1. หลังจากเปิด tab command prompt มาใหม่ ให้เข้าไปในโฟล์เดอร์ mosquitto ตาม path ที่เราติดตั้งโปรแกรม โดยใช้คำสั่ง cd 
  
```
   cd C:\Program Files\mosquitto
```

2. พิมพ์คำสั่ง สำหรับ รัน Mosquiito_sub ทำหน้าที่เป็น Subscribe โดยกำหนดค่าดังนี้ 
   
   1. Subscribe ไปที่ชื่อ topic เท่ากับ “รหัสนิสิต”(ภาษาอังกฤษ)

ตัวอย่าง command line

    # mosquitto_sub -h [hostname or IP] -t test
    mosquitto_sub -h 192.168.101.245 -t รหัสนิสิต

บันทึกผล: คำสั่งที่ใช้(command line) ในการรัน Mosquiito_sub

----------

    #ใส่คำสั่งที่ใช้

----------

บันทึกผล: ภาพการรัน Mosquiito_sub

----------


                                                              *ภาพผลการรัน Mosquiito_sub*

----------


## **Use Node-red Publish**
1. เปิดหน้า CMD ขึ้นมาใหม่อีก 1 teb และใช้คำสั่ง เปิด node-red 
   
```
   node-red start 
```

2. ทดลองสร้าง node-red เป็น Publish โดย ไปที่แถบทางซ้ายมือ >> network >> เลือก mqtt out node



![Fig: mqtt out node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675414749610_file.png)



3. ดับเบิ้ลคลิ๊กที่โหนด mqtt out node และ ตั้งค่าใส่ข้อมูลช่องต่าง ๆ ดังนี้
    1. Server >> แก้ไขเป็น “IP address ของ Broker” port: “1883”
    2. Topic >> ตั้งค่าเป็น รหัสนิสิต
    3. QoS >> ตั้งค่าเป็น “0” 


![Fig: ตัวอย่างการตั้งค่า Server](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675414885865_image.png)
![Fig: ตัวอย่างการตั้งค่า MQTT out node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675414930644_image.png)




4. ไปที่แถบซ้ายมือ >> common >> เลือก inject node


![fig:  inject node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675415228287_Untitled.png)



5. ดับเบิ้ลคลิ๊กที่ inject node และ ตั้งค่าดังนี้
    1.  msg.payload เลือก string ส่งข้อความ“message” 
    2.  เลือก >> interval>>every 1 seconds >> คลิ๊ก Done



![Fig: ตัวอย่างการตั้งค่า inject node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675415849061_Untitled.png)


6. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกันตามภาพด้านล่าง และ คลิ๊ก Done


![Fig: ตัวอย่าง Use Node-red Publish flow](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675416155334_image.png)




7. คลิ๊ก Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้


บันทึกผล: ภาพการตั้งค่า node-red เป็น Publish ของตัวเองดังตัวอย่างขั้นตอนที่ 3


----------


                                                          *รูปภาพ: การตั้งค่า mqtt out node ของ node-red* 


----------


บันทึกผล: ภาพ flow node-red  ของตัวเองดังตัวอย่างขั้นตอนที่ 6


----------


                                                               *รูปภาพ: Use Node-red Publish flow*



----------


บันทึกผล: ภาพรวมการทำงานทั้งระบบ

----------


                                                      *รูปภาพ: รวมการรันทั้งระบบ*




----------
----------

[1]Ref: http://www.steves-internet-guide.com/using-arduino-pubsub-mqtt-client/

[2]Ref: https://randomnerdtutorials.com/esp8266-and-node-red-with-mqtt/


