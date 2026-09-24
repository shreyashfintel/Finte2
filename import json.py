import json
import pandas as pd

file_path = "system_metrics.jsonl"  # Replace with your file path

records = []
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            records.append(json.loads(line))

# ---------------------------------------------------------
# 1. Primary Metrics DataFrame (Flat Fields & Summaries)
# ---------------------------------------------------------
# Flatten top-level scalar values, Space, ReadWrite, and PostgreSQL status
df_metrics = pd.json_normalize(records)

# Drop raw nested structures from the primary tabular view
df_summary = df_metrics.drop(
    columns=[
        "Disk.TopProcesses",
        "RAM.TopProcesses",
        "CPU.TopProcesses"
    ],
    errors="ignore"
)

# Convert timestamp column to proper datetime dtype
df_summary["Timestamp"] = pd.to_datetime(df_summary["Timestamp"])

# ---------------------------------------------------------
# 2. Extract & Normalize Inconsistent Sub-structures
# ---------------------------------------------------------
def normalize_top_processes(raw_records, parent_key, sub_key):
    """
    Normalizes fields where the value can be:
    - a list of dicts: [{'InstanceName': 'postgres', 'MBs': 6.09}, ...]
    - a single dict: {'InstanceName': 'python', 'MBs': 2.41}
    - an empty dict: {}
    """
    normalized_rows = []
    for entry in raw_records:
        ts = entry.get("Timestamp")
        sub_obj = entry.get(parent_key, {}).get(sub_key, [])
        
        if isinstance(sub_obj, dict):
            if sub_obj:  # Non-empty single dict
                row = sub_obj.copy()
                row["Timestamp"] = ts
                normalized_rows.append(row)
        elif isinstance(sub_obj, list):
            for item in sub_obj:
                if isinstance(item, dict):
                    row = item.copy()
                    row["Timestamp"] = ts
                    normalized_rows.append(row)
                    
    df_proc = pd.DataFrame(normalized_rows)
    if not df_proc.empty and "Timestamp" in df_proc.columns:
        df_proc["Timestamp"] = pd.to_datetime(df_proc["Timestamp"])
    return df_proc

# Extract normalized child tables
df_disk_proc = normalize_top_processes(records, "Disk", "TopProcesses")
df_ram_proc = normalize_top_processes(records, "RAM", "TopProcesses")
df_cpu_proc = normalize_top_processes(records, "CPU", "TopProcesses")

# ---------------------------------------------------------
# 3. Export Cleaned Datasets to CSV & JSON
# ---------------------------------------------------------
# Export Summary Metrics
df_summary.to_csv("system_summary_metrics.csv", index=False)
df_summary.to_json("system_summary_metrics.json", orient="records", date_format="iso", indent=2)

# Export Normalized Process Details to CSV
df_disk_proc.to_csv("disk_top_processes.csv", index=False)
df_ram_proc.to_csv("ram_top_processes.csv", index=False)
df_cpu_proc.to_csv("cpu_top_processes.csv", index=False)

print(f"Successfully processed {len(df_summary)} health log events.")