from datetime import datetime
import json
import logging
import os
import sys
import time

# ─────────────────────────────────────────────
# 1. LOGGING CONFIGURATION
# ─────────────────────────────────────────────
_LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Logs")
os.makedirs(_LOG_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  [%(name)-15s]  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(os.path.join(_LOG_DIR, "continuous_pipeline.log"), encoding="utf-8")
    ]
)
log = logging.getLogger("ContinuousPipeline")


# ─────────────────────────────────────────────
# 2. CORE LOGIC
# ─────────────────────────────────────────────
def safe_add(a: float | int, b: float | int) -> float | int:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Invalid types: {type(a)}, {type(b)}")
    return a + b


def run_pipeline_iteration(iteration_count: int) -> None:
    log.info(f"🔄 Starting Pipeline Iteration #{iteration_count}")

    number_batches = [
        (10.5, 20.3),
        (100, 250),
        (-50, 75.25),
        (0.001, 0.002),
        (42, 58)
    ]

    results = []
    for idx, pair in enumerate(number_batches, start=1):
        try:
            ans = safe_add(pair[0], pair[1])
            results.append({
                "row_id": idx,
                "input_a": pair[0],
                "input_b": pair[1],
                "result": ans,
                "status": "SUCCESS"
            })
        except Exception as exc:
            log.error(f"❌ Error at row {idx}: {exc}")
            results.append({
                "row_id": idx,
                "result": None,
                "status": f"FAILED: {exc}"
            })

    successful_sums = [item["result"] for item in results if item["status"] == "SUCCESS"]
    grand_total = sum(successful_sums)

    payload = {
        "iteration": iteration_count,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "grand_total": grand_total,
        "details": results
    }

    # JSON export
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_json_path = os.path.join(script_dir, "continuous_report.json")

    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=4)

    log.info(f"✅ Iteration #{iteration_count} completed. Grand Total: {grand_total}")


# ─────────────────────────────────────────────
# 3. CONTINUOUS DAEMON LOOP
# ─────────────────────────────────────────────
def main() -> None:
    log.info("🚀 Continuous Pipeline Daemon started.")
    
    iteration = 1
    # Sleep interval in seconds (e.g., har 10 seconds mein ek baar run hoga, aap isko apne mutabiq badal sakte hain)
    sleep_interval = 10 

    try:
        while True:
            run_pipeline_iteration(iteration)
            iteration += 1
            
            log.info(f"💤 Sleeping for {sleep_interval} seconds...\n")
            time.sleep(sleep_interval)
            
    except KeyboardInterrupt:
        log.info("🛑 Pipeline stopped manually by user.")
    except Exception as exc:
        log.critical(f"🔥 Critical daemon crash: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()