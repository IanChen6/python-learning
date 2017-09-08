from datetime import  datetime,timedelta,timezone
tz_utc_8=timezone(timedelta(hours=8))
now=datetime.now()
print(dir(now))
dt=now.replace(tzinfo=tz_utc_8)#强制设为UTC+8:00
print(dt)