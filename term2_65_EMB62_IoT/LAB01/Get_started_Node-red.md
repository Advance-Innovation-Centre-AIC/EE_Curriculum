# Get started Node-red 

## **Outline**

- ตั้งค่า Node-red บน Windows

- ตั้งค่า Node-red บน RaspberryPi



# **ตั้งค่า Node-red บน Windows**
1. Download และ ติดตั้ง Nodejs ที่เว็บไซต์ [Node.js](https://nodejs.org/en/)


![รูปภาพ: Website Node.js](https://paper-attachments.dropboxusercontent.com/s_EAE347BCB7B527CA2156619BD46DF2D9708CD446BDA75189903AABB7E89CF529_1668742701228_file.png)

2. เปิด Command Pronpm --versionmp โดยไปที่ Start>>พิมพ์ CMD ในช่องค้นหา
3. ตรวจสอบ version ของ node.js และ npm ที่ได้ติดตั้งไปก่อนหน้า โดยพิมพ์คำสั่ง ดังนี้

```
    node --version
    npm --version
```   
    
## 
![รูปภาพ: CMD แสดง  node.js และ npm version บน windows](https://paper-attachments.dropboxusercontent.com/s_EAE347BCB7B527CA2156619BD46DF2D9708CD446BDA75189903AABB7E89CF529_1668744508638_file.png)


ติดตั้ง node-red โดย พิมพ์คำสั่ง ติดตั้งด้วย npm ดังนี้


     npm install -g --unsafe-perm node-red


4. เมื่อติดตั้ง node-red ให้ปิด หน้าต่าง Commade Promp แล้วเปิดใหม่ 
5. พิมพ์ คำสั่ง เปิดใช้งาน node-red ดังนี้

```
    node-red start 
```

หลังจาก Run Node-red แล้ว เราสามารถใช้งาน node-red  โดยไปที่หน้าเบราเซอร์ของคอมพิวเตอร์เรา พิมพ์ IP 127.0.0.1 หรือ คำว่า “localhost”  ตามด้วย port 1880 ดังตัวอย่าง ด้านล่าง


    http://127.0.0.1:1880
    or
    http://localhost:1880



![รูปภาพ: ตัวอย่าง Browser Node-red](https://paper-attachments.dropboxusercontent.com/s_EAE347BCB7B527CA2156619BD46DF2D9708CD446BDA75189903AABB7E89CF529_1668745390560_file.png)



# **ตั้งค่า Node-red บน RaspberryPi**

1. สำหรับใช้งาน node-red บน Respberry Pi สามารถใช้ สคริปที่ node-red เตรียมให้ ดังนี้

    ```
    bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
    ```


![รูปภาพ: terminal แสดงการติดตั้งโปรแกรมสำหรับใช้งาน Node-red](https://paper-attachments.dropboxusercontent.com/s_5931C85939E77FD48CAE3A71450F98024B4F088C5796C975D6067813D61AA140_1623228230189_Screenshot+from+2021-06-09+15-43-33.png)


2. ใส่คำสั่ง สำหรับ Run Node-red ดังนี้

    ```
    node-red start
    ```

3. หลังจาก Run Node-red แล้ว เราสามารถเข้าหน้าเบราเซอร์บนคอมพิวเตอร์ของเรา ผ่าน IP address  ของ Respberry Pi และ ตามด้วย port 1880

```
    http://<IP address of RespberryPi>:1880
```

