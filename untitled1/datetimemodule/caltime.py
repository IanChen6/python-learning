from datetime import datetime, timedelta

now=datetime.now()
print(now)
n2=now +timedelta(days=1)
print(n2)
n3=now+timedelta(days=2,hours=10)
print(n3)