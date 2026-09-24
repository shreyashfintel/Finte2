# 📊 Daily Telemetry & System Health Report

**Report Date:** {{REPORT_DATE}}  
**Log Source:** `{{LOG_FILE_NAME}}`  
**Time Range:** {{START_TIME}} – {{END_TIME}} ({{TOTAL_SNAPSHOTS}} snapshots)  

---

### 1. System Overview

* **Host RAM:** {{TOTAL_RAM_GB}} GB
* **Disk Partition ({{DRIVE_LETTER}}:):** {{TOTAL_DISK_GB}} GB
* **Primary Workload:** {{PRIMARY_WORKLOAD_NAME}} (PID: {{PRIMARY_WORKLOAD_PID}})
* **Operational Status:** {{OVERALL_STATUS}}

---

### 2. Metric Extremes & Summary

| Resource Metric | Start Value | Min Recorded | Peak Recorded | End Value | Net Change |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CPU Usage** | {{CPU_START}}% | {{CPU_MIN}}% ({{CPU_MIN_TIME}}) | **{{CPU_PEAK}}%** ({{CPU_PEAK_TIME}}) | {{CPU_END}}% | Avg: ~{{CPU_AVG}}% |
| **RAM In Use** | {{RAM_USED_START_GB}} GB ({{RAM_USED_START_PCT}}%) | {{RAM_USED_MIN_GB}} GB ({{RAM_USED_MIN_TIME}}) | **{{RAM_USED_PEAK_GB}} GB** ({{RAM_USED_PEAK_TIME}}) | {{RAM_USED_END_GB}} GB ({{RAM_USED_END_PCT}}%) | **+{{RAM_USED_DELTA_GB}} GB** |
| **RAM Available** | {{RAM_FREE_START_GB}} GB | **{{RAM_FREE_MIN_GB}} GB** ({{RAM_FREE_MIN_TIME}}) | {{RAM_FREE_MAX_GB}} GB ({{RAM_FREE_MAX_TIME}}) | {{RAM_FREE_END_GB}} GB | -{{RAM_FREE_DELTA_GB}} GB |
| **Primary App Memory** | {{APP_MEM_START_MB}} MB | {{APP_MEM_START_MB}} MB (Start) | **{{APP_MEM_PEAK_MB}} MB** (End) | {{APP_MEM_END_MB}} MB ({{APP_MEM_END_PCT}}%) | **+{{APP_MEM_DELTA_MB}} MB (+{{APP_MEM_DELTA_PCT}}%)** |
| **Disk Active Time** | {{DISK_ACT_START}}% | {{DISK_ACT_MIN}}% | **{{DISK_ACT_PEAK}}%** ({{DISK_ACT_PEAK_TIME}}) | {{DISK_ACT_END}}% | Median: ~{{DISK_ACT_MEDIAN}}% |
| **Disk Read Speed** | {{DISK_READ_START_MB}} MB/s | {{DISK_READ_MIN_MB}} MB/s | **{{DISK_READ_PEAK_MB}} MB/s** ({{DISK_READ_PEAK_TIME}}) | {{DISK_READ_END_MB}} MB/s | {{DISK_READ_STATUS}} |
| **Disk Write Speed** | {{DISK_WRITE_START_MB}} MB/s | {{DISK_WRITE_MIN_MB}} MB/s | **{{DISK_WRITE_PEAK_MB}} MB/s** ({{DISK_WRITE_PEAK_TIME}}) | {{DISK_WRITE_END_MB}} MB/s | Flush rate: {{DISK_WRITE_FLUSH_RATE}} MB/s |
| **Free Storage ({{DRIVE_LETTER}}:)** | {{DISK_FREE_START_GB}} GB ({{DISK_FREE_START_PCT}}%) | **{{DISK_FREE_END_GB}} GB** (End) | {{DISK_FREE_START_GB}} GB (Start) | {{DISK_FREE_END_GB}} GB ({{DISK_FREE_END_PCT}}%) | **-{{DISK_CONSUMED_GB}} GB consumed** |
| **Battery Level** | {{BAT_START}}% ({{BAT_STATUS}}) | {{BAT_MIN}}% | **{{BAT_PEAK}}%** ({{BAT_PEAK_TIME}}) | {{BAT_END}}% ({{BAT_END_MODE}}) | +{{BAT_DELTA}}% |
| **Database Replicas** | {{DB_REPLICA_COUNT}} | {{DB_REPLICA_COUNT}} | {{DB_REPLICA_COUNT}} | {{DB_REPLICA_COUNT}} | {{DB_MODE}} |

---

### 3. Top Process Tracking

