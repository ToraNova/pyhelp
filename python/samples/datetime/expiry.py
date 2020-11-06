#!/usr/bin/python3o

from datetime import timezone, datetime, timedelta

if __name__ == "__main__":

    now = datetime.now(timezone.utc)
    delta = timedelta(days=1)
    ti0 = now + delta
    ti1 = now - delta

    tis0 = ti0.strftime("%Y%m%d")
    tis1 = ti1.strftime("%Y%m%d")

    re0 = datetime.strptime(tis0,"%Y%m%d")
    re1 = datetime.strptime(tis1,"%Y%m%d")
    print(re0, re0>=now)
    print(re1, re1>=now)
