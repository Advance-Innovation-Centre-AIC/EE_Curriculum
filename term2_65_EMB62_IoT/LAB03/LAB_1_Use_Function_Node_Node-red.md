# **Outline**
- Overview
- ขั้นตอนการทดลอง


# **Overview LAB 1: Use Function node in Node-red** 
   
   ทดลองนี้จะทำใช้ Function node ของ Node-red เขียนโปรแกรมให้รับค่าจาก payload และ ไปแสดงผลบน 
dashboard พร้อมกับค่า timestamp 


![Fig: MQTT flow diagram](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1676179284557_file.png)

    
   จากภาพเป็น flow diagram ของระบบ MQTT สำหรับแล็ปการทดลองนี้โดย ในระบบจะประกอบด้วย 
device 3 ตัว ที่จะเป็นตัวส่งข้อมูลกันโดยมีชื่อ topic ต่างกัน ผ่านบอร์ด Raspberry Pi ที่จะเป็น MQTT Broker และ ใช้ Node-red ที่อยู่บน PC ของแต่ละคน subscribe แต่ละ topic ผ่าน Broker เดียวกัน 

# **ขั้นตอนการทดลอง**

## **Use Node-red Subscrilbe**
1. เปิดหน้า CMD ขึ้นมาใหม่อีก 1 teb และใช้คำสั่ง เปิด node-red 
   
 ``` 
    node-red start 
```

2. ทดลองสร้าง node-red เป็น Subscribe โดย ไปที่แถบทางซ้ายมือ >> network >> เลือก mqtt in node


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674121375258_Screenshot+2023-01-19+164133.png)



3. ดับเบิ้ลคลิ๊กที่โหนด mqtt in node และ ตั้งค่าใส่ข้อมูลช่องต่าง ๆ ดังนี้
    1. Server >> แก้ไขเป็น “IP address ของ Broker” port: “1883”
    2. Action >> เลือก “Subscribe to single topic”
    3. Topic >> ตั้งค่าเป็นชื่อเดียวกันกับหัวข้อ Topic ของ publish
    4. QoS >> ตั้งค่าเป็น “0” 
    5. Output >> เลือก Auto-detect

![Fig: ตัวอย่างการตั้งค่า Server](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675391744627_image.png)
![Fig: ตัวอย่างการตั้งค่า MQTT in node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675392598210_image.png)


4. ไปที่แถบซ้ายมือ >> function >> เลือก function node


![fig: function node](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1675937730119_Screenshot+2023-02-09+171434.png)


5. จากข้อมูลรูปแบบที่ได้จาก MQTT in node เป็นข้อมูล string เราต้องการเพิ่มค่า timestamp โดยดับเบิ้ลคลิ๊กที่ function node >>Properties>>ใส่ code ด้านล่างลงที่ช่อง On Message 

```
    var now = new Date();
    var timestemp = now.getFullYear()
        + "/" + (now.getMonth() + 1)
        + "/" + now.getDate()
        + "," + now.getHours()
        + ":" + now.getMinutes()
        + ":" + now.getSeconds();
    // ตัวอย่างข้อมูล random
    // var temp = Math.round(Math.random() * 100);
    // var humi = Math.round(Math.random() * 10);
    
    var data = timestemp +","+ msg.payload;
    msg.payload = data;
    return msg;
```    



6. ไปที่แถบซ้ายมือ >> common >> เลือก debug node



![fig:  debug node](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674122277007_Screenshot+2023-01-19+165723.png)



7. ดับเบิ้ลคลิ๊กที่ debug node และ ตั้งค่าให้แสดงค่า output เป็น object โดยสามารถตั้งค่าตามภาพด้านล่าง และ คลิ๊ก Done


![Fig: ตัวอย่างการตั้งค่า debug node](https://paper-attachments.dropboxusercontent.com/s_DA7F9304F7FD16C94028EC84CCC3FE7AF8CB3BE2BB9AC49BF08A86122CCAFA23_1675409973531_image.png)



8. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกันตามภาพด้านล่าง และ คลิ๊ก Done


![Fig: ตัวอย่าง Use function Node-red  flow](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1675939703260_image.png)


9. คลิ๊ก Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้

บันทึกผล: ภาพการตั้งค่า node-red เป็น Subscribe ของตัวเองดังตัวอย่างขั้นตอนที่ 3


----------


                                                          *รูปภาพการตั้งค่า mqtt in node ของ node-red* 


----------


บันทึกผล: ภาพ flow node-red  ของตัวเองดังตัวอย่างขั้นตอนที่ 8


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


