# pip install psutil, plyer
# pip install requests
# pip install python-dotenv

# import psutil
# import time
# from plyer import notification
# import os
# import requests

# from dotenv import load_dotenv
# load_dotenv()

# SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

# #Constraints
# CPU_ALERT = 5
# BATTERY_ALERT = 30

# #time
# last_battery_alert = 0 
# last_cpu_alert = 0

# #notification_constraints
# BATTERY_ALERT_INTERVAL = 60
# CPU_ALERT_INTERVAL = 30

# #cpu_excluded_processes
# EXCLUDED = ["System Idle Process", "System"]


# def send_slack_alert(message):
#     if not SLACK_WEBHOOK_URL:
#         print("[Slack] NO webhook url set")
#         return
#     payload = {
#         "text" : message
#     }

#     try:
#         response = requests.post(SLACK_WEBHOOK_URL, json=payload)
#         if response.status_code != 200:
#             print(f"[Slack] Failed: {response.status_code}, {response.text}")
#     except Exception as e:
#         print('[Slack] error: {e}')



# def get_stats():
#     cpu = psutil.cpu_percent(interval=1)
#     ram = psutil.virtual_memory().percent
#     disk = psutil.disk_usage('/').percent
#     battery = psutil.sensors_battery()
#     battery_percent = battery.percent if battery else None
#     is_charging = battery.power_plugged if battery else None


#     print(f"""
# ========= SYSTEM STATS =========
# CPU Usage     : {cpu}%
# RAM Usage     : {ram}%
# Disk Usage    : {disk}%
# Battery Level : {battery_percent}%
# Charging      : {is_charging}
# ================================
# """)
#     return cpu, battery_percent, is_charging

# def adaptive_sleep(cpu):
#     if cpu < 60:
#         time.sleep(5)
#     elif cpu < 80:
#         time.sleep(2)
#     else:
#         time.sleep(0.5)


# def get_top_cpu_process(top_n = 5, delay = 1):
#     global EXCLUDED
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             proc.cpu_percent(interval=None)
#         except (psutil.NoSuchProcess, psutil.AccessDenied):
#             continue
    
#     time.sleep(delay)
#     process_list = []
#     for proc in psutil.process_iter(['pid', 'name']):
#         if proc.info['name'] in EXCLUDED:
#             continue
#         try:
#             cpu = proc.cpu_percent(interval=None)

#             if cpu > 5:
#                 process_list.append((proc.info['pid'], proc.info['name'], cpu/8))#(8threads)

#         except (psutil.NoSuchProcess, psutil.AccessDenied):
#             continue

#     #Sorting

#     process_list.sort(key=lambda x: x[2], reverse=True)
#     return process_list[:top_n]


# def show_alerts(cpu, battery_percent, is_charging):
#     global last_battery_alert, last_cpu_alert, CPU_ALERT, BATTERY_ALERT
#     now = time.time()
#     if cpu > CPU_ALERT and (now - last_cpu_alert > CPU_ALERT_INTERVAL):
#         process_list = get_top_cpu_process()
#         top_proc = 0
#         top_cpu = 0
#         top_proc_id = 0
#         (top_proc_id, top_proc, top_cpu) = process_list[0]

#         msg = f" CPU Alert: {cpu}%| Top process --> ID: {top_proc_id} | NAME: {top_proc} | CPU: ({top_cpu:.2f}%) "
#         send_slack_alert(msg)
#         notification.notify(
#             title = "High CPU Usage",
#             message = f"ALERT: CPU at {cpu}%, Top process --> ID: {top_proc_id} | NAME: {top_proc:<25} | CPU: ({top_cpu:.2f}%) ",
#             timeout = 5
#         )
#     last_cpu_alert = now

#     if battery_percent is not None and battery_percent < BATTERY_ALERT and not is_charging and (now - last_battery_alert > BATTERY_ALERT_INTERVAL):
#         notification.notify(
#             title = "Low Battery",
#             message = f"Battery at {battery_percent}%. Please plug in.",
#             timeout=5
#         )
#         last_battery_alert = now
    
# def monitor():
#     while True:
#         cpu, battery_percent, is_charging = get_stats()
#         show_alerts(cpu, battery_percent, is_charging)
#         adaptive_sleep(cpu)


# if __name__ == "__main__":
#     monitor()
