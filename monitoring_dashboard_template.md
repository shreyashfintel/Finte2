# System Monitoring Dashboard
**Technical Documentation & Management Report**

---

## 1. Executive Summary
The **System Monitoring Dashboard** is a lightweight, real-time PowerShell-based monitoring solution developed to provide continuous visibility into the health and performance of Windows-based systems. It automates critical metrics collection, replacing manual checks via Task Manager or Performance Monitor.

- **Real-Time Monitoring:** 5-second automated refresh cycle for system resources.
- **Early Incident Detection:** Identify abnormal spikes before service impact.
- **Rapid Root Cause Analysis:** Immediate identification of top resource-consuming processes.
- **Historical Logging:** Continuous structured JSONL logging for post-incident reviews and capacity planning.

---

## 2. Solution Overview

- **Refresh Rate:** 5 seconds polling interval
- **Architecture:** Lightweight PowerShell background process (zero third-party dependencies)
- **Log Format:** JSON Lines (`.jsonl`)
- **Monitored Resource Categories:**
  1. CPU (Processor) Utilization
  2. Memory (RAM) Utilization
  3. Disk Activity (I/O Throughput)
  4. Disk Capacity (Storage Usage)

---

## 3. Monitoring Categories

<table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
  <thead>
    <tr style="background-color: #1a4b75; color: #ffffff; text-align: left;">
      <th style="padding: 10px; border: 1px solid #dcdcdc; width: 22%;">Module</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc; width: 38%;">Key Metrics Displayed</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc; width: 40%;">Operational Value & Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #dcf1de; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold; vertical-align: top;">3.1 CPU Monitoring</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; vertical-align: top;">
        • CPU utilization percentage (used)<br>
        • CPU availability percentage (free)<br>
        • Identification of top CPU-consuming processes
      </td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; vertical-align: top;">
        Determines processor load, detects applications consuming disproportionate compute resources, and confirms if CPU saturation is causing degradation.
      </td>
    </tr>
    <tr style="background-color: #fef4cf; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold; vertical-align: top;">3.2 Memory (RAM) Monitoring</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; vertical-align: top;">
        • Total installed RAM<br>
        • Currently used RAM<br>
        • Available free RAM<br>
        • Identification of top memory-consuming processes
      </td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; vertical-align: top;">
        Assists in identifying memory pressure, isolates high-RAM consumers, and anticipates stability issues caused by insufficient memory.
      </td>
    </tr>
    <tr style="background-color: #ffdada; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold; vertical-align: top;">3.3 Disk Activity Monitoring</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; vertical-align: top;">
        • Current disk activity percentage<br>
        • Read throughput speed<br>
        • Write throughput speed<br>
        • Identification of top disk I/O-consuming processes
      </td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; vertical-align: top;">
        Reveals storage subsystem load, detects excessive disk operations per application, and diagnoses throughput bottlenecks.
      </td>
    </tr>
    <tr style="background-color: #f0f4f8; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold; vertical-align: top;">3.4 Disk Capacity Monitoring</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; vertical-align: top;">
        • Total storage capacity per drive<br>
        • Remaining free space per drive<br>
        • Usage percentage per drive
      </td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; vertical-align: top;">
        Identifies drives approaching capacity limits, determines cleanup requirements, and prevents application crashes due to full disks.
      </td>
    </tr>
  </tbody>
</table>
---

## 4. Alerting Frameworks

### 4.1 Color-Coded Health Status System

<table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
  <thead>
    <tr style="background-color: #1a4b75; color: #ffffff; text-align: left;">
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Color</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Status</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #dcf1de; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold;">Green</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Normal</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">System is operating within acceptable parameters. No action required.</td>
    </tr>
    <tr style="background-color: #fef4cf; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold;">Yellow</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Warning</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Resource is under elevated load. Monitor closely and be prepared to act.</td>
    </tr>
    <tr style="background-color: #ffdada; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold;">Red</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Critical</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Resource has exceeded critical thresholds. Immediate attention may be required.</td>
    </tr>
  </tbody>
