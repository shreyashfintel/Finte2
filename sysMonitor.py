#!/usr/bin/env python3

import psutil
import time
import json
import datetime
import os
import sys

INTERVAL = 5 # seconds

# ANSI color codes for beautiful terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_log_file_path():
    now = datetime.datetime.now()
    year_dir = f"{now.year}_logs"
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)
    return os.path.join(year_dir, f"{now.strftime('%Y-%m-%d')}.jsonl")

def get_top_cpu_processes(n=10):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    
    cpu_count = psutil.cpu_count() or 1
    
    processes.sort(key=lambda p: (p['cpu_percent'] or 0.0) / cpu_count, reverse=True)
    
    top = []
    for p in processes:
        pct = (p['cpu_percent'] or 0.0) / cpu_count
        if pct >= 2.0:
            top.append({
                "Process": p['name'],
                "CPU_Percent": round(pct, 2)
            })
            if len(top) == n:
                break
    return top

def get_top_ram_processes(n=10):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
            
    processes.sort(key=lambda p: p['memory_percent'] or 0.0, reverse=True)
    
    top = []
    for p in processes:
        pct = p['memory_percent'] or 0.0
        if pct >= 2.0:
            top.append({
                "ProcessName": p['name'],
                "Id": p['pid'],
                "RAM_MB": round(p['memory_info'].rss / (1024 * 1024), 2) if p['memory_info'] else 0.0,
                "RAM_%": round(pct, 2)
            })
            if len(top) == n:
                break
    return top

def get_total_disk_usage():
    total_size = 0
    total_used = 0
    
    seen_devices = set()
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                continue
        else:
            # Ignore virtual, loop/snap, and network mounts
            if 'snap' in part.mountpoint or 'docker' in part.mountpoint or part.fstype.lower() in (
                'squashfs', 'tmpfs', 'devtmpfs', 'overlay', 'nfs', 'nfs4', 'cifs', 'smb', 'fuse.sshfs', 'autofs'
            ):
                continue
                
        # Prevent double-counting the same underlying physical device/partition mounted in multiple places
        if part.device in seen_devices:
            continue
        seen_devices.add(part.device)
            
        try:
            usage = psutil.disk_usage(part.mountpoint)
            total_size += usage.total
            total_used += usage.used
        except PermissionError:
            pass
            
    total_free = total_size - total_used
    percent = round((total_used / total_size) * 100, 2) if total_size > 0 else 0
    
    return {
        "SizeGB": round(total_size / (1024**3), 2),
        "UsedGB": round(total_used / (1024**3), 2),
        "FreeGB": round(total_free / (1024**3), 2),
        "UsedPercent": percent
    }

