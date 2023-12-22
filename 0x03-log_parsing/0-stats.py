#!/usr/bin/python3
import sys


total_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        parts = line.split()
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_size += file_size

            # Update status code counts
            if status_code.isdigit():
                status_code = int(status_code)
                status_counts[status_code] = \
                    status_counts.get(status_code, 0) + 1

            # Print stats after every 10 lines
            if i % 10 == 0:
                print(f"File size: {total_size}")
                for status_code in sorted(status_counts):
                    print(f"{status_code}: {status_counts[status_code]}")
except KeyboardInterrupt:
    pass  # Handle Ctrl+C

    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")
