from datetime import datetime
import os


current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"[{current_time}] Demo python script successfully run ")


script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "cron_output.txt")

with open(log_path, "a", encoding="utf-8") as f:
    f.write(f"Script executed at: {current_time}\n")

print(f"Output successfully written to: {log_path}")