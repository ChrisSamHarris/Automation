from datetime import datetime
import json

#### UNIX TIME CONVERSION CALCULATOR #####
#Exmple JSON format: "dt": 1651942690
def unix_time_conversion(unix_ts):
    '''Function that converts UNIX date/time into a user-friendly format.
    if you encounter a "year is out of range" error the timestamp
    may be in milliseconds, try `ts /= 1000` in that case.'''
    ts = int(unix_ts)
    return datetime.utcfromtimestamp(ts).strftime('%dth %B %Y %H:%M')