def collect_metrics(prev_disk_io, prev_net_io, prev_time):
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    curr_time = time.time()
    time_delta = curr_time - prev_time
    
    # 1. CPU
    cpu_usage = psutil.cpu_percent(interval=None)
    cpu_free = 100.0 - cpu_usage
    top_cpu = get_top_cpu_processes(n=10)
    
    # 2. RAM and SWAP
    mem = psutil.virtual_memory()
    total_ram_gb = round(mem.total / (1024**3), 2)
    available_ram_gb = round(mem.available / (1024**3), 2)
    used_ram_gb = round((mem.total - mem.available) / (1024**3), 2)
    ram_perc = round(mem.percent, 2)
    
    swap = psutil.swap_memory()
    total_swap_gb = round(swap.total / (1024**3), 2)
    used_swap_gb = round(swap.used / (1024**3), 2)
    free_swap_gb = round(swap.free / (1024**3), 2)
    swap_perc = round(swap.percent, 2)
    
    top_ram = get_top_ram_processes(n=10)
    
    # 3. Disk Space & Activity
    disk_stats = get_total_disk_usage()
    
    curr_disk_io = psutil.disk_io_counters()
    read_speed_mb = 0.0
    write_speed_mb = 0.0
    disk_activity_perc = 0.0
    
    if prev_disk_io and curr_disk_io and time_delta > 0:
        read_bytes = curr_disk_io.read_bytes - prev_disk_io.read_bytes
        write_bytes = curr_disk_io.write_bytes - prev_disk_io.write_bytes
        read_speed_mb = (read_bytes / (1024 * 1024)) / time_delta
        write_speed_mb = (write_bytes / (1024 * 1024)) / time_delta
        
        if hasattr(curr_disk_io, 'busy_time') and curr_disk_io.busy_time is not None:
            delta_busy_ms = curr_disk_io.busy_time - prev_disk_io.busy_time
            disk_activity_perc = (delta_busy_ms / (time_delta * 1000.0)) * 100.0
            disk_activity_perc = round(min(100.0, max(0.0, disk_activity_perc)), 2)

    # 4. Network
    curr_net_io = psutil.net_io_counters()
    sent_speed_mb = 0.0
    recv_speed_mb = 0.0
    if prev_net_io and curr_net_io and time_delta > 0:
        sent_bytes = curr_net_io.bytes_sent - prev_net_io.bytes_sent
        recv_bytes = curr_net_io.bytes_recv - prev_net_io.bytes_recv
        sent_speed_mb = (sent_bytes / (1024 * 1024)) / time_delta
        recv_speed_mb = (recv_bytes / (1024 * 1024)) / time_delta
    
    # 5. Battery
    battery = psutil.sensors_battery() if hasattr(psutil, 'sensors_battery') else None
    if battery is None:
        battery_percent = "N/A"
        battery_status = "Not Available"
    else:
        battery_percent = round(battery.percent, 2)
        battery_status = 2 if battery.power_plugged else 1 
    
    metrics = {
        "Timestamp": now_str,
        "Disk": {
            "Space": {
                "DeviceID": "All Physical",
                "SizeGB": disk_stats["SizeGB"],
                "FreeGB": disk_stats["FreeGB"],
                "UsedGB": disk_stats["UsedGB"],
                "UsedPercent": disk_stats["UsedPercent"]
            },
            "Activity": {
                "InstanceName": "system",
                "UsedPercent": disk_activity_perc 
            },
            "ReadWrite": {
                "Disk": "system",
                "ReadMBs": round(read_speed_mb, 2),
                "WriteMBs": round(write_speed_mb, 2)
            }
        },
        "RAM": {
            "AvailableGB": available_ram_gb,
            "TotalGB": total_ram_gb,
            "UsedGB": used_ram_gb,
            "UsedPercent": ram_perc,
            "TopProcesses": top_ram
        },
        "SWAP": {
            "FreeGB": free_swap_gb,
            "TotalGB": total_swap_gb,
            "UsedGB": used_swap_gb,
            "UsedPercent": swap_perc
        },
        "Network": {
            "UploadMBs": round(sent_speed_mb, 2),
            "DownloadMBs": round(recv_speed_mb, 2),
            "TotalSentGB": round(curr_net_io.bytes_sent / (1024**3), 2),
            "TotalRecvGB": round(curr_net_io.bytes_recv / (1024**3), 2)
        },
        "Battery": {
            "Percentage": battery_percent,
            "Status": battery_status
        },
        "CPU": {
            "Used": round(cpu_usage, 2),
            "TopProcesses": top_cpu,
            "Free": round(cpu_free, 2)
        }
    }
    
    return metrics, curr_disk_io, curr_net_io, curr_time

