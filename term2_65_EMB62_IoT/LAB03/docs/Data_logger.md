# Data logger

# **Data Logger คืออะไร**
    Data logger เป็นอุปกรณ์สำหรับบันทึกข้อมูลเซนเซอร์พร้อมกับค่าเวลาจริงที่รับค่าจากเซนเซอร์ หลักการ

ทำงานของ data logger จะเป็นการรับค่าสัญญาณ analog จากเซนเซอร์มาแปลงเป็นข้อมูล digital แล้วเก็บเป็นชุดข้อมูลที่ประกอบด้วย ค่าเซนเซอร์ และเวลาที่ได้รับค่าเซนเซอร์ มาเก็บไว้ในหน่วยความจำ สำหรับ data logger จะมีทั้งเป็นอุปกรณ์สำเร็จรูปที่มาพร้อมกับเซนเซอร์ โดยสามารถวัดค่าเซนเซอร์และเก็บข้อมูลได้ในตัว หรือเราสามารถสร้าง data logger ได้โดยใช้บอร์ดสมองกลฝั่งตัวในการเขียนโปรแกรมให้อ่านค่าเซนเซอร์และเวลา บันทึกลงไฟล์ต่าง ๆ เช่น .txt .csv .json หรือ ใช้ database ในการเก็บข้อมูล




![Figure: อุปกรณ์ Data logger](https://paper-attachments.dropboxusercontent.com/s_D6E777D64AB0565D21DA2F2CD1630EFB1438E09DA100CCDDB8F0352EF928A459_1670558717571_data-logger.webp)


[1]


![figure: Text file icon](https://paper-attachments.dropboxusercontent.com/s_D6E777D64AB0565D21DA2F2CD1630EFB1438E09DA100CCDDB8F0352EF928A459_1670559577053_tex-file-format-symbol.png)
![figure: CSV file icon](https://paper-attachments.dropboxusercontent.com/s_D6E777D64AB0565D21DA2F2CD1630EFB1438E09DA100CCDDB8F0352EF928A459_1670559589850_Pngtreecsv+file+document+icon_4175842.png)
![figure: JSON file icon](https://paper-attachments.dropboxusercontent.com/s_D6E777D64AB0565D21DA2F2CD1630EFB1438E09DA100CCDDB8F0352EF928A459_1670559589859_Pngtreejson+file+document+icon_4172477.png)




## **ประโยชน์ของ Data Logger**
    เครื่องคอมพิวเตอร์ หรือ บอร์ดสมองกลฝั่งตัว (Embedded boards) สามารถอ่านข้อมูลจาก data logger เพื่อ

นำไปใช้งานต่าง ๆ เช่น การแสดงกราฟข้อมูลเซนเซอร์ในแต่ละช่วงเวลา หรือการนำข้อมูลไปวิเคราะห์เปรียบเทียบข้อมูลแต่ละช่วงเวลา( time series) เป็นต้น


## **Timestamp**
    เป็นค่าเวลาที่จะจดบันทึกพร้อมกับข้อมูลที่ได้รับมา สำหรับนำไปใช้ในการนำเสนอในรูปแบบข้อมูลของกราฟที่

เป็น time series หรือการทำไปวิเคราะห์ข้อมูล คาดการณ์สถานการณ์ต่าง ๆ เช่น เครื่องจักรทำงานผิดปกติ


## **What is a CSV File?** 

        CSV หรือชื่อเต็มว่า “Comma Separated Values”  เป็นรูปแบบอย่างง่ายในการเก็บข้อมูลลงตารางโดยไฟล์ csv จะใช้ comma เป็นตัวแยกข้อมูลออกเป็น column ซึ่งง่ายสำหรับการแยกข้อมูลและนำไปใช้ในการแสดงผลแบบกราฟหรือการวิเคราะห์ข้อมูล 


![figure: csv file](https://paper-attachments.dropboxusercontent.com/s_D6E777D64AB0565D21DA2F2CD1630EFB1438E09DA100CCDDB8F0352EF928A459_1670557220138_image.png)
![figure: show grap on csv file](https://paper-attachments.dropboxusercontent.com/s_D6E777D64AB0565D21DA2F2CD1630EFB1438E09DA100CCDDB8F0352EF928A459_1670561915095_Node-RED-Simple-Click-Data-Logging-520-min.webp)


[2]




[1] Ref. https://www.neonics.co.th
[2] Ref. [https://accautomation.ca](https://accautomation.ca/simple-click-data-logging-node-red/)



----------

