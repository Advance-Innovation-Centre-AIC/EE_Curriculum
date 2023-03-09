# **Outline**
- [Overview](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB03/Lab_Node_red_with_SQLite.md#overview-%E0%B9%80%E0%B8%9E%E0%B8%B4%E0%B9%88%E0%B8%A1%E0%B9%80%E0%B8%95%E0%B8%B4%E0%B8%A1-lab-use-sqlite-database-with-node-red)

- [ติดตั้ง SQLite modules Node-Red](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB03/Lab_Node_red_with_SQLite.md#%E0%B8%95%E0%B8%B4%E0%B8%94%E0%B8%95%E0%B8%B1%E0%B9%89%E0%B8%87-sqlite-modules-node-red)

- [ขั้นตอนการทดลอง](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB03/Lab_Node_red_with_SQLite.md#%E0%B8%82%E0%B8%B1%E0%B9%89%E0%B8%99%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%97%E0%B8%94%E0%B8%A5%E0%B8%AD%E0%B8%87)


# **Overview (เพิ่มเติม) LAB: Use SQLite Database with Node-red**

 เราสามารถนำค่าที่อ่านได้ไปเก็บลง sqlite database ได้ โดยใช้ sqlite node  ในการเข้าถึง sqlite database และตั้งค่าลงพื้นที่ที่ต้องการเก็บข้อมูล


![รูปภาพ: sqlite node](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669257489613_image.png)


# **ติดตั้ง SQLite modules Node-Red**
1. ไปที่ Manage palette >>Install>> search modules >> พิมพ์ “Modbus” >>node-red-sqlite>> install
2. หลังจากติดตั้งเสร็จ สังเกต แถบทางซ้ายมือ >> Storage >> จะปรากฎ sqlite node สำหรับใช้งาน



![รูปภาพ: Install node-red-sqlite](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669175748274_file.png)



![รูปภาพ: sqlite node](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669175994590_file.png)



# **ขั้นตอนการทดลอง**

1. สร้าง node สำหรับ query ข้อมูลหลังจากที่เราเก็บลง database ไปที่แถบซ้ายมือ >> common >> เลือก inject node
2. ไปที่แถบซ้ายมือ >> storage >> เลือก sqilte node
3. ไปที่แถบซ้ายมือ >> common >> เลือก debug node สำหรับ การ sqite node
4. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกันตามภาพด้านล่าง


![รูปภาพ: node flow สำหรับ query data](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669284321153_image.png)



5. ตั้งค่า inject node  ตามภาพด้านล่าง


![รูปภาพ: Edit inject node](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669284346470_image.png)

6. เพื่อความสะดวกสำหรับการใช้คำสั่ง query ของ database ให้ใช้ inject node ในการใส่ คำสั่งที่จำเป็น ของ database และตั้งค่าต่างดังภาพด้านล่าง


![รูปภาพ: Edit CREATE node](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669176588760_image.png)


 CREATE

    CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT, temperature NUMERIC, humidity NUMERIC, currentdate DATE, currenttime TIME, device TEXT)


![รูปภาพ: Edit INSERTnode](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669176905927_image.png)


INSERT

    INSERT INTO data(temperature, humidity, currentdate, currenttime, device) values(22.4, 48, date('now'), time('now'), "manual")


![รูปภาพ: Edit SELECT  node](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669176994354_image.png)


SELECT 

    SELECT * FROM data


7. เชื่อมต่อ node ต่าง ๆ สำหรับการใช้งาน database เบื่องต้น เข้าด้วยกันตามภาพด้านล่าง


![รูปภาพ: Basic_SQLite flow](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669285856022_image.png)

8. คลิ๊ก Done และ Deploy เมื่อเราต้องการสร้างหรือเปลี่ยน table ของ database ก็สามารถทำได้โดยการเปลี่ยนที่ msg.topic ของ node ที่ต้องการแก้ไขนั้นได้

   การทดลองเขียนโปรแกรม node-red อ่านค่า Modbus เราสามารถนำค่าที่อ่านได้ไปเก็บลง sqlite database ได้ โดยใช้ sqlite node  ในการเข้าถึง sqlite database และตั้งค่าลงพื้นที่ที่ต้องการเก็บข้อมูล


1. ไปที่แถบซ้ายมือ >> common >> เลือก inject node
2. ไปที่แถบซ้ายมือ >> function >> เลือก function node
3. ไปที่แถบซ้ายมือ >> storage >> เลือก sqilte node
4. ไปที่แถบซ้ายมือ >> common >> เลือก debug node สำหรับ การ sqite node
5. เชื่อมต่อ node ต่าง ๆ เข้าด้วยกันตามภาพด้านล่าง


![รูปภาพ: Basic_SaveData_Sqlite flow](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669283472321_image.png)


 

6. ไปที่ fuction node และ โปรแกรมดังนี้

code 
```
    var newMsg={};
    
    var t = new Date();
    // var date = t.getFullYear() + "/" + (t.getMonth() + 1) + "/" + t.getDate();
    var timestamp = t.getHours() + ":" + t.getMinutes() + ":" + t.getSeconds();
    
    var temp = Math.round(Math.random() * 100); 
    var humi = Math.round(Math.random() * 100);
    
    var msg = "(temperature,humidity,currenttime) VALUES (" + temp + "," + humi + ",\"" + timestamp +"\")";
    
    var topic = "INSERT INTO data"+ msg;
    
    newMsg.topic = topic;
    return newMsg;
```   


7. ตั้งค่า sqlite file  ตามภาพด้านล่าง เพื่อกำหนด path เก็บข้อมูลที่ต้องการลง database


![รูปภาพ: Edit sqlite node](https://paper-attachments.dropboxusercontent.com/s_B3016295DF2DA47BC44487210D359337B3B06F4BFA89777BB9C2F7C20A1E2E08_1669283777216_image.png)



8. คลิ๊กที่ Done 


14. คลิ๊ก Done และ Deploy เพื่อให้ Node-red ทำงานตามโปรแกรมที่ได้ตั้งค่าไว้


บันทึกผลการทดลอง

----------




----------
----------

[1] Ref. https://accautomation.ca/node-red-sql-database-log-modbus-logging/

[2] Ref. https://github.com/mpolinowski/nodered-sqlite

