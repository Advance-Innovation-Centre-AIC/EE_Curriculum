# -*- coding: utf-8 -*-
"""
Notifications
-------------
Example showing how to add notifications to a characteristic and handle the responses.
Updated on 2019-07-03 by hbldh <henrik.blidh@gmail.com>
"""
 
#from ctypes import HRESULT
import sys
import asyncio
import platform
import numpy as np
from struct import *
from bleak import BleakClient
import time
from datetime import datetime
 
datetime_format = r"%m/%d/%Y %H:%M:%S:%f"
 
f = open("datalogble.txt", "a")
# you can change these to match your device or override them from the command line
CHARACTERISTIC_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E" #
ADDRESS = (
    "F3:1C:83:D2:E7:8B" # watches' MAC addr
    #"8C:C6:81:19:93:B1"
    if platform.system() != "Darwin"
    else "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
)
 
 
def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    #print("{0}: {1}".format(sender, data))
    #print(data[0])
 
    if data[0] == 0xFF:
        pass
    
        seq_number  = (data[2]<<8) | data[1]
        acc_x       = np.int16( (data[4]<<8) | data[3] )
        acc_y       = np.int16( (data[6]<<8) | data[5] )
        acc_z       = np.int16( (data[8]<<8) | data[7] )
        gyro_x      = np.int16( (data[10]<<8) | data[9] )
        gyro_y      = np.int16( (data[12]<<8) | data[11] )
        gyro_z      = np.int16( (data[14]<<8) | data[13] )
        air_pressure = unpack('<f', data[15:19])
        time_now = datetime.now()
        timestamp = time_now.strftime(datetime_format)

        f.write(str(seq_number)+','+str(acc_x)+','+str(acc_y)+','+str(acc_z) +  ','+str(gyro_x) + ','+str(gyro_y) + ','+str(gyro_z)+","+timestamp+"\n")
        print(str(seq_number)+','+str(acc_x)+','+str(acc_y)+','+str(acc_z) +  ','+str(gyro_x) + ','+str(gyro_y) + ','+str(gyro_z)+","+timestamp)
    
    # Vital sign
    if data[0] == 0xFE:
        pass
    '''if data[0] == 0xFE:
        hr          = data[1]
        hr_conf     = data[2]
        spo2        = data[3]
        spo2_conf   = data[4]
        scd_contact_state   = data[5]
        raw_data_led1 = (data[9]<<24) | (data[8]<<16) | (data[7]<<8) | data[6]
        skin_temp     = ((data[11]<<8) | data[10] ) / 10.0
        print('vital_signs,'+str(hr)+','+str(hr_conf)+','+str(spo2)+','+str(spo2_conf) +  ','+str(scd_contact_state) + ','+str(raw_data_led1) + ','+str(skin_temp) )
    '''
async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        await client.start_notify(char_uuid, notification_handler)
        await asyncio.sleep(5.0)
        await client.stop_notify(char_uuid)
        print("stop")

 
if __name__ == "__main__":
    asyncio.run(
        main(
            sys.argv[1] if len(sys.argv) > 1 else ADDRESS,
            sys.argv[2] if len(sys.argv) > 2 else CHARACTERISTIC_UUID,
        )
    )
