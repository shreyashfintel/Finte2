# System Telemetry Log Audit Report
**Source File:** `{{source_file}}` | **Capture Duration:** `{{start_time}}` – `{{end_time}}` ({{record_count}} Polling Records) | **Log Artifact:** `{{log_artifact_date}}`

---

### 1. Telemetry Log Execution Overview
This report is derived exclusively from the raw JSONL records contained in `{{source_file}}`. The dataset records {{record_count}} continuous metric snapshots across a host configured with {{total_ram_gb}} GB total RAM and a {{disk_size_gb}} GB primary partition ({{drive_letter}}:).

---

### 2. Subsystem Telemetry Summary (Observed Metrics & Extremes)

| JSON Key & Subsystem | Initial State (`{{start_time}}`) | Minimum Recorded | Peak Recorded | Final State (`{{end_time}}`) | Observed Net Delta |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CPU Load (%)**<br>`.CPU.Used` | {{cpu_initial}}% | {{cpu_min}}% ({{cpu_min_time}}) | **{{cpu_peak}}%** ({{cpu_peak_time}}) | {{cpu_final}}% | Mean: ~{{cpu_mean}}% |
| **RAM Used (GB)**<br>`.RAM.UsedGB` | {{ram_used_initial}} GB ({{ram_used_initial_pct}}%) | {{ram_used_min}} GB ({{ram_used_min_time}}) | **{{ram_used_peak}} GB** ({{ram_used_peak_time}}) | {{ram_used_final}} GB ({{ram_used_final_pct}}%) | **+{{ram_used_delta}} GB net** |
| **RAM Free (GB)**<br>`.RAM.FreeGB` | {{ram_free_initial}} GB | **{{ram_free_min}} GB** ({{ram_free_min_time}}) | {{ram_free_max}} GB ({{ram_free_max_time}}) | {{ram_free_final}} GB | -{{ram_free_delta}} GB free |
| **Python Memory**<br>`.RAM.TopProcesses` | {{py_mem_initial}} MB ({{py_mem_initial_pct}}%) | {{py_mem_min}} MB (Start) | **{{py_mem_peak}} MB** (Final) | {{py_mem_final}} MB ({{py_mem_final_pct}}%) | **+{{py_mem_delta_mb}} MB (+{{py_mem_delta_pct}}%)** |
| **Disk Activity (%)**<br>`.Disk.Activity` | {{disk_act_initial}}% | {{disk_act_min}}% ({{disk_act_min_time}}) | **{{disk_act_peak}}%** ({{disk_act_peak_time}}) | {{disk_act_final}}% | Median: ~{{disk_act_median}}% |
| **Disk Read (MB/s)**<br>`.Disk.ReadWrite` | {{disk_read_initial}} MB/s | {{disk_read_min}} MB/s | **{{disk_read_peak}} MB/s** ({{disk_read_peak_time}}) | {{disk_read_final}} MB/s | {{disk_read_delta_notes}} |
| **Disk Write (MB/s)**<br>`.Disk.ReadWrite` | {{disk_write_initial}} MB/s | {{disk_write_min}} MB/s | **{{disk_write_peak}} MB/s** ({{disk_write_peak_time}}) | {{disk_write_final}} MB/s | {{disk_write_notes}} |
| **Drive C: Free (GB)**<br>`.Disk.Space.FreeGB` | {{drive_free_initial}} GB ({{drive_free_initial_pct}}%) | **{{drive_free_min}} GB** (Final) | {{drive_free_max}} GB (Start) | {{drive_free_final}} GB ({{drive_free_final_pct}}%) | **-{{drive_free_consumed}} GB consumed** |
| **Battery Level (%)**<br>`.Battery` | {{bat_initial}}% (Status: {{bat_status}}) | {{bat_min}}% | **{{bat_peak}}%** ({{bat_peak_time}}) | {{bat_final}}% ({{bat_final_mode}}) | +{{bat_delta}}% gained |
| **Postgres Replicas**<br>`.Postgres` | ReplicaCount: {{pg_replica_initial}} | {{pg_replica_min}} | {{pg_replica_max}} | ReplicaCount: {{pg_replica_final}} | {{pg_deployment_type}} |

---

### 3. Top Processes Recorded in Telemetry

