import time as tm
tm.localtime()

time_now = tm.localtime()

print("Trans time: ",str(time_now.tm_hour)+"h"+str(time_now.tm_min)+"m")


# Java time starts here -- 1/1/1970 0:00:00
tm.time()
#1633779358.0590053
time_now=tm.time()
delivery_time = time_now+(86400*7)
tm.localtime(delivery_time)

# sleep is in seconds
tm.sleep(5)