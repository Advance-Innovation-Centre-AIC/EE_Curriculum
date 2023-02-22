# LAB10: Node-red with Raspberry Pi GPIO

# **จุดประสงค์**
1. สามารถใช้ Node-red ควบคุมการทำงาน GPIO pin ของ raspberry Pi ตามที่กำหนดได้ 
# **อุปกรณ์ทดลอง**
1. Computer 
2. RaspberryPi 
3. ชุดเซนเซอร์ Crow Pi
# **โปรแกรมที่เกี่ยวข้อง**
1. Node-red
2. VNC Viewer หรือ โปรแกรม Remote อื่น ๆ 


# **LAB1: Use Node-red Control GPIO pin**

ทดลองใช้ node-red ควบคุม LED ผ่าน GPIO pin ของ raspberry pi 


## **ขั้นตอนการทดลอง**
1. เปิดโปรแกรม node-red บน Raspi 
    - โดยเปิด terminal ของ raspberr pi ขึ้นมาใส่คำสั่งดังนี้
    node-red start


2. เปิดหน้า editor สำหรับเขียนโปรแกรมของ Node-red โดย 
    - เปิด Web Browser บนคอมพิวเตอร์ที่เชื่อมต่อ network เดียวกันกับ Raspberry Pi ขึ้นมา 
    - ใส่ url:http://(ip-addressของRasPi):1880 


![fig: หน้า editor สำหรับเขียนโปรแกรมของ Node-red](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676543541139_image.png)



3. สร้าง inject node ขึ้นมา 2 node ให้เป็นตัวส่งข้อความ 0 และ 1 ไปยัง payload เมื่อมีการคลิ๊กที่ตัวมัน โดย 
    - ไปที่แถบซ้ายมือ >> common >> เลือก inject node
    
![fig: inject node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676529368807_Untitled.png)



4. การตั้งค่า inject node on/off โดย ดับเบิ้ลคลิ๊กที่ inject node 
    (1). ตั้งชื่อให้ inject node แต่ละตัว
        - ไปที่ Name >>ใส่ node นึงเป็น NO ส่วนอีก node เป็น OFF
    (2). กำหนดค่าให้ msg.payload ส่งค่า string 
        - ไปที่ ช่องใส่ใต้ Name เลือก เป็น msg.pyload 
        - ช่องหลังเท่ากับ เลือก string >>ใส่ 1  ที่ node ชื่อ NO 
                                                >> ใส่ 0 ที่ node ชื่อ OF
    (3). ตั้งให้ไม่ต้อง Repeat 
        - ไปที่ Repeat >> เลือก none
5. คลิ๊ก Done เพื่อ save การตั้งค่า


![fig: ตั้งค่า inject node ส่งค่า 1](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676609661033_image.png)
![fig: ตั้งค่า inject node ส่งค่า 0](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676609617708_image.png)



6. สร้าง rpi- gpio out node โดย
    - ไปที่แถบซ้ายมือ ที่ช่องค้นหา พิมพ์ “rpi” 
    - เลือก rpi-gpio out node 


![fig: gpio out  node](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676610109252_Untitled.png)



7. การตั้งค่า rpi-gpio out node  ให้รับค่า payload จาก node-red ส่งไปควบคุม GPIO21 ของ raspberry pi โดย ดับเบิ้ลคลิ๊กที่ node 
    (1). ไปที่ Properties >> Pin >> เลือก pin 40 - GPIO21
    (2). ไปที่ Type >> เลือก Digital output

     (3). ติ๊กที่ช่อง Initialise pin state? >> ตั้งค่าให้มีค่าเริ่มต้นเป็น 0 
     (4).ไปที่ Name >> ตั้งชื่อ node เป็น  “Pin40-Blink_Crowpi_No.#” 

        - โดยใส่เลขตามชุด Crowpi ของนิสิตแทน # ตัวอย่าง  “Pin40-Blink_Crowpi_No.1”
8. คลิ๊ก Done เพื่อ save การตั้งค่า

  

![fig: ตัวอย่างการตั้งค่า rpi-gpio out node](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676611542875_Untitled.png)


  

9. เชื่อมต่อ ทั้ง 3 node เข้าด้วยกันภาพ


![fig: Node-red control LED RPi  flow](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676611668613_image.png)



10. ทดสอบการทำงานของ node ที่สร้างขึ้น โดยคลิ๊ก Deploy 

**บันทึกผล: ภาพถ่ายชุด CrowPi ที่เปิดหน้า editor ของ node-red บน Browser ที่จอ Crowpi สั่งงาน GPIO pin เป็น ON และ OFF**

----------

