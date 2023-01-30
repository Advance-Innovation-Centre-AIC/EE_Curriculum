# **EMB-62-IoT**

## **Outline** 


***Final part***

1. node-red อ่าน data from nodemcu via MQTT protocol
    - ใช้ nodeMCU เป็นตัวอ่าน data แล้วสตรีมข้อมูลขึ้นไปยัง MQTT
    - ใช้ rpi/labtop ติดตั้ง node-red เพื่อ subscribe topic นั้นๆ
2. node-red เก็บค่า data ลง csv file
    - ใช้ node-red สร้าง node สำหรับการทำ data logger
    - ใช้ node-red สร้าง Dashboard สำหรับแสดงข้อมูล
3. node-red เก็บค่า data ลง database
    - สร้าง SQL database
    - ใช้ node-red บันทึกค่าที่ได้รับจาก MQTT ลงใน database ที่สร้างขึ้น
4. การเตรียม Dataset
    - ทฤษฎีการทำ ML
    - การจัดเตรียมข้อมูลสำหรับ ML (Data cleansing, filling)
5. basic ML สำหรับ Industry
    - ตัวอย่าง ML ที่นำมาใช้ในการ classification สำหรับข้อมูลอุตสาหกรรมที่เป็น time-series
6. การแสดงผล Analytics
    - การทำ Visualization ข้อมูลด้วย tools ที่กำหนดให้

**เกณฑ์การให้คะแนน เต็ม 50%**

- Homework for Quiz [5%]
- Workshop [15%]
- Class [5%]
- Test Final [25%]

**เงื่อนไขการเข้าเรียน:**

1. ให้เข้าสายได้ไม่เกิน 10 นาทีเท่านั้น
2. ต้องมีสมุดจดโน้ตทุกคาบ (เพราะจะมีคะแนนจดบันทึกให้ด้วย)
3. ทุกคนจะต้องไปสร้างเอกสารใน Google Doc (@go.buu.ac.th) เพื่อสร้าง Technical Learning Report เพื่อใช้บันทึกงานทุกๆคาบโดยละเอียด
