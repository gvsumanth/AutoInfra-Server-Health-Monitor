import time
from plyer import notification

from config import CPU_THRESHOLD, BATTERY_THRESHOLD, CPU_ALERT_INTERVAL, BATTERY_ALERT_INTERVAL
from slack_alerts import send_slack_alert
from gui_alert import show_critical_popup
from process_info import get_top_cpu_process
from email_alerts import send_email_alert
last_cpu_alert = 0
last_battery_alert = 0

def check_cpu_alert(cpu, logger):
    global last_cpu_alert
    now = time.time()

    if cpu > CPU_THRESHOLD and (now - last_cpu_alert > CPU_ALERT_INTERVAL):
        process_list = get_top_cpu_process()
        top_proc = top_cpu = top_proc_id = 0

        (top_proc_id, top_proc, top_cpu) = process_list[0]


        if cpu > 95:
            msg = f" CRITICAL CPU Alert: {cpu}%\n| Top process --> ID: {top_proc_id} | NAME: {top_proc} | CPU: ({top_cpu:.2f}%) "
            title = 'cpu'
            show_critical_popup(title, msg)
            send_slack_alert(msg)
            logger.warning(msg)
            send_email_alert(subject="CRITICAL CPU ALERT ", body=msg, logger=logger)

        else:
            msg = f" CPU Alert: {cpu}%| Top process --> ID: {top_proc_id} | NAME: {top_proc} | CPU: ({top_cpu:.2f}%) "
            send_slack_alert(msg)
            logger.warning(msg)
            notification.notify(
                title = "High CPU Usage",
                message = f"ALERT: CPU at {cpu}%\nCulpritID:{top_proc_id} | {top_proc:<25} | ({top_cpu:.2f}%) ",
                timeout = 5
            )
    last_cpu_alert = now

def check_battery_alert(battery_percent, is_charging, logger):
    global last_battery_alert
    now = time.time()

    if battery_percent is not None and battery_percent < BATTERY_THRESHOLD and not is_charging and (now - last_battery_alert > BATTERY_ALERT_INTERVAL):


        if battery_percent < 20:
            msg = f"CRITICAL: Battery at {battery_percent}%. Please plug in."
            title = 'battery'
            show_critical_popup(title, msg)
            send_slack_alert(msg)
            logger.warning(msg)
            send_email_alert(subject="CRITICAL battery ALERT ", body=msg, logger=logger)
        else:
            msg = f"Battery at {battery_percent}%. Please plug in."
            send_slack_alert(msg)
            logger.warning(msg)
            notification.notify(
                title = "Low Battery",
                message = msg,
                timeout=5
            )
        last_battery_alert = now
def show_alerts(cpu, battery_percent, is_charging, logger):
    # check_cpu_alert(cpu, logger)
    check_battery_alert(battery_percent, is_charging, logger)