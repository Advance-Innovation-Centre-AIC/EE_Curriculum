# -*- coding: utf-8 -*-
import sys
import asyncio
import platform


from struct import *
from bleak import BleakClient


import time
from datetime import datetime


datetime_format = "%m/%d/%Y %H:%M:%S"
HEADER = "\tHR, Hr_conf, Spo2, Spo2_conf, Scd_contact_state, Raw_data_led1, Skin_temp, Timestamp"


# you can change these to match your device or override them from the command line
CHARACTERISTIC_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
ADDRESS = (
    "F8:6F:87:C1:82:04"
    if platform.system() != "Darwin"
    else "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"
)


def notification_handler(sender, data):
    """Simple notification handler which prints the data received."""
    # print("{0}: {1}".format(sender, data))
    # print(data[0])
 
    if data[0] == 0xFE:
        hr          = data[1]
        hr_conf     = data[2]
        spo2        = data[3]
        spo2_conf   = data[4]
        scd_contact_state   = data[5]


        raw_data_led1 = (data[9]<<24) | (data[8]<<16) | (data[7]<<8) | data[6]
        skin_temp     = ((data[11]<<8) | data[10] ) / 10.0
       
        time_now = datetime.now()
        timestamp = time_now.strftime(datetime_format)
       
        print(
            '\t'+str(hr)
            +'\t'+str(hr_conf)
            +',\t'+str(spo2)
            +',\t'+str(spo2_conf)
            +',\t\t'+str(scd_contact_state)
            +',\t\t'+str(raw_data_led1)
            +',\t'+str(skin_temp)
            +',\t '+timestamp
            )


   
async def main(address, char_uuid):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        print('vital_signs')
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