def print_dashboard(metrics, log_file):
    clear_screen()
    c = Colors
    
    print(f"{c.BOLD}{c.CYAN}{'='*60}{c.RESET}")
    print(f"{c.BOLD}SYSTEM MONITOR V2{c.RESET} | Time: {metrics['Timestamp']}")
    print(f"{c.CYAN}{'-'*60}{c.RESET}")
    
    # CPU
    cpu = metrics['CPU']
    cpu_color = c.GREEN if cpu['Used'] < 50 else (c.YELLOW if cpu['Used'] < 85 else c.RED)
    print(f"{c.BOLD}[ CPU ]{c.RESET} Used: {cpu_color}{cpu['Used']}%{c.RESET} | Free: {cpu['Free']}%")
    if isinstance(cpu['TopProcesses'], list) and len(cpu['TopProcesses']) > 0:
        top_cpu_str = ", ".join([f"{p['Process']} ({p['CPU_Percent']}%)" for p in cpu['TopProcesses'][:5]])
        print(f"        {c.YELLOW}Top 5 (Logged 10):{c.RESET} {top_cpu_str}")
    print(f"{c.CYAN}{'-'*60}{c.RESET}")
    
    # RAM and SWAP
    ram = metrics['RAM']
    swap = metrics['SWAP']
    ram_color = c.GREEN if ram['UsedPercent'] < 60 else (c.YELLOW if ram['UsedPercent'] < 85 else c.RED)
    
    print(f"{c.BOLD}[ RAM ]{c.RESET} Used: {ram_color}{ram['UsedGB']} GB ({ram['UsedPercent']}%){c.RESET} | Available: {ram['AvailableGB']} GB | Total: {ram['TotalGB']} GB")
    print(f"{c.BOLD}[ SWAP ]{c.RESET} Used: {swap['UsedGB']} GB ({swap['UsedPercent']}%) | Free: {swap['FreeGB']} GB | Total: {swap['TotalGB']} GB")
    
    if isinstance(ram['TopProcesses'], list) and len(ram['TopProcesses']) > 0:
        print(f"        {c.YELLOW}Top 5 RAM Processes (Logged 10):{c.RESET}")
        for i, tp in enumerate(ram['TopProcesses'][:5]):
            print(f"          {i+1}. {tp.get('ProcessName', 'Unknown')} (PID {tp.get('Id', '')}) - {tp.get('RAM_MB', 0)} MB ({tp.get('RAM_%', 0)}%)")
    print(f"{c.CYAN}{'-'*60}{c.RESET}")
    
    # DISK
    disk = metrics['Disk']
    space = disk['Space']
    rw = disk['ReadWrite']
    activity = disk['Activity']['UsedPercent']
    disk_color = c.GREEN if space['UsedPercent'] < 70 else (c.YELLOW if space['UsedPercent'] < 90 else c.RED)
    
    print(f"{c.BOLD}[ DISK ]{c.RESET} Used: {disk_color}{space['UsedGB']} GB ({space['UsedPercent']}%){c.RESET} | Free: {space['FreeGB']} GB | Total: {space['SizeGB']} GB")
    print(f"         {c.YELLOW}I/O:{c.RESET} Read {rw['ReadMBs']} MB/s | Write {rw['WriteMBs']} MB/s | Activity: {activity}%")
    print(f"{c.CYAN}{'-'*60}{c.RESET}")

    # NETWORK
    net = metrics['Network']
    print(f"{c.BOLD}[ NET ]{c.RESET} Upload: {net['UploadMBs']} MB/s | Download: {net['DownloadMBs']} MB/s")
    print(f"{c.CYAN}{'-'*60}{c.RESET}")
    
    # BATTERY
    batt = metrics['Battery']
    if batt['Percentage'] == "N/A":
        print(f"{c.BOLD}[ BATTERY ]{c.RESET} Not Available (No battery detected)")
    else:
        batt_color = c.GREEN if batt['Percentage'] > 50 else (c.YELLOW if batt['Percentage'] > 20 else c.RED)
        status_str = "Charging/Plugged in" if batt['Status'] == 2 else "Discharging"
        print(f"{c.BOLD}[ BATTERY ]{c.RESET} {batt_color}{batt['Percentage']}%{c.RESET} ({status_str})")
    
    print(f"{c.BOLD}{c.CYAN}{'='*60}{c.RESET}")
    print(f"{c.BOLD}{c.GREEN}Data logged to {log_file}... (Press Ctrl+C to stop){c.RESET}")

def main():
    # Prime the overall CPU percent calculation
    psutil.cpu_percent()
    
    # Prime the process iterator so CPU percentages are calculated accurately over the interval
    list(psutil.process_iter(['cpu_percent']))
    
    prev_disk_io = psutil.disk_io_counters()
    prev_net_io = psutil.net_io_counters()
    prev_time = time.time()
    
    clear_screen()
    print("Initializing System Monitor V2...")
    
    try:
        while True:
            time.sleep(INTERVAL)
            metrics, prev_disk_io, prev_net_io, prev_time = collect_metrics(prev_disk_io, prev_net_io, prev_time)
            
            log_file = get_log_file_path()
            
            with open(log_file, 'a') as f:
                f.write(json.dumps(metrics) + '\n')
            
            print_dashboard(metrics, log_file)
            
    except KeyboardInterrupt:
        clear_screen()
        print(f"{Colors.BOLD}{Colors.GREEN}Monitoring stopped safely.{Colors.RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()