</table>

---

### 4.2 Configured Alert Thresholds

#### CPU Utilization Thresholds

<table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
  <thead>
    <tr style="background-color: #1a4b75; color: #ffffff; text-align: left;">
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Status</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Usage Range</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Audible Alert Trigger</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #dcf1de; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Green</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Below 75%</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">No alert</td>
    </tr>
    <tr style="background-color: #fef4cf; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Yellow</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">75% – 89%</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">No alert – monitor closely</td>
    </tr>
    <tr style="background-color: #ffdada; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Red</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">90% and above</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold;">Audible alert triggered</td>
    </tr>
  </tbody>
</table>

#### RAM (Memory) Utilization Thresholds

<table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
  <thead>
    <tr style="background-color: #1a4b75; color: #ffffff; text-align: left;">
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Status</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Usage Range</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Audible Alert Trigger</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #dcf1de; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Green</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Below 50%</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">No alert</td>
    </tr>
    <tr style="background-color: #fef4cf; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Yellow</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">50% – 79%</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">No alert – monitor closely</td>
    </tr>
    <tr style="background-color: #ffdada; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Red</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">80% and above</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold;">Audible alert triggered</td>
    </tr>
  </tbody>
</table>

#### Disk Activity Thresholds

<table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
  <thead>
    <tr style="background-color: #1a4b75; color: #ffffff; text-align: left;">
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Status</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Usage Range</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Audible Alert Trigger</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #dcf1de; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Green</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Below 60%</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">No alert</td>
    </tr>
    <tr style="background-color: #fef4cf; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Yellow</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">60% – 84%</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">No alert – monitor closely</td>
    </tr>
    <tr style="background-color: #ffdada; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Red</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">85% and above</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold;">Audible alert triggered</td>
    </tr>
  </tbody>
</table>

#### Disk Capacity Thresholds

<table style="width: 100%; border-collapse: collapse; margin-bottom: 25px;">
  <thead>
    <tr style="background-color: #1a4b75; color: #ffffff; text-align: left;">
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Status</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Usage Range</th>
      <th style="padding: 10px; border: 1px solid #dcdcdc;">Audible Alert Trigger</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #dcf1de; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Green</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Below 80%</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">No alert</td>
    </tr>
    <tr style="background-color: #fef4cf; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Yellow</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">80% – 89%</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">No alert – monitor closely</td>
    </tr>
    <tr style="background-color: #ffdada; color: #111111;">
      <td style="padding: 10px; border: 1px solid #dcdcdc;">Red</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc;">90% and above</td>
      <td style="padding: 10px; border: 1px solid #dcdcdc; font-weight: bold;">Audible alert triggered</td>
    </tr>
  </tbody>
</table>

---

### 4.3 Audible Alert System
Audible notification triggers immediately whenever any monitored metric enters the **Red** threshold:
- CPU utilization $\ge$ 90%
- RAM utilization $\ge$ 80%
- Disk activity $\ge$ 85%
- Disk capacity $\ge$ 90%

---

## 5. Process Visibility & Root Cause Analysis
Surfaces top consuming processes in real-time to answer:
- Which application is consuming the most CPU?
- Which process is causing memory pressure?
- Which process is driving disk I/O bottlenecks?

---

## 6. Historical Data Logging (JSONL)
- Records 1 entry every 5 seconds.
- Lightweight, append-only format for post-incident audits and capacity baseline planning.

---

## 7. Business Value & Operational Benefits
- **Early Problem Detection:** Visual and audible alerts mitigate unplanned downtime.
- **Rapid Troubleshooting:** Process-level attribution shortens MTTR.
- **Audit & Compliance:** Complete historical time-series performance tracking.

---

## 8. Conclusion & Recommendations
- Deploy across mission-critical Windows endpoints.
- Establish JSONL log retention and rotation schedules.
- Regularly review and adjust thresholds against evolving application baseline profiles.