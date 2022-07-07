import sys

import datetime
input = sys.stdin.readline



def time():
    h, m = map(int,input().split())
    pre=datetime.datetime(2018,1,1,h,m)
    period = datetime.timedelta(minutes=45)
    
    time = pre - period

    print(' '.join([str(int(str(time)[11:13])),str(int(str(time)[14:16])) ]))

if __name__ == "__main__" :
    time()
