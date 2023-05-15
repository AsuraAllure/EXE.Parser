import datetime

#Unix and POSIX-compliant systems implement the time_t type as a signed integer
#(typically 32 or 64 bits wide) which represents the number of seconds since
#the start of the Unix epoch: midnight UTC of January 1, 1970 (not counting leap seconds).
#Some systems correctly handle negative time values,


#from datetime import datetime
#ts = int('1284101485')
# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
#print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))


class TimeDateStamp:
    def __init__(self, tds):
        self.tds = int.from_bytes(tds, "little", signed=False)

    def __str__(self):
        return datetime.datetime.utcfromtimestamp(self.tds).strftime('%Y-%m-%d %H:%M:%S')