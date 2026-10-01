from datetime import datetime
import json
import logging
import os
import sys

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
        logging.FileHandler(os.path.join(_LOG_DIR, "addition_pipeline.log"), encoding="utf-8")
    ]
)
log = logging.getLogger("AdditionPipeline")


# ─────────────────────────────────────────────
# 2. CORE MATHEMATICAL & PIPELINE FUNCTIONS
# ─────────────────────────────────────────────
def safe_add(a: float | int, b: float | int) -> float | int:
    """Do numbers ka secure addition with type checking."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Invalid types provided for addition: {type(a)}, {type(b)}")
    return a + b


def process_batch_additions(data_batches: list[tuple[float, float]]) -> list[dict]:
    """Multiple pairs ko batch mein process karta hai aur detailed results return karta hai."""
    results = []
    log.info(f"🔄 Starting batch processing for {len(data_batches)} pairs...")
    
    for idx, pair in enumerate(data_batches, start=1):
        try:
            val1, val2 = pair
            ans = safe_add(val1, val2)
            results.append({
                "row_id": idx,
                "input_a": val1,
                "input_b": val2,
                "result": ans,
                "status": "SUCCESS"
            })
        except Exception as exc:
            log.error(f"❌ Error at row {idx} with pair {pair}: {exc}")
            results.append({
                "row_id": idx,
                "input_a": pair[0] if len(pair) > 0 else None,
                "input_b": pair[1] if len(pair) > 1 else None,
                "result": None,
                "status": f"FAILED: {str(exc)}"
            })
            
    log.info("✅ Batch processing completed.")
    return results


# ─────────────────────────────────────────────
# 3. MAIN EXECUTION PIPELINE
# ─────────────────────────────────────────────
def main() -> None:
    log.info("🚀 Deep Addition Pipeline initialized.")

    # Sample input dataset
    number_batches = [
        (10.5, 20.3),
        (100, 250),
        (-50, 75.25),
        (0.001, 0.002),
        (42, 58)
    ]

    # Batch processing run karein
    processed_output = process_batch_additions(number_batches)

    # Total sum calculate karein successful results ka
    successful_sums = [item["result"] for item in processed_output if item["status"] == "SUCCESS"]
    grand_total = sum(successful_sums)
    
    log.info(f"📊 Grand Total of all successful additions: {grand_total}")

    # Output data ko JSON format mein structure karna
    pipeline_payload = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_records": len(number_batches),
        "successful_records": len(successful_sums),
        "grand_total": grand_total,
        "details": processed_output
    }

    # JSON file mein export karna
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_json_path = os.path.join(script_dir, "addition_report.json")

    try:
        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(pipeline_payload, f, indent=4)
        log.info(f"💾 Report successfully exported to: {output_json_path}")
    except Exception as exc:
        log.critical(f"❌ Failed to write JSON report: {exc}")
        sys.exit(1)

    log.info("👋 Pipeline executed cleanly.")


if __name__ == "__main__":
    main()