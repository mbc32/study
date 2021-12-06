import time
time_stamp = time.time()
log_file = './log/study.log'
with open(log_file, 'w') as file_handle:
    file_handle.write(str(time_stamp) + '\n')
