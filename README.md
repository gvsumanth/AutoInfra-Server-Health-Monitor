# AutoInfra-Server-Health-Monitor


A Python-based system monitoring script to track CPU, RAM, disk usage, and uptime on Windows or Linux systems.  
Logs system metrics to a timestamped file and sends Slack alerts when resource usage exceeds defined thresholds.

## Features
- Real-time monitoring of system health using `psutil`
- Slack alert integration via webhook for threshold breaches
- Configurable thresholds and modular code structure
- Scheduled execution using Windows Task Scheduler or cron

## Tech Stack
Python, psutil, logging, requests (for Slack), Task Scheduler (Windows)

## Status
Work in progress — core functionality being implemented.

## Author
Sumanth GV  
GitHub: https://github.com/gvsumanth
