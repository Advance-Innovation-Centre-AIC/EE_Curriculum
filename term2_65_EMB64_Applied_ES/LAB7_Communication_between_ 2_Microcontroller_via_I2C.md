# LAB7: Communication between 2 Microcontroller via I2C

# **จุดประสงค์**
1. สามารถต่อใช้งาน I2C ของบอร์ดที่กำหนดมาให้ได้
2. สามารถเขียนโปรแกรมใช้งาน I2C สื่อสารกันระหว่างบอร์ดสองบอร์ดได้
3. สามารถเขียนโปรแกรมกำหนดให้บอร์ดหนึ่งส่งข้อมูลไปยังอีกบอร์ดหนึ่ง เพื่อควบคุมอุปกรณ์ผ่านขา I/O ได้ 


# **LAB01: Master read message from Slave using I2C**  ****

   ทดลองเขียนโปรแกรมส่งข้อความผ่านขา I2C ระหว่าง 2 บอร์ด ที่ทำหน้าที่เป็น Master และ Slave

## **อุปกรณ์ทดลอง**
| **Name**               | **Quantity** | **Component**  |
| ---------------------- | ------------ | -------------- |
| U1_Master,<br>U2_Slave | 2            | Arduino Uno R3 |

## **โปรแกรม**
1. Arduino IDE หรือ www.tinkercad.com(Circuits)
## **Schematic**


