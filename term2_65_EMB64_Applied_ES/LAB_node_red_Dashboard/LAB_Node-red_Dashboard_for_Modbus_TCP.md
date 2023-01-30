# LAB: Node-red Dashboard for Modbus TCP

# **ติดตั้ง modules Dashboard Node-Red** 
1. ไปที่ Manage palette >>Install>> search modules >> พิมพ์ “Dashboard >> เลือก node-red-dashboard >> install


![รูปภาพ: install node-red-dashboard](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668755968870_file.png)



2. หลังจากติดตั้งเสร็จ สังเกตแถบทางซ้ายมือ จะปรากฎ dashboard node สำหรับใช้งาน


![รูปภาพ: dashboard node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668756487606_file.png)



# **การทดลองที่1:** 

ทดลองเขียน Node-red แสดงค่าที่อ่านจาก Modbus TCP/IP ข้อมูล Digital บน Dashboard แบบข้อความ

## **วัตถุประสงค์**
1. เพื่อเรียนรู้วิธีเขียนโปรแกรม Node-red แสดงค่าที่อ่านจาก Modbus TCP/IP บน Dashboard แบบข้อความ
## **อุปกรณ์ประกอบการทดลอง**
2. คอมพิวเตอร์
## **โปรแกรมประกอบการทดลอง**
1. Modbus slave tool 
2. Node-red
## **ขั้นตอนการทดลอง**

     จากการทดลองเขียนโปรแกรม node-red อ่านค่า Modbus เราสามารถนำค่าที่อ่านได้ไปแสดงโดยใช้ node dashboard ในการแสดงผลแบบต่าง ๆ ได้ ในที่นี้จะใช้ text node สำหรับใช้ แสดงข้อมูลที่เป็นข้อความ


![รูปภาพ: text node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668758369209_image.png)



1. ไปที่แถบซ้ายมือ >> funtion >> เลือก function node 
2. ไปที่แถบซ้ายมือ >> dashboard >> เลือก text node
3. เชื่อม modbus read ต่อ function node และ  text node ต่อจาก function node


![รูปภาพ: Basic-ui-textt-node flow](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668765407348_image.png)



4. ไปที่ edit function node >> On Message แล้วเขียน script ให้ส่งข้อมูล address ที่ 1 ชองข้อมูลที่อ่านได้จาก modbus read ดังนี้


    var msg1 = { payload: msg.payload[0] };
    return msg1;


![รูปภาพ: Edit function node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668757943325_image.png)



5. ไปที่ edit text node ตั้งค่าตามภาพด้านล่าง แล้วคลิ๊ก Done


![รูปภาพ: Edit text node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668761386668_image.png)



6. หลังจากตั้งค่า node ต่าง ๆ เรียบร้อยแล้วให้ กด “Deploy” 
7. เปิด แถบ Browser ขึ้นใหม่ แล้ว พิมพ์ ip address node-red ตาม ด้วย port:1880 และ /ui


    127.0.0.0.1:1880/ui
    or
    localhost:1880/ui


## **บันทึกผลการทดลอง**

…
…
…

# **แบบฝึกหัด**
1. ทดลองตั้งค่า Modbus read ให้เป็น function code แบบ 04 read/write register เพื่อแสดง

ค่า บน Dashboard แบบข้อความ


----------
# **การทดลองที่2:**

เขียน Node-red แสดงค่าที่อ่านจาก Modbus TCP/IP แสดงข้อมูล Analog บน Dashboard แบบ Chart

## **วัตถุประสงค์**
1. เพื่อเรียนรู้วิธีเขียนโปรแกรม Node-red แสดงค่าที่อ่านจาก Modbus TCP/IP บน Dashboard แบบ Chart
## **อุปกรณ์ประกอบการทดลอง**
1. คอมพิวเตอร์
## **โปรแกรมประกอบการทดลอง**
1. Modbus slave tool 
2. Node-red
## **ขั้นตอนการทดลอง**
    จากการทดลองเขียนโปรแกรม node-red อ่านค่า Modbus เราสามารถนำค่าที่อ่านได้ไปแสดงโดยใช้ 

node dashboard ในการแสดงผลแบบต่าง ๆ ได้ ในที่นี้จะใช้ chart node สำหรับใช้ แสดงข้อมูลเทียบกับเวลา


![รูปภาพ: chart node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668762063752_image.png)

1. สร้าง modbus read node และ fuction node ตามขั้นตอนจากการทดลองก่อนหน้านี้
2. ไปที่แถบซ้ายมือ dashboard >> เลือก chart node
3. เชื่อม modbus read ต่อ function node และ  chart node ต่อจาก function node


![รูปภาพ: Basic-ui-chart-node flow](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668765145355_image.png)



4. ตั้งค่า chart node ตามภาพด้านล่าง


![รูปภาพ: edit chart node](https://paper-attachments.dropboxusercontent.com/s_E1F4097AE86D6BC006BA3F68803FE6B26B34FEC61653B412A44A5B3B4028A764_1668762403927_image.png)



5. คลิ๊ก Done และ Deploy
6. ที่ไป Browser ui 


## **บันทึกผลการทดลอง**

…
…
…


# **แบบฝึกหัด**
1. **ทดลองเขียน function node แสดงส่งข้อมูล 2 outputs** 
2. **ตั้งค่า Chart node ให้แสดง 2 Output บน Chart  เดียวกัน**