*ภาพการทดลอง ON /OFF*


----------


## **แบบฝึกหัดที่1**
- ทดลองใช้ node-red ควบคุม Buzzer ของชุด Crow Pi ผ่าน GPIO18 ของ raspberryPi แล้วบันทึกผลตามตัวอย่าง LAB ที่ 1


----------
----------
# **LAB2: Use Node-red to read DHT11 sensor** 

ทดลองใช้ node-red อ่านค่า DHT11 sensor ของชุด Crow Pi ผ่าน GPIO4 ของ raspberryPi

## **ขั้นตอนการทดลอง**
1. สร้าง inject node
    - ไปที่แถบซ้ายมือ >> common >> เลือก inject node


![fig: inject node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676529368807_Untitled.png)



2. ตั้งค่าให้ inject node เป็นตัวส่งข้อความ timestamp ไปยัง payload แบบ interval ที่มีการทำซ้ำ ทุก ๆ 5 วินาที โดย ดับเบิ้ลคลิ๊กที่ inject node 
        (1). ไปที่ ช่องใส่ใต้ Name เลือก เป็น msg.pyload และ เลือก timestamp
        (2). ตั้งให้ Repeat ทุก ๆ 5 วินาที
        - ไปที่ Repeat >> เลือก interval >>every ใส่ 5 >>เลือก seconds
            
![fig: ตั้งค่า inject node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676529024985_Untitled.png)



3. สร้าง  rpi-dht22 node โดย
    - ไปที่แถบซ้ายมือ ที่ช่องค้นหา พิมพ์ “rpi” 
    - เลือก rpi-dht22 node
![fig: rpi-dht22 node](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676613291038_image.png)



4. ตั้งค่า rpi-dht22 node โดย ดับเบิ้ลคลิ๊กที่ node  ตั้งค่าตามภาพด้านล่าง 


![fig: rpi-dht22 node](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676613440426_Untitled.png)



5. สร้าง function node เพื่อเพิ่มค่า timestamp ให้กับข้อมูลเซนเซอร์ที่อ่านได้ ดังนี้ 
    - ไปที่แถบซ้ายมือ >> function >> เลือก function node
    
![fig: function node](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1675937730119_Screenshot+2023-02-09+171434.png)



    - ดับเบิ้ลคลิ๊กที่ function node >>Properties>>ใส่ code ด้านล่างลงที่ช่อง On Message 
    

Name: Timestamp, temperature

    var t = new Date();
    var timestemp = t.getFullYear() 
            + "/" + (t.getMonth() + 1) 
            + "/" + t.getDate()
            + "," + t.getHours() 
            + ":" + t.getMinutes() 
            + ":" + t.getSeconds();
    
    var temp = msg.payload;
    var data = timestemp + "," + temp;
    msg.payload = data;
    return msg
    


6. คลิ๊ก Done เพื่อ save การตั้งค่า function node
7. สร้าง debug node  
    - ไปที่แถบซ้ายมือ >> common >> เลือก debug node


![fig:  debug node](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674122277007_Screenshot+2023-01-19+165723.png)



8. ตั้งค่าให้แสดงค่า payload ที่เป็นค่า output จาก function node โดย 
    - ดับเบิ้ลคลิ๊กที่ debug node 
    - ตั้งค่าตามภาพด้านล่าง โดยที่ช่อง Name ให้ใส่เลขชุดทดลอง CrowPi ของตัวเอง 

เช่น ชุด Crowpi 1 ใส่ “Temp CrowPi No.1”

    - คลิ๊ก Done เพื่อ save การตั้งค่า


![fig: Edit debug node](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676613693847_image.png)



9. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกัน โดยเรียงลำดับดังนี้
**    
                *inject node → rpi-dht22 node → function node → debug node*     

**บันทึกผล: ภาพถ่ายชุด CrowPi ที่เปิดหน้า editor ของ node-red บน Browser ผ่าน** ***usl:*** **http://localhost:1880   ที่จอ Crowpi ในตอนที่โปรแกรมอ่านค่า sensor** 

----------









----------


# **LAB3: Use Node-red Dashboard control Raspberry Pi**  

ทดลองใช้ button node ในการกดสั่ง เปิด-ปิด LED pin40 บน Crowpi ผ่าน GPIO21 ของ Raspberry Pi 

## **ขั้นตอนการทดลอง**
1. ติดตั้ง modules Dashboard Node-Red 
    - ไปที่ Manage palette >>Install>> search modules >> พิมพ์ “Dashboard >> เลือก node-red-dashboard >> install
2. สังเกตแถบทางซ้ายมือ จะปรากฎ dashboard node สำหรับใช้งาน


