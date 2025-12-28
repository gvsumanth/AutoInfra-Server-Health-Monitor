import psutil
import time

#cpu_excluded_processes
EXCLUDED = ["System Idle Process", "System"]


def get_top_cpu_process(top_n = 5, delay = 1):
    global EXCLUDED
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    time.sleep(delay)
    process_list = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] in EXCLUDED:
            continue
        try:
            cpu = proc.cpu_percent(interval=None)

            if cpu > 5:
                process_list.append((proc.info['pid'], proc.info['name'], cpu/8))#(8threads)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    #Sorting

    process_list.sort(key=lambda x: x[2], reverse=True)
    return process_list[:top_n]
