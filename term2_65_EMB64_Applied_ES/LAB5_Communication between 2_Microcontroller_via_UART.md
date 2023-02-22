# LAB5: Communication between 2 Microcontroller via UART

# **จุดประสงค์**
1. สามารถต่อใช้งาน UART ของบอร์ดที่กำหนดมาให้ได้
2. สามารถเขียนโปรแกรมใช้งาน UART สื่อสารกันระหว่างบอร์ดสองบอร์ดได้
3. สามารถเขียนโปรแกรมกำหนดให้บอร์ดหนึ่งส่งข้อมูลไปยังอีกบอร์ดหนึ่ง เพื่อควบคุมอุปกรณ์ผ่านขา I/O ได้ 


# **LAB1: Send Message between 2 Boards using UART** 

     ทดลองเขียนโปรแกรมส่งข้อความผ่านขา serial ระหว่าง 2 บอร์ด ที่ทำหน้าที่เป็น Master และ Slave

## **อุปกรณ์ทดลอง**
| **Name**               | **Quantity** | **Component**  |
| ---------------------- | ------------ | -------------- |
| U1_Master,<br>U2_Slave | 2            | Arduino Uno R3 |

## **โปรแกรม**
1. Arduino IDE หรือ www.tinkercad.com(Circuits)
## **Schematic**
![Figure: Master board send message to Slave board using UART](https://paper-attachments.dropboxusercontent.com/s_8ED121AA1AA7529CE40378D1CCA59E33B5AED484D19F6E657B52202571A1D8ED_1671535813674_image.png)


**Code Master** 


    //Sender Arduino Board Code (Master)
    char mystring[20] = "\rLinuxHint.com\n"; //String data which is to be sent
    void setup() {                
     Serial.begin(9600);                  // Begin the Serial at 9600 Baud rate
    }
    void loop() {
     Serial.write(mystring,15);             //Write the serial data
     delay(1000);
    }


**Code slave**

    
    //Receiver Arduino Board Code (Slave)
    char mystring[30];               //Initialized variable to store receive
    void setup() {
     Serial.begin(9600);             // Begin the Serial at 9600 Baud
    }
    void loop() {
     Serial.readBytes(mystring,15);  //Read the serial data
     Serial.println(mystring);       //Print data on Serial Monitor
     Serial.println(" RECEIVER");
     delay(1000);    
    }


## **บันทึกผลการทดลอง**
1. บันทึกขั้นตอนการทดลอง
2. บันทึกภาพการเชื่อมต่อวงจร (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม


----------
# **LAB2: Blink LED Using Two Boards through UART Communication**

 ทดลองเขียนโปรแกรมให้บอร์ด Master ส่งค่า on/off ผ่าน UART เพื่อควบคุม LED ของบอร์ด Slave

## **อุปกรณ์ทดลอง**
| **Name**               | **Quantity** | **Component**  |
| ---------------------- | ------------ | -------------- |
| U1_Master,<br>U2_Slave | 2            | Arduino Uno R3 |
| R1                     | 1            | 220 Ω Resistor |
| D1                     | 1            | Red LED        |



## **โปรแกรม**
1. Arduino IDE หรือ www.tinkercad.com(Circuits)
## **Schematic**
![Figure: Master board control LED of Slave board using UART](https://paper-attachments.dropboxusercontent.com/s_8ED121AA1AA7529CE40378D1CCA59E33B5AED484D19F6E657B52202571A1D8ED_1671536031321_image.png)


**Code Master** 


    //Transmitter (Tx)Arduino UNO Board Code
    //use pin T0,R0
    
    void setup()
    {
      Serial.begin(9600);
    }
    void loop()
    {
      Serial.println(1);
      delay(2000);
      Serial.println(0);
      delay(2000);
    }


**Code slave**

    //Receiver (Rx) Aduino uno Board Code
    // use pin 1<-Tx , 0->Rx
    char serialinput  = ' ';
    byte LED = 2;
     
    void setup()
    {
       pinMode(LED, OUTPUT);
       Serial.begin(9600);
    }
    void loop()
    {
       if(Serial.available()) 
       {
          char serialinput = Serial.read();
          if (serialinput =='0') { digitalWrite(LED, LOW); }
          if (serialinput =='1') { digitalWrite(LED, HIGH); }
          Serial.println(serialinput);
       }
    }


## **บันทึกผลการทดลอง**
1. บันทึกขั้นตอนการทดลอง
2. บันทึกภาพการเชื่อมต่อวงจร (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม


----------
# **LAB3: PushButton switch of Master control LED of Slave via UART**

ทดลองเขียนโปรแกรมให้บอร์ด Master รับค่าจาก PushButton แล้วส่งสถานะ ผ่าน UART เพื่อควบคุม LED ของบอร์ด Slave

## **อุปกรณ์ทดลอง**
| **Name**              | **Quantity** | **Component**  |
| --------------------- | ------------ | -------------- |
| U1_Master<br>U2_Slave | 2            | Arduino Uno R3 |
| R1                    | 1            | 220 Ω Resistor |
| D1                    | 1            | Red LED        |
| S1                    | 1            | Pushbutton     |



## **โปรแกรม**
1. Arduino IDE หรือ www.tinkercad.com(Circuits)
## **Schematic**
![Figure: Switch of Master board control LED of Slave board using UART](https://paper-attachments.dropboxusercontent.com/s_8ED121AA1AA7529CE40378D1CCA59E33B5AED484D19F6E657B52202571A1D8ED_1671592358783_image.png)


**Code Master** 

    // Master control Slave via UART(TX)
    const int Input_digital = 8; //set pin 8 to active
    void setup() {
    // put your setup code here, to run once:
    pinMode (Input_digital,INPUT_PULLUP); //set pin 8 as input
     Serial.begin(9600);
    }
    void loop() {
    int Input = 0;
    Input = digitalRead(Input_digital);
    Serial.print(Input);
    }

**Code Slave**

    //Receiver (Rx) Aduino uno Board Code
    // use pin 1<-Tx , 0->Rx
    char serialinput  = ' ';
    byte LED = 2;
     
    void setup()
    {
       pinMode(LED, OUTPUT);
       Serial.begin(9600);
    }
    void loop()
    {
       if(Serial.available()) 
       {
          char serialinput = Serial.read();
          if (serialinput =='1') { digitalWrite(LED, LOW); }
          if (serialinput =='0') { digitalWrite(LED, HIGH); }
          Serial.println(serialinput);
       }
    }


## **บันทึกผลการทดลอง**
1. บันทึกขั้นตอนการทดลอง
2. บันทึกภาพการเชื่อมต่อวงจร (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม


----------

[1] Ref[.](https://linuxhint.com/serial-uart-communication-between-two-arduino/) [https://linuxhint.com](https://linuxhint.com/serial-uart-communication-between-two-arduino/)
[2] Ref. [https://docs.arduino.cc](https://docs.arduino.cc/tutorials/nano-every/uart#goals)
[3] Ref. https://store.arduino.cc/products/arduino-uno-rev3?queryID=undefined
[4] Ref. https://www.arduino.cc/reference/en/language/functions/communication/serial/


