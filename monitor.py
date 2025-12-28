import psutil
import time
from alerts import show_alerts

def get_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else None
    is_charging = battery.power_plugged if battery else None


    print(f"""
========= SYSTEM STATS =========
CPU Usage     : {cpu}%
RAM Usage     : {ram}%
Disk Usage    : {disk}%
Battery Level : {battery_percent}%
Charging      : {is_charging}
================================
""")
    return cpu, battery_percent, is_charging

def adaptive_sleep(cpu):
    if cpu < 60:
        time.sleep(5)
    elif cpu < 80:
        time.sleep(2)
    else:
        time.sleep(0.5)


def monitor(logger):
    while True:
        cpu, battery_percent, is_charging = get_stats()
        show_alerts(cpu, battery_percent, is_charging, logger)
        adaptive_sleep(cpu)
