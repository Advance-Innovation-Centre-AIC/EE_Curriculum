# LAB-Basic Digital and  Analog  I/O of Microcontroller

# **Outline**
- จุดประสงค์
- LAB1: Basic Digital Input/Output
- LAB2: Lab2: Basic Analog Input

อธิบายพื้นฐาน Digital กับ  Analog  : [link](https://docs.aic-eec.com/embedded-systems/hardware-and-firmware/lab1-oscilloscope/basic-digital-and-analog-i-o)

# **จุดประสงค์** 
1. สามารถต่อวงจรสำหรับรับและส่งข้อมูลแบบ Digital และ  Analog  ผ่านขา I/O ของ Embedded board ได้ 
2. เขียนโปรแกรมรับและส่งข้อมูล Digital และ  Analog  ผ่านขา I/O ของ Embedded board ได้

# **Lab1: Basic Digital Input/Output**

ทดลองเขียนโปรแกรมรับข้อมูลแบบดิจิตอลจาก button ผ่านขา Input และส่งข้อมูลแบบดิจิตอลเพื่อควบคุม LED ผ่านขา Output ของ Aduino Uno R3

## **อุปกรณ์ทดลอง** 
| Arduino Uno R3 | 1            |
| -------------- | ------------ |
| Pushbutton     | 1            |
| **Component**  | **Quantity** |
| 220Ω Resistor  | 1            |
| Red LED        | 1            |

## **Schematic** 
![](https://paper-attachments.dropboxusercontent.com/s_F84F01DD9F719107CBC0632F893B1C6CC0705268D31C8BB1AAA955EA7694C945_1634474556222_inputPullupSerial_sch.png)

## **Code**
    // Lab1-3: Basic Digital Input/Output
    void setup() {
      //start serial connection
    ⑥  Serial.begin(9600);
      //configure pin 2 as an input and enable the internal pull-up resistor
      pinMode(2, INPUT_PULLUP);
      pinMode(13, OUTPUT);
    }
    
    void loop() {
      //read the pushbutton value into a variable
      int sensorVal = digitalRead(2);
      //print out the value of the pushbutton
      Serial.println(sensorVal);
    
      // Keep in mind the pull-up means the pushbutton's logic is inverted. It goes
      // HIGH when it's open, and LOW when it's pressed. Turn on pin 13 when the
      // button's pressed, and off when it's not:
      if (sensorVal == HIGH) {
        digitalWrite(13, LOW);
      } else {
        digitalWrite(13, HIGH);
      }
    }


## **บันทึกผลการทดลอง** 
1. ขั้นตอนการทดลอง
2. ภาพการเชื่อมต่อขาระหว่างอุปกรณ์ (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม


# **Lab2: Basic Analog Input**

ทดลองเขียนโปรแกรมรับข้อมูลแบบ  Analog  จากตัวต้านทานปรับค่าได้ (Potentiometer) ผ่านขา input ของ Aduino Uno R3

## **อุปกรณ์ทดลอง** 
| **Component**       | **Quantity** |
| ------------------- | ------------ |
| Arduino Uno R3      | 2            |
| 10 kΩ Potentiometer | 1            |
| Photoresistor       | 1            |
| 10 kΩ Resistor      | 1            |

## **Schematic** 


![Potentiometer https://www.arduino.cc/en/Tutorial/BuiltInExamples/ Analog Input](https://paper-attachments.dropboxusercontent.com/s_F84F01DD9F719107CBC0632F893B1C6CC0705268D31C8BB1AAA955EA7694C945_1634400356306_analoginoutserial_sch.png)
![Photoresistor https://www.arduino.cc/en/Tutorial/BuiltInExamples/ Analog Input](https://paper-attachments.dropboxusercontent.com/s_F84F01DD9F719107CBC0632F893B1C6CC0705268D31C8BB1AAA955EA7694C945_1634400365185_PhotoResistorA0_schem.png)




## code
    // Lab2-1: Basic  Analog  Input
    int sensorPin = A0;    // connect this pin to potentiometer
    int sensorValue = 0;  // variable to store the value coming from the sensor
    
    void setup() {
      pinMode(sensorPin, INPUT); 
      Serial.begin(9600); // start serial monitor
    }
    
    void loop() {
      // read the value from the sensor:
      sensorValue = analog Read(sensorPin); 
      Serial.println(sensorValue);
      // stop the program for <sensorValue> milliseconds:
      delay(sensorValue);
    }
## **บันทึกผลการทดลอง**
1. ขั้นตอนการทดลอง
2. ภาพการเชื่อมต่อขาระหว่างอุปกรณ์ (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม

----------

# **Lab3: Basic Analog Output**

ทดลองเขียนโปรแกรมรับข้อมูลแบบ Analog จากตัวต้านทานปรับค่าได้ (Potentiometer) ผ่านขา input และส่งข้อมูลแบบ Analog เพื่อควบคุม LED ผ่านขา Output ของ Arduino Uno R3

## **อุปกรณ์ทดลอง** 

| **Component**  | **Quantity** |
| -------------- | ------------ |
| Arduino Uno R3 | 1            |
| Photoresistor  | 1            |
| 10 kΩ Resistor | 1            |
| Red LED        | 1            |
| 220Ω Resistor  | 1            |



## **Schematic** 


![Schematic Basic Analog Output](https://paper-attachments.dropboxusercontent.com/s_F84F01DD9F719107CBC0632F893B1C6CC0705268D31C8BB1AAA955EA7694C945_1634475487274_lab5.png)



### code
     // Lab3: Basic  Analog  Output
    int sensorPin = A0;   --------------------------------------------------- // connect this pin to potentiometer
    int ledPin = 9;      // connect this pin to external LED
    int sensorValue = 0;  // variable to store the value coming from the sensor
    
    void setup() {
      // declare the ledPin as an OUTPUT:
      pinMode(ledPin, OUTPUT); // set this pin to output
      Serial.begin(9600); // start serial monitor
    }
    
    void loop() {
      // read the value from the sensor:
      sensorValue =  Analog Read(sensorPin);
      sensorValue = map(sensorValue, 0,1023,0,255);
      // turn the ledPin on
       Analog Write(ledPin, sensorValue);
      Serial.println(sensorValue); // bright LED with read value
       
    }


## **บันทึกผลการทดลอง** 
1. ขั้นตอนการทดลอง
2. ภาพการเชื่อมต่อขาระหว่างอุปกรณ์ (Circuit)
3. ค้นหาข้อมูลและอธิบายหลักการทำงานของโปรแกรม