| Process Name | Subsystem | Resource Footprint | Runtime Behavior |
| :--- | :--- | :--- | :--- |
| **{{PROC_1_NAME}}** (PID: {{PROC_1_PID}}) | Memory & CPU | • Start: {{PROC_1_START_MB}} MB<br>• Mid: {{PROC_1_MID_MB}} MB<br>• End: **{{PROC_1_END_MB}} MB**<br>• CPU Range: {{PROC_1_CPU_RANGE}} | {{PROC_1_BEHAVIOR}} |
| **{{PROC_2_NAME}}** (PID: {{PROC_2_PID}}) | Kernel Memory | • Started: {{PROC_2_START_TIME}} ({{PROC_2_START_MB}} MB)<br>• Peak: **{{PROC_2_PEAK_MB}} MB**<br>• CPU Max: {{PROC_2_PEAK_CPU}}% | {{PROC_2_BEHAVIOR}} |
| **{{PROC_3_NAME}}** (Multi-Instance) | Disk I/O | • Peak Write: **{{PROC_3_PEAK_WRITE_MB}} MB/s**<br>• Periodic Flushes: {{PROC_3_FLUSH_RANGE_MB}} MB/s | {{PROC_3_BEHAVIOR}} |
| **{{PROC_4_NAME}}** | Disk I/O & CPU | • Peak Write: **{{PROC_4_PEAK_WRITE_MB}} MB/s** ({{PROC_4_PEAK_TIME}})<br>• CPU Max: {{PROC_4_PEAK_CPU}}% | {{PROC_4_BEHAVIOR}} |
| **Desktop Background Tasks** | CPU & Memory | • UI Engine CPU: up to **{{PROC_5_CPU}}%**<br>• Web Browser CPU: up to **{{PROC_6_CPU}}%**<br>• Total Memory: ~{{DESKTOP_MEM_RANGE_MB}} MB | {{DESKTOP_BEHAVIOR}} |

---

### 4. Key Chronological Events

| Timestamp | Milestone Event | Metrics at Event | Operational Note |
| :---: | :--- | :--- | :--- |
| `{{EVENT_1_TIME}}` | **Session Started** | CPU: {{EVENT_1_CPU}}% \| RAM: {{EVENT_1_RAM_GB}} GB \| Free Disk: {{EVENT_1_DISK_GB}} GB | Baseline initialized. |
| `{{EVENT_2_TIME}}` | **Read I/O Burst** | Read: **{{EVENT_2_READ_MB}} MB/s** \| Write: {{EVENT_2_WRITE_MB}} MB/s | Peak data read throughput observed. |
| `{{EVENT_3_TIME}}` | **Disk Saturation Peak** | Disk Active: **{{EVENT_3_DISK_ACT}}%** \| Write: {{EVENT_3_WRITE_MB}} MB/s | Highest I/O utilization window. |
| `{{EVENT_4_TIME}}` | **Peak CPU Utilization** | CPU Used: **{{EVENT_4_CPU}}%** (Free: {{EVENT_4_CPU_FREE}}%) | High core utilization across active processes. |
| `{{EVENT_5_TIME}}` | **OS Memory Compression** | Compressed RAM: **{{EVENT_5_COMP_MB}} MB** | Memory manager invoked page compression. |
| `{{EVENT_6_TIME}}` | **Full Charge Reached** | Battery: **{{EVENT_6_BAT}}%** (AC Utility) | Host shifted to float charging mode. |
| `{{EVENT_7_TIME}}` | **Peak Memory Load** | RAM Used: **{{EVENT_7_RAM_USED_GB}} GB ({{EVENT_7_RAM_USED_PCT}}%)** \| Free: {{EVENT_7_RAM_FREE_GB}} GB | System memory peak threshold reached. |
| `{{EVENT_8_TIME}}` | **Session Terminated** | CPU: {{EVENT_8_CPU}}% \| RAM: {{EVENT_8_RAM_GB}} GB \| Free Disk: {{EVENT_8_DISK_GB}} GB | Telemetry capture ended. |

---

### 5. Automated Health Audit

| Focus Area | Data Evidence | Finding | Health Status |
| :--- | :--- | :--- | :---: |
| **Memory Retention** | {{MEM_AUDIT_EVIDENCE}} | {{MEM_AUDIT_FINDING}} | {{MEM_AUDIT_BADGE}} |
| **Disk Space Burn** | {{DISK_AUDIT_EVIDENCE}} | {{DISK_AUDIT_FINDING}} | {{DISK_AUDIT_BADGE}} |
| **Processor Stability**| {{CPU_AUDIT_EVIDENCE}} | {{CPU_AUDIT_FINDING}} | {{CPU_AUDIT_BADGE}} |