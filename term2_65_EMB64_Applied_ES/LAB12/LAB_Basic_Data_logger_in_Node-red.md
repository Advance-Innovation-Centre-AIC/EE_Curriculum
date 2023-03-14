# **LAB 1: Create and Write csv file without header**

    จากการทดลองนี้เป็นการเขียนโปรแกรม node-red นำค่าไปเก็บลงไฟล์ csv โดยการเพิ่ม write file node และตั้งค่าให้สร้างไฟล์เก็บไว้ในพื้นที่ที่เราคำหนด
          

1. ไปที่ Desktop ในคอมพิวเตอร์ และสร้าง folder ชื่อ “datalog” 
2. สร้าง write file node 
    - ไปที่แถบซ้ายมือ >> storage >> เลือก write file node


![fig: write file node](https://paper-attachments.dropboxusercontent.com/s_658EA92A6511F4A6D9DBC5C18FA68E122C12026AE7FD8BD469980BE09BFF5730_1668764340477_image.png)



3. ตั้งค่าให้ write file node สร้างไฟล์เก็บไว้ใน folder ที่สร้างขึ้นก่อนหน้า โดย ดับเบิ้ลคลิ๊กที่ node
    (1). ไปที่ Filename >> เลือก path >> ใส่ path ที่อยู่ของ folder ชื่อ “datalog” 
        - เพิ่ม “/data_รหัสนิสิต.csv” หลังใส่ path
    (2). ไปที่ Action >> “append to File” เพื่ออนุญาติให้เขียนข้อมูลต่อจากข้อมูลเดิมถ้ามีอยู่แล้ว
        - ติ๊กทั้ง 2 ช่อง เพื่อ กำหนดให้ขึ้นบรรทัดใหม่ทุกครั้ง และ ถ้าไม่มี ไฟล์ ชื่อตามที่กำหนดให้สร้างใหม่
    (3). ไปที่ Name >> ใส่ “write file”  


![fig: ตั้งค่า write file node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677742590478_Untitled.png)



4. สร้าง inject node ขึ้นมา 1 node 
    - ไปที่แถบซ้ายมือ >> common >> เลือก inject node


![fig: inject node](https://paper-attachments.dropboxusercontent.com/s_A5E95AB51EE1AF35346DDF9CFF68330E25C993FDA296C5C779550CEF4FB19221_1676529368807_Untitled.png)



5. ตั้งค่าให้ inject node เป็นตัวส่ง timestamp ไปยัง payload และทำงานทุกครั้งเมื่อกดที่โหนด โดย ดับเบิ้ลคลิ๊กที่ inject node 
        (1). ไปที่ ช่องใส่ใต้ Name เลือก เป็น msg.pyload และ เลือก timestamp
        (2). ตั้งให้ Repeat ตั้งค่าเป็น none
            - ไปที่ Repeat >> เลือก none 
    
![fig: ตั้งค่า inject node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677744974608_Untitled.png)



5. สร้าง debug node  
    - ไปที่แถบซ้ายมือ >> common >> เลือก debug node


![fig:  debug node](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674122277007_Screenshot+2023-01-19+165723.png)



6. ตั้งค่าให้แสดงค่า payload ที่เป็นค่า output จาก function node โดยดับเบิ้ลคลิ๊กที่ debug node 
    - ไปที่ Output >> ตั้งค่าเป็น msg.payload
    - ไปที่ To >> ตั้งค่า ให้ติ๊กถูก 3 ช่อง
    - ไปที่ Name >> ตั้งค่าเป็น “Debug Create CSV file”


![fig: Edit Debug Create node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677741433724_Untitled.png)




7. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกัน โดยเรียงลำดับดังภาพตัวอย่างนี้


![Fig: Example Create CSV file without header flow-node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677745211992_image.png)



8. คลิ๊กที่ Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้

**บันทึกผล: ภาพ flow node-red  ของตัวเองทั้งหมด**
 ****

----------

                                                               *รูปภาพ: Node-red flow*


----------

**บันทึกผล: ภาพรวมการทำงานทั้งระบบ และ แน็บไฟล์ csv. ที่เก็บข้อมูล ส่งใน classroom**

----------


                                                      *รูปภาพ: รวมการรันทั้งระบบ*



----------
----------
# **LAB 2: Create and Add header in CSV file**

   จากการทดลองนี้เป็นการเขียนโปรแกรม node-red โดยใช้ function node รับข้อมูลจาก msg.topic มาตั้งเป็นชื่อไฟล์ และใส่ ชื่อ header ลงไฟล์ csv  ทุกครั้งที่มีการสร้างไฟล์ใหม่ 


1. คัดลอก inject node, write file node และ debug node จาก LAB1 
2. ตั้งค่าให้ inject node เป็นตัวส่งข้อความไปยัง msg.topic และทำงานทุกครั้งเมื่อกดที่โหนด โดย ดับเบิ้ลคลิ๊กที่ inject node 
        (1). ไปที่ช่องใต้ Name เลือก เป็น msg.topic และ เลือก string ใส่ข้อความ “dataLAB2_รหัสนิสิต”
        (2). ตั้งให้ Repeat ตั้งค่าเป็น none
            - ไปที่ Repeat >> เลือก none 


![fig: Edit inject node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677749195708_Untitled.png)



3. ตั้งค่าให้ write file node สร้างไฟล์ตามค่าที่รับ จาก function node ตามข้อความใน msg.filename โดย ดับเบิ้ลคลิ๊กที่ node
    (1). ไปที่ Filename >> เลือก msg >> ใส่ “filename” 
    (2). ไปที่ Action >> เลือก “overwrite file” ให้เขียนข้อมูลทับข้อมูลเดิมถ้ามีอยู่แล้ว
        - ติ๊กทั้ง 2 ช่อง เพื่อ กำหนดให้ขึ้นบรรทัดใหม่ทุกครั้ง และ ถ้าไม่มี ไฟล์ ชื่อตามที่กำหนด ให้สร้างใหม่
    (3). ไปที่ Name >> ใส่ “write file”  


![fig: edit write file node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677750161913_Untitled.png)



4. ตั้งค่า debug node ให้แสดง output แบบ Object  โดยดับเบิ้ลคลิ๊กที่  debug node 
    - ไปที่ Output >> ตั้งค่าเป็น complete msg object
    - ไปที่ To >> ตั้งค่า ให้ติ๊กถูก 3 ช่อง
    - ไปที่ Name >> ตั้งค่าเป็น “Debug Create and Add Header”


![fig: Edit Debug Create and Add Header node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677748737447_Untitled.png)



5. สร้าง function node ขึ้นมา 1 node
    - ไปที่แถบซ้ายมือ >> function >> เลือก function node


![fig: function node](https://paper-attachments.dropboxusercontent.com/s_E52CE9636CC21E54CB784CCA8A27CB5635D96E67078036B8A8B926DABD6486D6_1675937730119_Screenshot+2023-02-09+171434.png)



6. เขียนโปรแกรมสำหรับรับค่า msg.topic มาเป็นชื่อไฟล์ และ ส่งข้อความ header สำหรับเป็นชื่อหัวตารางของไฟล์ CSV โดยดับเบิ้ลคลิ๊กที่ function node 
    - ไปที่ Properties >>ใส่ code ด้านล่างลงที่ช่อง On Message 


    // กำหนดตัวแปร filename โดยรับค่า msg.topic จาก inject node 
    var filename = "D:/data_logger/"+msg.topic+".csv" 
    // กำหนดตัวแปร headers มีค่าเป็นชุดข้อความ 
    var headers = "Date,Time,data1"
    // ส่งข้อมูล Output เป็น ชื่อไฟล์ และ ข้อความ header แบบ json  
    return {filename:filename,payload:headers}

   
  
  7. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกัน โดยเรียงลำดับดังภาพตัวอย่างนี้
   

![fig: Example Create file and add header](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677750416169_image.png)



8. คลิ๊กที่ Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้

**บันทึกผล: ภาพ flow node-red  ของตัวเองทั้งหมด**
 ****

----------

                                                               *รูปภาพ: Node-red flow*


----------

**บันทึกผล: ภาพรวมการทำงานทั้งระบบ และ แน็บไฟล์ csv. ที่เก็บข้อมูล ส่งใน classroom**

----------


                                                      *รูปภาพ: รวมการรันทั้งระบบ*


----------
## **แบบฝึกหัดที่ 1**
1. จงเขียนโปรแกรม node-red สร้างไฟล์ 3 ไฟล์ ชื่อว่า “data(1 ถึง 3)_รหัสนิสิต.csv” อยู่ใน folder ชื่อว่า “lab2_2” และแต่ละไฟล์มี header มี 4 column ชื่อดังนี้ 
    - date
    - time
    - data
2. จงเขียนโปรแกรม node-red ให้ทุก ๆ  10 วินาที เก็บค่าลงไฟล์ CSV  ชื่อว่า “data1_รหัสนิสิต.csv” ที่สร้างจากข้อ 1 โดยประกอบด้วยข้อมูลต่าง ๆ ดังนี้ 
    1. ที่ header ชื่อ date เก็บค่า วัน รูปแบบเป็น “YYYY/MM/DD” 
    2. ที่ header ชื่อ time เก็บค่า เวลา รูปแบบเป็น “้hh:mm:ss”
    3. ที่ header ชื่อ data เก็บค่า random 


----------
----------
# **LAB 3: Read CSV File** 
     จากการทดลองนี้เป็นการเขียนโปรแกรม node-red เพื่ออ่านข้อมูลจากไฟล์ CSV โดยใช้ read file node 

และ csv node ในการอ่านค่าจากไฟล์และแปลงข้อมูลจาก csv string เป็นรูปแบบ JavaScript object มาแสดงบน node-red ที่หน้า debug ทุกครั้งที่มีการกด inject node


1. download ไฟล์ >> [datatest_lab3.csv](https://drive.google.com/file/d/118cRqEhxF7FNR6RknIZ8_PSM2XsgH2kp/view?usp=share_link) ชุดข้อมูลสำหรับการทดลองนี้ไปไว้ใน folder ชื่อว่า “datalog_รหัสนิสิต” ของตนเอง
2. สร้าง inject node จำนวน 1 node
3. ตั้งค่าให้ inject node  ที่ Repeat ตั้งค่าเป็น none และคลิ๊ก Done


![fig: edit inject node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677814821072_Untitled.png)



4. สร้าง Read file node 
    - ไปที่แถบซ้ายมือ >> storage >> เลือก read file node
    
![fig: read file node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677814930672_image.png)

5. ตั้งค่า read file node ดังนี้
    (1). ไปที่ Filename >>เลือก path >> ใส่ที่อยู่ของไฟล์ที่ download จากขั้นตอนที่ 1 และตามด้วยชื่อไฟล์นั้น
    (2). ไปที่ Output >> เลือก “a sing utf8 string” และคลิ๊ก Done


![fig: edit read file node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677815923966_Untitled.png)

6. สร้าง csv node สำหรับแปลงข้อมูลจากไฟล์ csv 
    - ไปที่แถบซ้ายมือ >> parser >> เลือก csv node
    
![fig: csv node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677821213764_image.png)



7. ตั้งค่า csv node ดังนี้ 
    (1). ไปที่ Columns >>ใส่ “Date,Time,Temperature” (เป็นชื่อ columnsหรือheaderไฟล์ คั้นด้วย comma)
    (2). ไปที่ Separator
    (3). ไปที่ CSV to Object options >> Input >> ติ๊กเลือกสองช่องแรก
    (4). ไปที่ CSV to Object options >> Output >> a single message [array] (ต้องการแสดงข้อความแบบ array ที่ละช่อง)
    (5). ไปที่ Object to CSV options >> Output >> never send column headers
    (6). ไปที่ Object to CSV options >> Newline >> เลือก Windows (\r\n) 
    และคลิ๊ก Done
    
![fig: edit csv node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677819798965_Untitled.png)



8. ตั้งค่า debug node ให้แสดง output แบบ Object  โดยดับเบิ้ลคลิ๊กที่  debug node 
    - ไปที่ Output >> ตั้งค่าเป็น complete msg object
    - ไปที่ To >> ตั้งค่า ให้ติ๊กถูก 3 ช่อง
    - ไปที่ Name >> ตั้งค่าเป็น “Debug Read CSV file” และคลิ๊ก Done
    
![fig: Edit Debug Read CSV file](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677820036832_Untitled.png)



9. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกัน โดยเรียงลำดับดังภาพตัวอย่างนี้


![fig: Example Read csv file](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677820222573_image.png)




10. คลิ๊กที่ Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้

**บันทึกผล: ภาพ flow node-red  ของตัวเองพร้อมผลหน้า debug** 
 ****

----------

                                                               *รูปภาพ: Node-red flow*


----------
----------
# **LAB4:  Read CSV file and display on UI**
    จากการทดลองนี้เป็นการเขียนโปรแกรม node-red เพิ่มจากการทดลอง LAB3 เพื่อนำข้อมูลจาก CSV node 

มาแสดงบน Dashboard ของ node-red ในรูปแบบ ตาราง ทุกครั้งที่มีการกด inject node 


1. สร้าง table node 
    - ไปที่แถบซ้ายมือ >> dashboard >> เลือก table node


![fig: table node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677666145078_image.png)


****หมายเหตุ: ถ้า Dashboard ไม่มี lable ให้ติดตั้งเพิ่ม โดยไปที่ แถบสามขีดขวามือ >> palette >> ค้นหา “node-red-node-ui-table” >> install*

2. การตั้งค่า table node 
    - ตั้งชื่อ tab หรือชื่อ dashboard ที่ต้องการแสดง table 
        - ไปที่ Group >>คลิ๊กที่ ลูกศร >>Tab >> คลิ๊กที่ ลูกศร >>Name>> ใส่ “datalogger” และคลิ๊ก update 
    
![fig: edit name dashboard tab node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677821431174_Untitled.png)

    - กลับมาที่หน้าตั้งค่า table node 
        - ไปที่ Name >> ใส่ “Data from csv file”
        - ไปที่ Columns >> คลิ๊กที่ +add จำนวน 3 ครั้ง สำหรับกำหนดค่าแต่ละ olumn ที่ต้องการแสดงบน dashboard โดยให้ตั้งค่าตามภาพด้านล่าง และคลิ๊ก Done
        
![fig: edit table node](https://paper-attachments.dropboxusercontent.com/s_A5CBDACDEEDF14937D944AAF6AB4E2B261739094E752D1CB67AF30435F18B81F_1677821436132_Untitled_3.png)



9. เชื่อมต่อ table node เข้า csv node ของ LAB3 ที่ได้สร้างก่อนหน้านี้
10. คลิ๊กที่ Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้

**บันทึกผล: ภาพ flow node-red  ของตัวเองพร้อมผลหน้า debug** 

----------

                                                               *รูปภาพ: Node-red flow*


----------

**บันทึกผล: ภาพหน้า Dashboard ที่แสดงข้อมูลที่ได้จากโปรแกรมนี้** 

----------


                                          *รูปภาพ: Node-red Dashboard* 
                                
----------


----------

 





