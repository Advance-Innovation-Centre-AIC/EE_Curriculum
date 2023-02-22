# LAB11: Basic Node-red Dashboard

# **จุดประสงค์**
1. สามารถแสดงข้อมูลบน Dashboard ของ Node-red ตามที่กำหนดได้ 
# **อุปกรณ์ทดลอง**
1. Computer 
# **โปรแกรมที่เกี่ยวข้อง**
1. Node-red
# **LAB1: Create tabs and Groups on Dashboard** 

การทดลองนี้กำหนดให้ทดลองสร้างหน้า Dashboard โดยมีการจัด layout แบ่งเป็น 2 Groups 

- โดย Group1 ชื่อ Controlling 
    - มีแสดง Switch สำหรับควบคุมเปิด-ปิด จำนวน 3 ตัว 
- ส่วน Group2 ชื่อ Monitoring 
    - แสดงสถานะ switch แบบข้อความ จำนวน 3 ชุดข้อมูล 
    - และ ข้อมูลแบบกราฟ จำนวน 2 ชุดข้อมูล
![fig: component of Smart home Model on Node-red Dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676524647843_Untitled.png)



## **ขั้นตอนการทดลอง**
1. เปิดหน้า  node-red  บนคอมพิวเตอร์ของตัวเอง โดยใช้คำสั่ง 
    node-red start 


2. เปิดหน้า editor สำหรับเขียนโปรแกรมของ Node-red โดย 
    - เปิด Web Browser บนคอมพิวเตอร์ที่เชื่อมต่อ network เดียวกันกับ Raspberry Pi ขึ้นมา 
    - ใส่ url:http://(ip-addressของRasPi):1880 