![](https://paper-attachments.dropboxusercontent.com/s_034D2B985EFD34AACD429E2256A3327F94460DD70092A24C6D41CA17BB3EDAA0_1672126448964_image.png)


**Code Master**

    // Master read massage 
    #include <Wire.h>
    
    void setup() {
      Wire.begin();           // Join I2C bus (address is optional for controller device)
      Serial.begin(9600);       // Start serial for output 
    }
    
    void loop() {
        Wire.requestFrom(8, 6);    // Request 6 bytes from slave device with address 8 
        while(Wire.available()) { // loop untill data is available
            char data = Wire.read();    // read a byte of data
            Serial.print(data);         // Print the data show on Serial monitor 
        }
        delay(500);
    }

**Code Slave**

    // Wire Slave Sender
    #include <Wire.h>
    
    void setup() {
      Wire.begin(8);        // join i2c bus with address 8
      Wire.onRequest(requestEvent); //  Wait request from Master device.
    }
    
    void loop() {
      delay(100);
    }
    // function that executes whenever data is requested by master
    // this function is registered as an event, see setup()
    void requestEvent() {
      Wire.write("hello "); // respond with message of 6 bytes
      // as expected by master
       
    }


## **บันทึกผลการทดลอง**
1. บันทึกขั้นตอนการทดลอง

 2.  ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม

3.  บันทึกภาพการเชื่อมต่อวงจร (Circuit)
![](/static/img/pixel.gif)

![](/static/img/pixel.gif)
![](/static/img/pixel.gif)

----------
# **LAB02: Master control LED of slave using I2C**  

     ทดลองเขียนโปรแกรมส่งข้อความผ่านขา I2C ระหว่าง 2 บอร์ด ที่ทำหน้าที่เป็น Master และ Slave

## **อุปกรณ์ทดลอง**
| **Name**               | **Quantity** | **Component**  |
| ---------------------- | ------------ | -------------- |
| U1_Master,<br>U2_Slave | 2            | Arduino Uno R3 |

## **โปรแกรม**
1. Arduino IDE หรือ www.tinkercad.com(Circuits)
## **Schematic**


![](https://paper-attachments.dropboxusercontent.com/s_034D2B985EFD34AACD429E2256A3327F94460DD70092A24C6D41CA17BB3EDAA0_1672126505754_image.png)


**Code Master**

    // Example Master code
    #include<Wire.h>
    int slave_add = 8; // 
    int x ;
    void setup() 
    {
      Wire.begin();           // Join I2C bus (address is optional for controller device)
      Serial.begin(9600);       // Start serial for output
    }
    
    void loop() 
    { 
      sendCommand(slave_add, 1); // send address and command to sendCommand function 
      delay(2000);    
      sendCommand(slave_add, 0); // send address and command to sendCommand function 
      delay(2000); 
    }
    
    
    void sendCommand(int address, int command){  
    Wire.beginTransmission(address); // start transmit to slave device   
      x = Wire.write(command); //  sends command to slave device 
      Serial.print(x); 
      Wire.endTransmission(); //  end the transmission
    }
    

**Code Slave**

    // Slave receiver
    #include <Wire.h>
    int Greed = 2;
    int Yellow = 3;
    int Red = 4;
    int x = 0;
    
    void setup() {
      Wire.begin(8);  // join i2c bus with address 8              
      Wire.onReceive(receiveEvent); // Wait receive data from Master device.
      Serial.begin(9600);
    
      pinMode(Greed, OUTPUT);
      pinMode(Yellow, OUTPUT);
      pinMode(Red, OUTPUT);
      
      digitalWrite(Greed,0);
      digitalWrite(Yellow,0);
      digitalWrite(Red,0);
      
    }
    
    void loop() {
      delay(1000);
      digitalWrite(Greed,x);
      delay(500);
      digitalWrite(Yellow,x);
      delay(500);
      digitalWrite(Red,x);
      
      delay(1000);
      digitalWrite(Red,x);
      delay(500);
      digitalWrite(Yellow,x);
      delay(500);
      digitalWrite(Greed,x);
    
    }
    
    void receiveEvent(int msg){ 
      x= Wire.read(); // // read a byte of data
      Serial.println(x);
     
    }


## **บันทึกผลการทดลอง**
1. บันทึกขั้นตอนการทดลอง
2. บันทึกภาพการเชื่อมต่อวงจร (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม


----------
# **LAB03: Master connect to 2 slaves**

ทดลองเขียนโปรแกรมส่งข้อความผ่านขา I2C ระหว่าง บอร์ ที่ทำหน้าที่เป็น Master และ 2 บอร์ดเป็น Slave

## **อุปกรณ์ทดลอง**
| Name                                  | Quantity | Component      |
| ------------------------------------- | -------- | -------------- |
| U1_Master,<br>U2_Slave1,<br>U3_Slave2 | 3        | Arduino Uno R3 |
| R1, R2, R3                            | 3        | 220 Ω Resistor |
| D1                                    | 1        | Green LED      |
| D2                                    | 1        | Yellow LED     |
| D3                                    | 1        | Red LED        |
| S1                                    | 1        | Slideswitch    |

![figure: Slideswitch of www.tinkercad.com](https://paper-attachments.dropboxusercontent.com/s_034D2B985EFD34AACD429E2256A3327F94460DD70092A24C6D41CA17BB3EDAA0_1672126799487_image.png)



## **โปรแกรม**
1. Arduino IDE หรือ www.tinkercad.com(Circuits)
## **Schematic**


![](https://paper-attachments.dropboxusercontent.com/s_034D2B985EFD34AACD429E2256A3327F94460DD70092A24C6D41CA17BB3EDAA0_1672126545743_image.png)


**Code Master**

    // Master 
    #include<Wire.h>
    int slave1 = 8;
    int slave2 = 9;
    int x ;
    
    void setup() 
    {
      Wire.begin();           // Join I2C bus (address is optional for controller device)
      Serial.begin(9600);       // Start serial for output 
    }
    
    void loop() 
    {
      Wire.requestFrom(slave2, 1); // Request a byte from slave2 device
      x= Wire.read(); // read data from slave2
     
      Wire.beginTransmission(slave1); //start transmit to slave1 device  
      Wire.write(x); // write data x to slave1 device
      Serial.print(x); 
      Wire.endTransmission(); // stop transmit to slave1 device  
      delay(2000); 
    }
    

**Code Slave1**

    // Slave 1 follow slave code Lab2 

**Code Slave2**

    #include <Wire.h>
    int button = 2;
    int msg = 0;
    
    void setup() {
      Wire.begin(9);    // join i2c bus with address 9             
      Wire.onRequest(requestEvent); //  Wait request from Master device.
      Serial.begin(9600);
      
      pinMode(button, INPUT_PULLUP);
    }
    
    void loop() {  
      msg = digitalRead(button);
      Serial.println(msg);
      
      delay(500);
      }
    
    void requestEvent(){
       Wire.write(msg); // respond with state button  
     
    }


## **บันทึกผลการทดลอง**
1. บันทึกขั้นตอนการทดลอง
2. บันทึกภาพการเชื่อมต่อวงจร (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม


----------

Ref. [https://www.arduino.cc/en/Reference/Wire](https://www.arduino.cc/en/Reference/Wire).

