# Writing a Function on Node-red 

# **Function node**

Node-red สามารถเขียนโค้ด JavaScript ลง Function node ได้ โดยสามารถเรียกข้อความจาก function node ที่ return ค่า msg ออกมา ซึ่งเป็น Object และสามารถรับข้อมูลเข้ามายัง function  ผ่าน (property) payload ได้


    


![figure: function node](https://paper-attachments.dropboxusercontent.com/s_D6E777D64AB0565D21DA2F2CD1630EFB1438E09DA100CCDDB8F0352EF928A459_1670816077975_image.png)



## **Writing a Function**

การใส่ข้อมูลลง msg และ return ค่าออกจาก function node


    msg.payload = '123';
    return msg;


![Figure: Show debug Writing a Function flow](https://paper-attachments.dropboxusercontent.com/s_4B538F09C5D886BC9475F751A0B960F29C520192BAC17CD867EC4ADD224AEFDA_1670836581577_image.png)




## **Multiple Outputs**

function node ใส่เงื่อนไขสำหรับการรับและส่งออกแบบมากกว่า 1 Output 

    if (msg.topic === "banana") {
       return [ null, msg ];
    } else {
       return [ msg, null ];
    }

กำหนดให้ ถ้า msg.topic คือคำว่า banana ให้ แสดง msg ที่ output 2 แต่ถ้า ไม่ใช่ให้แสดง msg ที่ output 1


![Figure: Show debug Multiple Outputs flow](https://paper-attachments.dropboxusercontent.com/s_4B538F09C5D886BC9475F751A0B960F29C520192BAC17CD867EC4ADD224AEFDA_1670842106405_image.png)




## **Multiple Messages**

function code สำหรับ return มากกว่า 1 msg และ ตั้งค่า เป็น 2 Output 

    var msg1 = { payload:"first out of output 1" };
    var msg2 = { payload:"second out of output 1" };
    var msg3 = { payload:"third out of output 1" };
    var msg4 = { payload:"only message from output 2" };
    return [ [ msg1, msg2, msg3 ], msg4 ];



![Figure: Show debug Multiple Messages flow](https://paper-attachments.dropboxusercontent.com/s_4B538F09C5D886BC9475F751A0B960F29C520192BAC17CD867EC4ADD224AEFDA_1670834211562_image.png)


[1] Ref. [www. nodered.org](https://nodered.org/docs/user-guide/writing-functions)
























