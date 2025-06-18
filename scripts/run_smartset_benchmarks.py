#
# This script will run only smartset benchmarks in tests/smartset/test_benchmarks.py
# It saves the results to .benchmarks/smartset_benchmark_<timestamp>.json
# and prints the results out to the console.
#

import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

def main():
    # Add project root to PATH
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

    timestamp = datetime.now().strftime("%m%d%Y-%H%M")

    root = Path(__file__).resolve().parents[1]
    smartset_benchmarks = Path(root).joinpath('tests', 'smartset', 'test_benchmarks.py')
    logs_dir = Path(root).joinpath('logs', '.benchmarks')
    logs_dir.mkdir(parents=True, exist_ok=True)

    if smartset_benchmarks.exists():
        command = f'pytest {str(smartset_benchmarks)} --benchmark-only --benchmark-save=smartest_benchmark_{timestamp} --benchmark-storage={str(logs_dir)}'
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f'ERROR: Subprocess: {e}')

if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print(f'ERROR: Cannot find file: {e}')
    except Exception as e:
        print(f'ERROR: {e}')