import time
def now():
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
	
print(now())
