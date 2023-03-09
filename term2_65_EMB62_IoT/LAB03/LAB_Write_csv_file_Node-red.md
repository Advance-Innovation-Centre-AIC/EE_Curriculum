# **Outline**
- Overview
- ขั้นตอนการทดลอง

# **Overview LAB2: Write csv file in Node-red**

  จากการทดลองนี้เป็นการเขียนโปรแกรม node-red นำค่าที่อ่านได้จากการทดลองที่ 1 ไปเก็บลงไฟล์ csv โดยการเพิ่ม write file node และตั้งค่าเก็บไว้ในพื้นที่คอมพิวเตอร์ของเรา      
      

![fig: write file node](https://paper-attachments.dropboxusercontent.com/s_658EA92A6511F4A6D9DBC5C18FA68E122C12026AE7FD8BD469980BE09BFF5730_1668764340477_image.png)



# **ขั้นตอนการทดลอง**

1. ไปที่ ไดร์ฟ D ในคอมพิวเตอร์ของนิสิตและสร้าง folder ชื่อ “data_logger” 
2. คลิ๊กที่ ไฟล์ source >> [createfilecsv.json](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB03/flows/createfilecsv.json)  และ copy code ไปลง node-red ของตัวเอง 

3. ไปที่ แถบขวามือ>>คลิ๊กที่แถบ ขีดสามขีด>> เลือก import


![fig: import function](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1676198928565_Untitled.png)


4. วาง code ลงหน้า cilpboard >>ที่มุมซ้าย เลือก new flow >> import 



![](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1676199206287_Untitled.png)


5. สังเกตที่แถบ flow จะมี flow ชื่อว่า “Createfilecsv” ปรากฎ



![](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1676199329352_image.png)


6. ทำการคลิ๊กที่ node สีฟ้าอย่างละครั้งจะได้ไฟล์ csv 3ไฟล์ อยู่ใน folder data_logger


![](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1676199448253_image.png)

7. กลับไปที่ flow node ของตัวเอง 
8. สร้าง 3 node และตั้งค่าตามขั้นตอนการทดลองที่1 
9. ไปที่แถบซ้ายมือ >> storage >> เลือก write file node
10. ตั้งค่า write file node ดังภาพด้านล่าง


![](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1676200773070_image.png)


11. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกันตามภาพด้านล่าง และ คลิ๊ก Done


![fig: write data MQTT to csv file flow](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1676200873202_image.png)

12. ให้สร้าง node แบบขั้นตอน 11 อีก 2 ชุด และ ทำการตั้งค่าให้เก็บข้อมูลของ Topic room2 และ room3 ลงไฟล์ data_room2.csv และ data_room3.csv ตามลำดับ
13. คลิ๊กที่ Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้

บันทึกผล: ภาพ flow node-red  ของตัวเองทั้งหมด


----------


                                                               *รูปภาพ: Use Node-red flow*


----------


บันทึกผล: ภาพรวมการทำงานทั้งระบบ และ แน็บไฟล์ csv. ที่เก็บข้อมูล ส่งใน classroom


----------

                                                   *รูปภาพ: รวมการรันทั้งระบบ*



----------
----------

[1]Ref: http://www.steves-internet-guide.com/using-arduino-pubsub-mqtt-client/
[2]Ref: https://randomnerdtutorials.com/esp8266-and-node-red-with-mqtt/