![fig: install node-red-dashboard](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668755968870_file.png)
![fig: Dashboard node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668756487606_file.png)



3. หล้งจากติดตั้ง dashboard เพิ่มมาแล้วให้ไปที่แถบเครื่องมือด้านขวา>>เลือก Dashboard >>layout


![fig: Layout Dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676364484241_Untitled.png)



4. คลิ๊กที่ + tab เพื่อสร้างหน้า Dashboard 
5. เพิ่มสร้าง tab แล้วให้คลิ๊ก edit 


![fig: Create tab](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676364831304_Untitled.png)



8. เมื่อหน้า edit tab  ปรากฎให้แก้ชื่อ Dashboard เป็น “My CrowPi No.#” โดย # ให้แทน เป็น ตัวเลขชุดทดลอง CrowPi ของตนเอง 
9. คลิ๊ก update เพื่อบันทึกการตั้งค่า


![fig: ตัวอย่างการตั้งค่า ชื่อ dashboard node-red](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676790002565_Untitled.png)



10. ทำการสร้าง group ที่ 1 Group
    - โดย ไปที่ tab ที่เราแก้ไขชื่อ >> คลิ๊กที่ +  Group จะปรากกฎ Group อยู่ใน dashboard ของเรา 


![fig: Create Groups tab on dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676365803952_Untitled.png)



11. หลังจากสร้าง layout dashboard แล้วให้กลับไปหน้า editor ของ node-red เพื่อทำการเขียนโปแกรม 
12. สร้าง button node ขึ้นมา 2 node สำหรับควบคุม On/Off LED pin 40 บน CrowPi
    - โดยไปที่แถบทางซ้ายมือ >> dashboard >> เลือก button 


![fig: button node](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676790552025_Untitled.png)



13. ตั้งค่าแต่ละ button node ที่สร้างมา โดยดับเบิ้ลคลิ๊กที่ button node 
    (1 ). ตั้งค่าให้ทั้ง button node แสดงบน Group1 dashboard  ของนิสิต 
        - โดย ไปที่ Properties >> Group >> เลือก “[My CrowPi No.#]Group1”
    (2). ตั้งชื่อที่ต้องการแสดงบน Dashboard ให้ button node โดย node นึง On และ อีก node เป็น Off
        - ไปที่ช่อง Label >>ใส่ชื่อ ตัวอย่างเช่น “ON”
    (3). ตั้งชื่อที่แสดงบน editor เป็นชื่อเดียวกับช่อง label ของแต่ละ node 
        - ไปที่ช่อง name >>ใส่ชื่อ node  ตัวอย่างเช่น label ชือ “ON”  ให้ใส่ “ON”
    (4). ตั้งค่าให้ข้อความใน payload เมื่อมีการกดที่ button node ที่ชื่อ ON และ OFF 
        - ที่ button node ชื่อ NO ไปที่ช่อง Payload >>เลือก string>>ใส่ข้อความ “1”
        - ที่ button node ชื่อ OFF ไปที่ช่อง Payload >>เลือก string>>ใส่ข้อความ “0”
        - ไปที่ช่อง Topic >>เลือก msg >>ใส่ข้อความ “payload”
14. คลิ๊ก Done เพื่อ save การตั้งค่า


![fig: ตัวอย่าง ตั้งค่า button node ชื่อ ON](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676792642911_Untitled.png)

15. สร้าง rpi- gpio out node แตะตั้งค่าตาม LAB1 ในขึ้นตอนที่ 6 สำหรับรับค่า payload จาก button node ทั้ง 2 node 
16. เชื่อมทั้ง 2 button node เข้ากับ rpi-gpio out node   
17. ทดสอบการทำงานของ node ที่สร้างขึ้น โดยคลิ๊ก Deploy  
18. เปิด Web Browser บน CrowPi ขึ้นมา และไปที่ url : http://localhost:1880/ui 

**บันทึกผล: ภาพถ่ายชุด CrowPi ที่เปิดหน้า editor และ dashboard  ของ node-red บน Browser ที่จอ Crowpi สั่งงาน GPIO pin เป็น ON และ OFF** 

----------

*ภาพการทดลอง ON* 

*ภาพการทดลอง OFF*


----------


## **แบบฝึกหัดที่2**
- ทดลองสร้าง dashboard node-red ควบคุม Buzzer ของชุด Crow Pi ผ่าน GPIO18 ของ raspberryPi แล้วบันทึกผลตามตัวอย่าง LAB ที่ 3
----------

[1] Ref. https://iotdesignpro.com/projects/home-automation-with-node-red-and-raspberry-pi

