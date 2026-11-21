
from pathlib import Path
import argparse
import hashlib

# Project test-data directory
DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "original"

def generate_files(count):
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    for i in range(1, count + 1):
        file_path = DATA_DIR / f"sample_{i:03d}.txt"

        content = (
            f"Sample File: {i}\n"
            "Project: Ransomware Defense and Recovery\n"
            "Purpose: Backup and recovery testing\n"
            f"Test Data: {hashlib.sha256(str(i).encode()).hexdigest()}\n"
        )

        file_path.write_text(content, encoding="utf-8")

    print(f"Successfully generated {count} sample files!")
    print(f"Location: {DATA_DIR}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=100)
    args = parser.parse_args()

    if args.count < 1:
        parser.error("Count must be at least 1")

    generate_files(args.count)
