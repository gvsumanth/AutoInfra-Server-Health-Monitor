import time
print(time.time())

print("______________________________________________________")
import psutil




def get_top_cpu_process(top_n = 5, delay = 1):

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    time.sleep(delay)
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            cpu = proc.cpu_percent(interval=None)

            if cpu > 1:
                process_list.append((proc.info['pid'], proc.info['name'], cpu))

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    #Sorting

    process_list.sort(key=lambda x: x[2], reverse=True)
    return process_list[:top_n]
a = get_top_cpu_process()
for i in a :
    print(i)