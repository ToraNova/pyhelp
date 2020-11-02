#!/usr/bin/python3

from datetime import timezone, datetime, timedelta

'''
datetime handling example
'''

if __name__ == "__main__":

    #now = datetime.datetime.now() # localtime
    now = datetime.now(timezone.utc) #creating a utc time
    delta = timedelta(
            days=2, weeks=3,
            seconds=3,microseconds=10,milliseconds=30,
            minutes=15,hours=1
    )
    future = now + delta
    past = now - delta

    assert(future > now)
    assert(now > past)
    assert(past < future)
    print(past)
    print(now)
    print(future)

    print(now.strftime("%Y/%m/%d %H.%M.%S"))
    print(now.strftime("%y/%-m/%-d %-H.%-M.%-S")) #no padding
    print(now.strftime("%I")) #12 hour clock
    print(now.strftime("%c")) # locale string
    print(now.strftime("%j %U")) #day of year, week of year
    print(now.strftime("%b %B")) #month as locale abbreviated and full name
    print(now.strftime("%d %-d")) #day of month
    print(now.strftime("%w %a %A")) #week day
    print(now.isoformat()) # isoformat

    fstring = datetime.fromisoformat("2020-11-02T18:10:40.741462+00:00")
    print(fstring)

    fstring = datetime.strptime("2020-11-02","%Y-%m-%d")
    print(fstring)