| Process Identity | Logged Subsystem | Metric Values & Peak Footprint | Observed Behavior in Log |
| :--- | :--- | :--- | :--- |
| **{{process_1_name}}**<br>(PID {{process_1_pid}}) | RAM & CPU | • Start: {{proc_1_start_mem}} MB ({{proc_1_start_mem_pct}}%)<br>• Mid: {{proc_1_mid_mem}} MB ({{proc_1_mid_mem_pct}}%)<br>• End: **{{proc_1_end_mem}} MB ({{proc_1_end_mem_pct}}%)**<br>• CPU: {{proc_1_cpu_range}} | {{proc_1_behavior_description}} |
| **Memory Compression**<br>(PID {{proc_mc_pid}}) | Kernel RAM | • First Logged: {{proc_mc_first_time}} ({{proc_mc_first_mem}} MB)<br>• Peak: **{{proc_mc_peak_mem}} MB ({{proc_mc_peak_pct}}%)**<br>• CPU: up to {{proc_mc_peak_cpu}}% | {{proc_mc_behavior_description}} |
| **{{db_process_name}}**<br>({{db_instances_label}}) | Disk I/O | • Single Instance Max: **{{db_proc_single_max}} MB/s**<br>• Total Write Flushes: {{db_proc_flush_range}} MB/s | {{db_proc_behavior_description}} |
| **{{tool_process_name}}** | Disk I/O & CPU | • Write Peak: **{{tool_proc_peak_write}} MB/s** ({{tool_proc_peak_time}})<br>• CPU: up to {{tool_proc_peak_cpu}}% | {{tool_proc_behavior_description}} |
| **{{app_ui_process_name}} / {{browser_process_name}}** | CPU & RAM | • {{app_ui_name}} CPU: up to **{{app_ui_peak_cpu}}%**<br>• {{browser_name}} CPU: up to **{{browser_peak_cpu}}%**<br>• {{app_ui_name}} RAM: ~{{app_ui_ram_range}} MB | {{desktop_proc_behavior_description}} |

---

### 4. Chronological Telemetry Log Milestones

| Timestamp | Event Type | Logged Metrics | Operational Observation from Log |
| :--- | :--- | :--- | :--- |
| `{{time_milestone_1}}` | Session Start | CPU: {{m1_cpu}}% \| RAM: {{m1_ram}} GB ({{m1_ram_pct}}%)<br>Drive C: {{m1_disk}} GB free \| Bat: {{m1_bat}}% | First logged record. Baseline state established. |
| `{{time_milestone_2}}` | I/O Surge | Read: **{{m2_read}} MB/s** \| Write: {{m2_write}} MB/s<br>Disk Activity: {{m2_disk_act}}% | Highest read throughput logged in the file on Drive {{drive_letter}}:. |
| `{{time_milestone_3}}` | Disk Load Peak | Disk Activity: **{{m3_disk_act}}%**<br>Write: {{m3_write}} MB/s \| CPU: {{m3_cpu}}% | Highest disk activity percentage recorded across the entire log file. |
| `{{time_milestone_4}}` | CPU Peak | CPU Used: **{{m4_cpu}}%** (Free: {{m4_cpu_free}}%)<br>RAM: {{m4_ram}} GB ({{m4_ram_pct}}%) | Maximum CPU utilization recorded; driven by top active processes. |
| `{{time_milestone_5}}` | Kernel Action | Memory Compression: **{{m5_mc_mem}} MB**<br>System RAM: {{m5_sys_ram}} GB | First appearance of Memory Compression process in TopProcesses. |
| `{{time_milestone_6}}` | Battery 100% | Battery: **{{m6_bat}}%** (Status: {{m6_bat_status}})<br>Power: {{m6_power_source}} | Battery percentage reached full 100% capacity and remained through session end. |
| `{{time_milestone_7}}` | RAM Peak | RAM Used: **{{m7_ram_used}} GB ({{m7_ram_used_pct}}%)**<br>RAM Free: **{{m7_ram_free}} GB**<br>Top Process: {{m7_top_mem}} MB ({{m7_top_mem_pct}}%) | Maximum RAM consumption recorded across the entire session. |
| `{{time_milestone_8}}` | Session Close | CPU: {{m8_cpu}}% \| RAM: {{m8_ram}} GB ({{m8_ram_pct}}%)<br>Drive C: {{m8_disk}} GB free (-{{m8_disk_delta}} GB net) | Final logged record. {{m8_summary_note}} |

---

### 5. Data-Driven Observations from Logged Metrics

| Observation Domain | Numeric Evidence from JSON Log | Direct Finding |
| :--- | :--- | :--- |
| **Memory Trajectory** | {{obs_mem_evidence}} | {{obs_mem_finding}} |
| **Storage Consumption** | {{obs_storage_evidence}} | {{obs_storage_finding}} |
| **Compute Efficiency** | {{obs_compute_evidence}} | {{obs_compute_finding}} |