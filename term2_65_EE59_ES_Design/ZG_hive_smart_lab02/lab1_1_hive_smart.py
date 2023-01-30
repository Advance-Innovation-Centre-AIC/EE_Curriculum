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
 
datetime_format = "%m/%d/%Y %H:%M:%S"
HEADER ="\t seq_number, \tacc_x, acc_y,acc_z, \t\tgyro_x, gyro_y,gyro_z,Timestamp"


# you can change these to match your device or override them from the command line
CHARACTERISTIC_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
ADDRESS = (
    "F8:6F:87:C1:82:04"
    if platform.system() != "Darwin"
    else "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
)


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    #print("{0}: {1}".format(sender, data))
    #print(data[0])
 
    if data[0] == 0xFF:
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
        print(
            "\t "+str(seq_number)
            +',\t\t'+str(acc_x)
            +',\t'+str(acc_y)
            +',\t'+str(acc_z)
            +',\t\t'+str(gyro_x)
            +',\t'+str(gyro_y)
            +',\t'+str(gyro_z)
            +',\t'+timestamp
            )
async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        print('Movement')
        print (HEADER)
       
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