![fig: หน้า editor สำหรับเขียนโปรแกรมของ Node-red](https://paper-attachments.dropboxusercontent.com/s_2C13000DC6F13E536CABBC78E2E49EA9AB888FD291A9D82FBAC717817612EF08_1676543541139_image.png)



3. ติดตั้ง modules Dashboard Node-Red 
    - ไปที่ Manage palette >>Install>> search modules >> พิมพ์ “Dashboard >> เลือก node-red-dashboard >> install
4. สังเกตแถบทางซ้ายมือ จะปรากฎ dashboard node สำหรับใช้งาน


![fig: install node-red-dashboard](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668755968870_file.png)
![fig: Dashboard node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668756487606_file.png)



5. หล้งจากติดตั้ง dashboard เพิ่มมาแล้วให้ไปที่แถบเครื่องมือด้านขวา>>เลือก Dashboard >>layout


![fig: Layout Dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676364484241_Untitled.png)



6. คลิ๊กที่ + tab เพื่อสร้างหน้า Dashboard 
7. เพิ่มสร้าง tab แล้วให้คลิ๊ก edit 


![fig: Create tab](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676364831304_Untitled.png)



8. เมื่อหน้า edit tab ปรากฎให้แก้ชื่อ Dashboard เป็น “My Home รหัสนิสิต” และตั้งค่าตามภาพด้านล่าง 


![fig: edit dashboard tab node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676365163216_image.png)



9. คลิ๊ก update 
10. ทำการสร้าง 2 groups ตามที่ concept กำหนด 
    - โดย ไปที่ tab ที่เราแก้ไขชื่อ >> คลิ๊กที่ +  Group จะปรากกฎ Group อยู่ใน dashboard ของเรา 


![fig: Create Groups tab on dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676365803952_Untitled.png)



11. คลิ๊กที่ edit ของแต่ละ Group แก้ไขชื่อเป็น Controlling และ Monitoring ตามลำดับ


![fig: name Groups node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676366199457_image.png)


  

12. สร้าง spacer ในแต่ละ Group โดยไปที่ Group >> + spacer 


![fig: layout dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676368942608_Untitled.png)



13. เมื่อสร้าง layout ตามที่กำหนดครบแล้วให้ คลิ๊ก Deploy  
14. เข้าหน้า dashboard โดยเปิด Web Browser ขึ้นมาไปที่ url : [http://localhost:1880/ui](http://localhost:1880/ui)


![fig: Example layout dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676369203314_image.png)


**บันทึกผล: ภาพหน้า layout dahboard และ ภาพหน้า web Browser UI ของนิสิต ตัวอย่างดังขั้นตอนที่ 12 และ ขั้นตอนที่ 14**  

----------

*ภาพหน้า layout dahboard* 


----------

*ภาพหน้า web Browser UI* 


----------
----------
# **LAB2: Use Switch node**

     จากภาพ concept ด้านล่าง กำหนดให้สร้าง switch สำหรับควบคุมไฟแต่ละห้อง ทั้งหมด 3 switch อยู่บน Group1: Controlling ซึ่งเราสามารถสร้าง switch และตั้งค่าให้อยู่บน layout dashboard ตามที่เราสร้างขึ้นก่อนหน้านี้ได้ดังขั้นตอนต่อไปนี้
     

![fig: component on Group1 dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676524566609_Untitled.png)



## **ขั้นตอนการทดลอง**
1. สร้าง switch node สำหรับควบคุม light room ทั้งหมด 3 switch 
    - โดยไปที่แถบทางซ้ายมือ >> dashboard >> เลือก switch


![fig: switch node](https://paper-attachments.dropboxusercontent.com/s_5B2CDC83F09B6CAA259D6A1C2DA4E12C8BBA30AF2DF3C11B70D082BF17634CD2_1675591211022_Untitled.png)



2. ตั้งค่าแต่ละ switch node ที่สร้างมา โดยดับเบิ้ลคลิ๊กที่ switch node 
    (1 ). ตั้งค่าให้ทั้ง 3 switch node แสดงบน Group Controlling dashboard  ของนิสิต 
        - โดย ไปที่ Properties >> Group >> เลือก “[My Home รหัสนิสิต]Controlling”
    (2). ตั้งชื่อทั้ง 3 switch node ให้มีชื่อตามกำหนดคือ Living room, Bedroom และ ฺBathroom ตามลำดับ
        - ไปที่ช่อง Label >>ใส่ชื่อ ตัวอย่างเช่น “Living room”
    (3). ตั้งชื่อ switch node เดียวกันกับช่อง label ของ switch node แต่ละตัว 
        - ไปที่ช่อง name >>ใส่ชื่อswitch node  ตัวอย่างเช่น “Living room”
    (4). ตั้งค่าให้ข้อความใน payload เปลี่ยนตามสถานะ switch และ แสดงข้อความ payload ใต้ switch node  
        - ไปที่ช่อง On Payload >>เลือก string>>ใส่ข้อความ “on”
        - ไปที่ช่อง Off Payload >>เลือก string>>ใส่ข้อความ “off”
        - ไปที่ช่อง Topic >>เลือก msg >>ใส่ข้อความ “payload”
3. คลิ๊ก Done เพื่อ save การตั้งค่า


![fig: ตัวอย่างการตั้งค่า switch ของ Living room](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676373371788_Untitled.png)



7. ทดสอบการทำงานของ switch node ที่สร้างขึ้น โดยคลิ๊ก Deploy 
8. ไปที่ Web Browser ขึ้นมาไปที่ url : http://localhost:1880/ui

**บันทึกผล: ภาพหน้าการตั้งค่าทั้ง 3 switch node ตัวอย่างตามขั้นตอนที่ 3**

----------


1. *ภาพการตั้งค่า switch ของ Living room*
2. *ภาพการตั้งค่า switch ของ*  *Bedroom* 
3. *ภาพการตั้งค่า switch ของ  Bathroom*


----------

**บันทึกผล: ภาพหน้า Flow swtich node  และ ภาพหน้า web Browser UI dashboard สถานะทั้ง switch  3 ห้องเป็น on**

----------

*ภาพหน้า Flow swtich node  usl:* http://localhost:1880 


----------

*ภาพหน้า web Browser UI* url : http://localhost:1880/ui


----------
----------
# **LAB3: Use Text node**

     จากภาพ concept ด้านล่าง กำหนดให้สร้าง Text node สำหรับแสดงข้อความสถานะไฟในแต่ละห้อง ทั้งหมด 3 node อยู่บน Group2: Monitoring ซึ่งเราสามารถสร้าง Text node และตั้งค่าให้อยู่บน layout dashboard ตามที่เราสร้างขึ้นก่อนหน้านี้ได้ดังขั้นตอนต่อไปนี้


![fig: component for Status light room on Group2 dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676439236543_Untitled.png)



## **ขั้นตอนการทดลอง**
1. สร้าง Text node สำหรับแสดงข้อความสถานะ light room ทั้งหมด 3 node โดยไปที่แถบทางซ้ายมือ >> dashboard >> เลือก text node


![fig: text node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668758369209_image.png)



2. เชื่อมต่อ text node เข้ากับ switch node ที่สร้างขึ้นจากการทดลองที่ 1 ตามแต่ละห้อง


![fig: ตัวอย่างการเชื่อม switch node และ  text node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676442863320_image.png)



3. ตั้งค่าแต่ละ text node ที่สร้างมา โดยดับเบิ้ลคลิ๊กที่ text node 
    (1 ). ตั้งค่าให้ทั้ง 3 text node แสดงบน Group Monitoring dashboard  ของนิสิต 
        - โดย ไปที่ Properties >> Group >> เลือก “[My Home รหัสนิสิต] Monitoring”
    (2). ตั้งชื่อทั้ง 3 text node ให้มีชื่อตามกำหนดคือ Living room, Bedroom และ ฺBathroom ตามลำดับ
        - ไปที่ช่อง Label >>ใส่ชื่อ ตัวอย่างเช่น “Light: Living room”
    (3). ตั้งชื่อ text node เดียวกันกับช่อง label ของ text node แต่ละตัว 
        - ไปที่ช่อง name >>ใส่ text node  ตัวอย่างเช่น “Light: Living room”
    (4). ตั้งค่าให้แสดงข้อความ payload ตามสถานะ switch  บน dashboard 
        - ไปที่ช่อง Volue format >> ใส่ “{{msg.payload}}”
    (5). ตั้งค่า Layout การแสดงข้อความ ตามภาพตัวอย่าง 


4. คลิ๊ก Done เพื่อ save การตั้งค่า


![fig: ตัวอย่างการตั้งค่า Text node ของ Living room](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676454340278_Untitled.png)



7. ทดสอบการทำงานของ switch node ที่สร้างขึ้น โดยคลิ๊ก Deploy 
8. ไปที่ Web Browser ขึ้นมาไปที่ url : http://localhost:1880/ui

**บันทึกผล: ภาพหน้าการตั้งค่าทั้ง 3 text node ตัวอย่างตามขั้นตอนที่ 4**

----------


1. *ภาพการตั้งค่า text node ของ Living room*
2. *ภาพการตั้งค่า text node ของ*  *Bedroom* 
3. *ภาพการตั้งค่า text node ของ  Bathroom*


----------

**บันทึกผล: ภาพหน้า Flow node  และ ภาพหน้า web Browser UI dashboard สถานะทั้ง node ทั้ง  3 ห้องเป็น off**

----------

*ภาพหน้า Flow node  usl:* http://localhost:1880 


----------

*ภาพหน้า web Browser UI* url : http://localhost:1880/ui


----------
----------
# **LAB4: Use Chart node**

     จากภาพ concept ด้านล่าง กำหนดให้สร้าง Chart node สำหรับแสดงข้อมูลอุรหภูมิในแต่ละห้อง ทั้งหมด 2 node อยู่บน Group2: Monitoring ซึ่งเราสามารถสร้าง Chart node และตั้งค่าให้อยู่บน layout dashboard ตามที่เราสร้างขึ้นก่อนหน้านี้ได้ดังขั้นตอนต่อไปนี้


![fig: component for Temperature Chart on Group2 dashboard](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676524899980_Untitled.png)



## **ขั้นตอนการทดลอง**
1. สร้าง inject node เป็นตัวส่งข้อความ timestamp ไปยัง payload แบบ interval ที่มีการทำซ้ำ ทุก ๆ 5 วินาที
    - ไปที่แถบซ้ายมือ >> common >> เลือก inject node


![fig: inject node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676529368807_Untitled.png)



    - ตั้งค่าดังภาพด้านล่าง


![fig: ตั้งค่า inject node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676529024985_Untitled.png)



2. สร้าง function node เพื่อจำลองตัวเลขสุ่มเป็นข้อมูลสำหรับแสดงค่าบน Chart node ดังนี้ 
    - ไปที่แถบซ้ายมือ >> function >> เลือก function node
    
![fig: function node](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1675937730119_Screenshot+2023-02-09+171434.png)



    - ดับเบิ้ลคลิ๊กที่ function node >>Properties>>ใส่ code ด้านล่างลงที่ช่อง On Message 
    

Name: Timestamp+random number

    var temp = Math.round(Math.random() * 100);
    msg.payload = temp;
    return msg;


3. คลิ๊ก Done เพื่อ save การตั้งค่า function node


4. สร้าง Chart node สำหรับแสดงข้อมูลจำลองอุณหภูมิห้อง Livingroom และ Bedroom ทั้งหมด 2 node 
    - ไปที่แถบทางซ้ายมือ >> dashboard >> เลือก Chart node


![fig: chart node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668762063752_image.png)

    
5. ตั้งค่าแต่ละ Chart node ที่สร้างมา โดยดับเบิ้ลคลิ๊กที่ Chart node โดย
    (1 ). ตั้งค่าให้ทั้ง 2 node แสดงบน Group Monitoring dashboard  ของนิสิต 
        - ไปที่ Properties >> Group >> เลือก “[My Home รหัสนิสิต] Monitoring”
    (2). ตั้งชื่อที่ต้องการแสดงบน dashboard ทั้ง 2 node ให้มีชื่อตามกำหนดคือ Temp Living room และ Temp Bedroom 
        - ไปที่ช่อง Label >>ใส่ชื่อ ตัวอย่างเช่น  “Temp Living room”
    (3). ตั้งชื่อให้ Chart node เป็นชื่อเดียวกันกับช่อง label ของแต่ละตัว 
        - ไปที่ช่อง name >>ใสjชื่อ chart node  ตัวอย่างเช่น “Light: Living room”
    (4). ตั้งค่าให้ แกน x มีการแสดงข้อมูลที่ช่วงเวลา 1 ชั่วโมงและ แกน Y ช่วงข้อมูลตั้งแต่ 0-100 
        - ไปที่ช่อง X-axis >> last >> ใส่ค่า 1 >> เลือก hours 
        - ไปที่ช่อง Y-axis >> min >> ใส่ 0 >> max >> ใส่ 100
        - ไปที่ Legend >> เลือก Show >> Inyetpolate >>เลือก linear
6. สำหรับสีของเส้นให้เลือกตามต้องการ
7. คลิ๊ก Done เพื่อ save การตั้งค่า


![fig: ตัวอย่างการตั้งค่า Chart node ของ Living Room](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676530992230_Untitled.png)



8. เชื่อมต่อ ทั้ง 3 node เข้าด้วยกัน


![fig: ตัวอย่าง flow node ของ chart living room](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676531713612_image.png)



9. ทดสอบการทำงานของ node ที่สร้างขึ้น โดยคลิ๊ก Deploy 
10. ไปที่ Web Browser ขึ้นมาไปที่ url : http://localhost:1880/ui

**บันทึกผล: ภาพหน้า Edit chart node การตั้งค่าของทั้ง 2 Chart node** 

----------


1. *ภาพหน้า Edit  Chart node ของ Living room*
2. *ภาพหน้า Edit  Chart node ของ*  *Bedroom* 


----------

**บันทึกผล: ภาพหน้า Flow node โดยมี ส่วนต่าง ๆ ตามที่กำหนดทั้งหมด  และ ภาพหน้า web Browser UI dashboard ทั้งหมด โดยข้อมูลบน chart มีการแสดงผลผ่านมาแล้วมากกว่า 10 นาที**

----------

*ภาพหน้า Flow node  usl:* http://localhost:1880 


----------

*ภาพหน้า web Browser UI* url : http://localhost:1880/ui



----------


----------

[1] Ref. http://www.iotsharing.com/2018/05/how-to-build-iot-dashboard-using-node-red.html




