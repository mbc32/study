import time
time_stamp = time.time()
log_file = './log/study.log'
file_handle = open(log_file, 'w')
while True:
    file_handle.write(str(time_stamp) + '\n')
    time.sleep(60)
