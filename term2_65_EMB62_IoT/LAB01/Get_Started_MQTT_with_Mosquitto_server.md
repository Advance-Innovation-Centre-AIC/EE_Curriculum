# Get Started MQTT with Mosquitto server 

# **Outline**

- [Setting is MQTT Broker](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB01/Get_Started_MQTT_with_Mosquitto_server.md#setting-is-mqtt-broker)

- [Example Test Mosquitto Broker](https://github.com/Advance-Innovation-Centre-AIC/EE_Curriculum/blob/main/term2_65_EMB62_IoT/LAB01/Get_Started_MQTT_with_Mosquitto_server.md#Example-Test-Mosquitto-Broker)



## **Setting is MQTT Broker** 


### **on windows**

1. Download และ ติดตั้ง  link: https://mosquitto.org/download/

2.  เปิด Command promp โดย ไปที่ Search >> พิมพ์ cmd >> เลือก Run as administrator

3.  หลังจากเปิด CMD tab ให้ตรวจสอบ IP คอมพิวเตอร์ของเรา โดยใช้คำสั่ง ipconfig และดูค่าIP Wi-Fi ที่ IPv4 Address แล้วจดบันทึกไว้
    ipconfig


![](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674188850961_Screenshot+2023-01-20+112628.png)



4. เข้าไปในโฟล์เดอร์ mosquitto ตาม path ที่เราติดตั้งโปรแกรม โดยใช้คำสั่ง cd 
  
```  
    cd C:\Program Files\mosquitto
```

5. ใช้คำสั่ง echo ใส่ข้อมูลการตั้งค่าดังนี้

    - mosquitto broker เป็น port 1883 (default port)
    
```
    echo listener 1883 >>mosquitto.conf
```  

   - ตั้งค่า อนุญาติให้ client เชื่อมต่อโดยไม่ต้องระบุ username หรือ password
   
```  
  echo allow_anonymous true >>mosquitto.conf
```

6. ตรวจสอบข้อมูลที่อยู่ใน mosquitto.conf ไฟล์ว่าตรงตามที่ต้องการหรือไม่ โดยใช้คำสั่ง type
    type mosquitto.conf


![Fig: Display the contents of the mosquitto.conf file.](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674112199305_Screenshot+2023-01-19+140814.png)



## **Example** **Test Mosquitto Broker**

### **Run Mosquitto Broker**


1. เปิด Command promp โดย ไปที่ Search >> พิมพ์ cmd >> เลือก Run as administrator

2. เข้าไปในโฟล์เดอร์ mosquitto ตาม path ที่เราติดตั้งโปรแกรม โดยใช้คำสั่ง cd

```
    cd C:\Program Files\mosquitto
```


3. Run Mosquitto Broker โดยคำสั่ง -v เพื่อแสดงข้อมูลการทำงานของ broker และใช้คำสั่ง -c เพื่อใช้งานการ

ตั้งค่าตาม mosquitto.conf 


```
    mosquitto -v -c mosquitto.conf
```
 
 
![Fig: Display run the Mosquitto MQTT broker with the specified configuration file](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674112995761_image.png)




### **Run  Subscribe client** 


1. เปิด tab command prompt ขึ้นมาใหม่ 1 tab ให้เข้าไปในโฟล์เดอร์ mosquitto ตาม path ที่เราติดตั้งโปรแกรม โดยใช้คำสั่ง cd 
 
```
    cd C:\Program Files\mosquitto
```

2. พิมพ์คำสั่งกำหนดให้ tab นี้ทำหน้าที่เป็น subscribe 
    
    - โดยมี topic เท่ากับ “test” ติดต่อกันผ่าน mosquitto Broker ใส่เลข ip Broker ตามขั้นตอนที่ 3 ของ Setting is MQTT Broker

Example run command line on Command prompt

```
    # mosquitto_sub -h [hostname or IP] -t test
    # Example broker ip 192.168.101.245
    mosquitto_sub -h 192.168.101.245 -t test
```


![Fig: Display is information of mosquitto broker than  mosquitto_sub (Client) connected.](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674114180482_image.png)


### **Run  Publish client** 

1. เปิด tab command prompt มาใหม่อีกหนึ่ง tab ให้เข้าไปในโฟล์เดอร์ mosquitto ตาม path ที่เราติดตั้งโปรแกรม โดยใช้คำสั่ง cd 


```
    cd C:\Program Files\mosquitto

```

2. พิมพ์คำสั่งกำหนดให้ tab นี้ทำหน้าที่เป็น publish client
 
    - โดยส่งข้อความ “Hello !!” ใน topic เท่ากับ “test” ผ่าน Mosquitto Broker เดียวกันกับ Subscribe client 


```
    # mosquitto_pub -h [hostname or IP] -t test -m "Hello!!"
    mosquitto_pub -h 192.168.101.245 -t test -m "Hello!!"
```


![Fig: Display Result run Broker, subscribe client and publish client of Mosquitto](https://paper-attachments.dropboxusercontent.com/s_7788A459FC6A88558CA5CA14FB949EF0AF66791C1E6DA46173C45740A9B53F44_1674114766410_image.png)




----------

[1]Ref: [https://youtu.be/DH-VSAACtBk](https://youtu.be/DH-VSAACtBk)


