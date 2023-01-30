# Timestamp with Nod-red

      สำหรับ javascript จะใช้ new date () ในการใช้งานคำสั่งเกี่ยวกับ วันและเวลา ซึ่งชื่อ Methods ต่าง ๆ ในการเรียกใช้สามารถดูได้ตามลิ้ง [[1]](https://www.w3schools.com/jsref/jsref_obj_date.asp)

    Timestamp node ของ Node-red จะแสดงค่าเป็นคือ millisecond ซึ่งเริ่มต้นนับจาก 00:00:00 UTC on 

January 1, 1970 ถ้าเราต้องการให้แสดงค่า เป็นวันเวลาในรูปแบบที่เราเข้าใจ เราจะต้องเขียน function node สำหรับแปรข้อความเพิ่ม [2]



![Figure : ตัวอย่าง debug วัน node-red](https://paper-attachments.dropboxusercontent.com/s_4B538F09C5D886BC9475F751A0B960F29C520192BAC17CD867EC4ADD224AEFDA_1670825688161_image.png)



## **Format Date**

จาก function node ด้านล่าง ใช้ตัวแปร date ในการกำหนดรูปแบบ การแสดงค่า วันแบบ YYYY/MM/DD

    var t = new Date();
    var date = t.getFullYear() 
               + "/" + (t.getMonth() + 1) 
               + "/" + t.getDate();
               + "/" + t.getDay();
               
    msg.payload = date;
    return msg;



## **Format Time**

จาก function node ด้านล่าง ใช้ตัวแปร time ในการกำหนดรูปแบบ การแสดงค่า วันแบบ hh:mm:ss

    var t = new Date();
    var time = t.getHours() + ":" 
             + t.getMinutes() + ":" 
             + t.getSeconds();
            
    msg.payload = time;
    return msg;



# **Example** 

การแสดงค่า timestamp และค่า random 2 ค่า 

function node

    var t = new Date(); 
    var timestemp = t.getFullYear()+"/"+(t.getMonth()+1)+"/"+t.getDate()
                    +","+t.getHours()+":"+t.getMinutes()+":"+t.getSeconds();
    
    var temp = Math.round(Math.random() * 100);
    var humi = Math.round(Math.random() * 100);
    
    var data = timestemp + "," + temp + "," + humi 
                         +"," + temp + "," + humi;
                         
    msg.payload = data;
    return msg;

output ที่ได้จะได้ชุดข้อมูลที่เป็น string ต่อกันโดยขั้นด้วย comma สามารถนำไปประยุกต์ใช้กับการเก็บข้อมูลลง ไฟล์ csv พร้อมค่าเวลาได้


![](https://paper-attachments.dropboxusercontent.com/s_4B538F09C5D886BC9475F751A0B960F29C520192BAC17CD867EC4ADD224AEFDA_1670830322212_image.png)





[1] Ref. https://www.w3schools.com/jsref/jsref_obj_date.asp]
[2] Ref.[www.Automation 360](https://automation360blog.wordpress.com/2019/09/18/node-red_date_time/)]


----------

